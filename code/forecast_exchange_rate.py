# ================================
# SOUTH AFRICA EXCHANGE RATE FORECAST PROJECT
# Phase 3: Trend Regression and Visualization
# Author: Thato Mokgosi
# ================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# ================================
# STEP 1: LOAD DATA
# ================================

file_path = "../data/South_Africa_Exchange_Rate.xlsx"

# Load Excel file
data = pd.read_excel(file_path)

# Fix header problem (your data has header in row 1)
data.columns = data.iloc[1]
data = data.drop([0,1]).reset_index(drop=True)

# Convert years to numeric
data = data.melt(id_vars=["Country Name"], var_name="Year", value_name="Exchange_Rate")

# Convert to correct data types
data["Year"] = pd.to_numeric(data["Year"])
data["Exchange_Rate"] = pd.to_numeric(data["Exchange_Rate"])

# Keep only South Africa
data = data[data["Country Name"] == "South Africa"]

print("FIRST ROWS OF CLEAN DATA:")
print(data.head())

# ================================
# STEP 2: DESCRIPTIVE STATISTICS
# ================================

print("\nDESCRIPTIVE STATISTICS")
print(data["Exchange_Rate"].describe())

# ================================
# STEP 3: TREND REGRESSION MODEL
# ================================

# Create time index variable t
data["t"] = np.arange(len(data))

# Regression
X = data[["t"]]
y = data["Exchange_Rate"]

model = LinearRegression()
model.fit(X, y)

# Trend values
data["Trend"] = model.predict(X)

# Print regression equation
print("\nTREND REGRESSION EQUATION:")
print("Exchange Rate =", model.coef_[0], "* t +", model.intercept_)

# ================================
# STEP 4: PLOT ACTUAL VS TREND
# ================================

plt.figure(figsize=(14,7))

# Actual data
plt.plot(data["Year"], data["Exchange_Rate"], label="Actual Exchange Rate", linewidth=2)

# Trend line
plt.plot(data["Year"], data["Trend"], linestyle="--", linewidth=3, label="Trend Line")

# Graph settings
plt.title("South Africa Exchange Rate Trend (1960–2024)")
plt.xlabel("Year")
plt.ylabel("Exchange Rate (ZAR per USD)")
plt.legend()
plt.grid(True)

# Optional zoom (remove if you want full scale)
plt.ylim(0, 20)

# Save graph
plt.savefig("../output/exchange_rate_trend.png")

# Show graph
plt.show()

# ================================
# STEP 5: SAVE CLEAN DATA FOR REPORT
# ================================

data.to_csv("../output/clean_exchange_rate_data.csv", index=False)
print("\nClean dataset saved to output folder.")
