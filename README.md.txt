# South Africa Exchange Rate Analysis Project

## Project Overview  
This project analyses the South African exchange rate over time using Python and Excel.  
The objective is to clean historical exchange rate data, perform descriptive statistics, estimate a trend regression model, and visualize the exchange rate trend and forecasts.

This project demonstrates skills in:
- Data cleaning  
- Python programming  
- Econometrics and regression analysis  
- Data visualization  
- Git and GitHub version control  

---

## Folder Structure  

Economic_project  
│  
├── code  
│   ├── exchange_rate_analysis.py  
│   ├── forecast_exchange_rate.py  
│  
├── data  
│   ├── South_Africa_Exchange_Rate.xlsx  
│  
├── output  
│   ├── exchange_rate_clean.csv  
│   ├── exchange_rate_trend_plot.png  
│  
├── report  
│   ├── Exchange_Rate_Report.pdf  
│  
└── README.md  

---

## Data Source  
The exchange rate data was obtained from the World Bank database and contains annual exchange rates for South Africa from 1960 to 2024.

---

## Methodology  

### Phase 1: Data Cleaning  
- Loaded Excel data using pandas  
- Converted wide format to long format  
- Removed missing values  
- Saved cleaned dataset to CSV  

### Phase 2: Descriptive Statistics  
- Calculated mean, standard deviation, minimum, and maximum exchange rates  
- Summarised long-run exchange rate behaviour  

### Phase 3: Trend Regression  
- Estimated a linear time trend regression model  
- Exchange Rate = α + βt  
- Forecasted future exchange rates using the trend model  

### Phase 4: Visualisation  
- Plotted actual exchange rates  
- Plotted regression trend line  
- Saved graphs for the report  

---

## How to Run the Code  

1. Open the project folder in Visual Studio Code or Anaconda Prompt  
2. Navigate to the code folder  

