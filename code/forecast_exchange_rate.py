import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ===============================
# STEP 1: LOAD EXCEL DATA
# ===============================

file_path = "../data/South_Africa_Exchange_Rate.xlsx"
data = pd.read_excel(file_path)

# Fix column names using second row
data.columns = data.iloc[1]
data = data.drop(index=[0, 1])  # remove metadata rows
data.reset_index(drop=True, inplace=True)

# Keep only South Africa
data = data[data["Country Name"] == "South Africa"]

# ===============================
# STEP 2: CONVERT TO LONG FORMAT
# ===============================

data_long = data.melt(
    id_vars=["Country Name"],
    var_name="Year",
    value_name="Exchange_Rate"
)

# Convert Year and Exchange Rate to numbers
data_long["Year"] = pd.to_numeric(data_long["Year"], errors="coerce")
data_long["Exchange_Rate"] = pd.to_numeric(data_long["Exchange_Rate"], errors="coerce")

# Remove missing values
data_long = data_long.dropna()

print("FIRST ROWS OF CLEAN DATA:")
print(data_long.head())

# ===============================
# STEP 3: DESCRIPTIVE STATISTICS
# ===============================

print("\nDESCRIPTIVE STATISTICS")
print(data_long["Exchange_Rate"].describe())

# ===============================
# STEP 4: TREND REGRESSION
# ===============================

# Create time index t
data_long["t"] = np.arange(len(data_long))

# Regression
coefficients = np.polyfit(data_long["t"], data_long["Exchange_Rate"], 1)
trend = np.poly1d(coefficients)
data_long["Trend"] = trend(data_long["t"])

print("\nTREND REGRESSION EQUATION:")
print(f"Exchange Rate = {coefficients[0]} * t + {coefficients[1]}")

# ===============================
# STEP 5: FORECAST NEXT 10 YEARS
# ===============================

future_t = np.arange(len(data_long), len(data_long) + 10)
future_years = np.arange(data_long["Year"].max() + 1, data_long["Year"].max() + 11)
forecast_rates = trend(future_t)

forecast_df = pd.DataFrame({
    "Year": future_years,
    "Forecast_Exchange_Rate": forecast_rates
})

# ===============================
# STEP 6: SAVE DATA FILES
# ===============================

data_long.to_csv("../output/exchange_rate_clean.csv", index=False)
forecast_df.to_csv("../output/exchange_rate_forecast.csv", index=False)

# ===============================
# STEP 7: GRAPH
# ===============================

plt.figure(figsize=(12,6))
plt.plot(data_long["Year"], data_long["Exchange_Rate"], label="Actual Exchange Rate")
plt.plot(data_long["Year"], data_long["Trend"], linestyle="--", label="Trend Line")
plt.plot(future_years, forecast_rates, linestyle=":", label="Forecast")

plt.xlabel("Year")
plt.ylabel("ZAR per USD")
plt.title("South Africa Exchange Rate Trend and Forecast")
plt.legend()
plt.grid()

# Save graph
plt.savefig("../output/exchange_rate_forecast.png")
plt.show()

