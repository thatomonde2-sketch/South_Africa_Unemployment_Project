import pandas as pd
import requests
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# Download unemployment data
url = "https://api.worldbank.org/v2/country/ZAF/indicator/SL.UEM.TOTL.ZS?date=1990:2023&format=json"
response = requests.get(url)
data = response.json()[1]

# Convert to DataFrame
df = pd.DataFrame(data)[["date", "value"]]
df.columns = ["Year", "Unemployment_Rate"]

# Clean data
df["Year"] = df["Year"].astype(int)
df = df.sort_values("Year")
df = df.dropna()

# Save cleaned data
df.to_excel("unemployment_sa.xlsx", index=False)

# Plot historical data
plt.figure()
plt.plot(df["Year"], df["Unemployment_Rate"])
plt.title("Unemployment Rate in South Africa")
plt.xlabel("Year")
plt.ylabel("Unemployment Rate (%)")
plt.show()

# ---- FORECASTING ----
model = ARIMA(df["Unemployment_Rate"], order=(1,1,1))
model_fit = model.fit()

forecast = model_fit.forecast(steps=10)

# Plot forecast
plt.figure()
plt.plot(df["Year"], df["Unemployment_Rate"], label="Historical")
plt.plot(range(df["Year"].max()+1, df["Year"].max()+11), forecast, label="Forecast")
plt.legend()
plt.title("Forecast of Unemployment Rate in South Africa")
plt.xlabel("Year")
plt.ylabel("Unemployment Rate (%)")
plt.show()