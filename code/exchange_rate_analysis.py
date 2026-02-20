import pandas as pd

# Load the Excel file WITHOUT headers
file_path = "../data/South_Africa_Exchange_Rate.xlsx"
raw = pd.read_excel(file_path, header=None)

# Show raw data (for debugging)
print("RAW DATA PREVIEW:")
print(raw.head())

# Set row 1 as column names
raw.columns = raw.iloc[1]

# Remove the first two rows (metadata + header row)
data = raw.drop([0, 1]).reset_index(drop=True)

# Rename first column to Country
data.rename(columns={data.columns[0]: "Country"}, inplace=True)

# Convert wide format to long format (Year, Exchange Rate)
data_long = data.melt(id_vars=["Country"], var_name="Year", value_name="Exchange_Rate")

# Convert Year to numeric
data_long["Year"] = pd.to_numeric(data_long["Year"])
data_long["Exchange_Rate"] = pd.to_numeric(data_long["Exchange_Rate"])

# Filter only South Africa
sa_data = data_long[data_long["Country"] == "South Africa"]

# Show cleaned data
print("\nCLEANED DATA:")
print(sa_data.head())

# Save cleaned dataset
sa_data.to_csv("../data/clean_exchange_rate_sa.csv", index=False)

print("\nClean dataset saved as clean_exchange_rate_sa.csv")
