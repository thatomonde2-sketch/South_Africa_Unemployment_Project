import pandas as pd
import matplotlib.pyplot as plt
import requests

# World Bank API JSON link for South Africa unemployment
url = "https://api.worldbank.org/v2/country/ZAF/indicator/SL.UEM.TOTL.ZS?format=json"

# Download JSON data
response = requests.get(url)
data_json = response.json()

# Extract the actual data part
records = data_json[1]

# Convert to DataFrame
data = pd.DataFrame(records)

# Keep only Year and Value
data = data[["date", "value"]]

# Rename columns
data = data.rename(columns={"date": "Year", "value": "Unemployment_Rate"})

# Convert to numbers
data["Year"] = pd.to_numeric(data["Year"])
data["Unemployment_Rate"] = pd.to_numeric(data["Unemployment_Rate"])

# Remove missing values
data_clean = data.dropna()

# Sort by Year
data_clean = data_clean.sort_values("Year")

# Show sample table
print("Sample Data Table:")
print(data_clean.head(10))

# Save table to Excel
data_clean.to_excel("unemployment_table.xlsx", index=False)

# Plot graph
plt.plot(data_clean["Year"], data_clean["Unemployment_Rate"])
plt.xlabel("Year")
plt.ylabel("Unemployment Rate (%)")
plt.title("South Africa Unemployment Rate Over Time")
plt.savefig("unemployment_graph.png")
plt.show()





