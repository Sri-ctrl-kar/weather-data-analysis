# Weather Data Visualizer: Australian Climate Analysis

## 📌 Project Overview
This project is a data analysis and visualization tool built using Python. It processes historical weather data from the **Australian Bureau of Meteorology** (specifically focusing on the **Albury** weather station) to identify climate trends, rainfall patterns, and temperature correlations.

The project demonstrates key data science skills including data cleaning, statistical analysis, and visualization using the `Pandas`, `NumPy`, and `Matplotlib` libraries.

## 📂 Dataset Description
The dataset used is `weatherAUS.csv` (Weather in Australia), sourced from [Kaggle](https://www.kaggle.com/datasets/jsphyg/weather-dataset-rattle-package).

**Key Columns Processed:**
- **Date:** The date of observation.
- **MinTemp / MaxTemp:** Used to calculate the daily average `Temperature`.
- **Rainfall:** The amount of rainfall recorded for the day in mm.
- **Humidity9am / Humidity3pm:** Used to calculate the daily average `Humidity`.

## 🛠️ Tools & Technologies
- **Python 3.x**
- **Pandas:** For data manipulation, cleaning, and aggregation.
- **NumPy:** For high-performance statistical calculations.
- **Matplotlib:** For generating static data visualizations.

## ⚙️ Key Features & Methodology
1. **Data Cleaning:**
   - Filtered dataset to focus on a single location (`Albury`) for clear trend analysis.
   - Derived new columns: `Temperature` (avg of Min/Max) and `Humidity` (avg of 9am/3pm).
   - Handled missing values (NaN) by imputing column means or zeroes for rainfall.
   
2. **Statistical Analysis:**
   - Computed global statistics: Mean, Maximum, Minimum Temperature, and Total Cumulative Rainfall.

3. **Visualization:**
   - **Line Chart:** Displays daily temperature trends over the first year.
   - **Scatter Plot:** Analyzes the correlation between Humidity and Temperature.
   - **Bar Chart:** Aggregates and compares Total Rainfall by Month.

4. **Export:**
   - Saves the processed data to `cleaned_weather_data.csv`.
   - Exports all charts as `.png` images.

## 📊 Results & Insights
Upon running the analysis, the following insights were visualized:
- **Temperature Trends:** Seasonal variations are clearly visible in the `temp_trend.png` line chart.
- **Rainfall Patterns:** The `monthly_rainfall.png` bar chart highlights the wettest months of the year for the selected location.
- **Humidity vs. Temp:** The `humidity_vs_temp.png` scatter plot generally shows an inverse relationship (higher temperatures often correlate with lower humidity).

## 🚀 How to Run
1. **Prerequisites:**
   Ensure you have Python installed. Install the required libraries:
   ```bash
   pip install pandas numpy matplotlib
