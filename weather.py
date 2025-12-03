import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# STEP 1: Data Acquisition & Loading

def load_data(filepath):
    """Loads CSV into a DataFrame and inspects it."""
    try:
        # Load the specific Australian Weather dataset
        df = pd.read_csv(filepath)
        print("--- Data Loaded Successfully ---")
        print(f"Total Rows: {len(df)}")
        print("Columns:", df.columns.tolist())
        return df
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found. Please check the file name.")
        return None


# STEP 2: Data Cleaning & Processing

def clean_data(df):
    """
    Adapts weatherAUS.csv columns to the assignment requirements:
    - Creates 'Temperature' from MinTemp/MaxTemp
    - Creates 'Humidity' from Humidity9am/Humidity3pm
    - Filters for a specific location to simulate 'local' weather
    """
    print("\n--- Cleaning Data ---")
    
    # 1. Filter for ONE location to make charts readable (Local Weather)
    # Change 'Albury' to 'Sydney', 'Melbourne', 'Brisbane' etc. as needed
    city = 'Albury' 
    df = df[df['Location'] == city].copy()
    print(f"Filtered data for location: {city}")

    # 2. Convert Date to Datetime
    df['Date'] = pd.to_datetime(df['Date'])
    
    # 3. Create composite 'Temperature' and 'Humidity' columns
    # Taking the average of Min/Max and 9am/3pm readings
    df['Temperature'] = (df['MinTemp'] + df['MaxTemp']) / 2
    df['Humidity'] = (df['Humidity9am'] + df['Humidity3pm']) / 2
    
    # 4. Handle Missing Values
    # Fill numeric gaps with the mean of that column
    cols_to_fill = ['Temperature', 'Humidity', 'Rainfall']
    for col in cols_to_fill:
        df[col] = df[col].fillna(df[col].mean())

    # 5. Select only the columns needed for the assignment
    final_cols = ['Date', 'Temperature', 'Humidity', 'Rainfall']
    df_clean = df[final_cols].copy()
    
    print("Data cleaning completed.")
    print(df_clean.head())
    return df_clean


# STEP 3: Statistical Analysis (NumPy)

def analyze_statistics(df):
    """Computes statistics using NumPy."""
    print("\n--- Statistical Analysis ---")
    
    temps = df['Temperature'].values
    rain = df['Rainfall'].values
    
    print(f"Temperature (Mean): {np.mean(temps):.2f}°C")
    print(f"Temperature (Max):  {np.max(temps):.2f}°C")
    print(f"Temperature (Min):  {np.min(temps):.2f}°C")
    print(f"Total Rainfall:     {np.sum(rain):.2f} mm")
    print("-" * 30)


# STEP 4: Visualization (Matplotlib)

def visualize_data(df):
    """Generates the 3 required plots."""
    print("\n--- Generating Plots ---")
    
    # Plot 1: Line Chart for Daily Temperature
    plt.figure(figsize=(10, 5))
    # We slice [:100] to show just the first 100 days so the chart isn't too crowded
    # Remove [:100] to plot ALL years (might be messy)
    plt.plot(df['Date'][:365], df['Temperature'][:365], label='Daily Avg Temp', color='tab:red')
    plt.title('Daily Temperature Trends (First Year)')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('temp_trend.png')
    plt.show()

    # Plot 2: Scatter Plot (Humidity vs Temperature)
    plt.figure(figsize=(8, 6))
    plt.scatter(df['Humidity'], df['Temperature'], alpha=0.5, c='blue', s=10)
    plt.title('Humidity vs. Temperature')
    plt.xlabel('Humidity (%)')
    plt.ylabel('Temperature (°C)')
    plt.grid(True)
    plt.savefig('humidity_vs_temp.png')
    plt.show()


# STEP 5: Grouping & Aggregation

def group_and_aggregate(df):
    """Groups data by Month and plots Rainfall."""
    print("\n--- Grouping Data ---")
    
    # Extract Month Name
    df['Month'] = df['Date'].dt.month_name()
    
    # Group by Month and sum Rainfall
    # Reindex ensures months are in calendar order
    month_order = [
        'January', 'February', 'March', 'April', 'May', 'June', 
        'July', 'August', 'September', 'October', 'November', 'December'
    ]
    monthly_rain = df.groupby('Month')['Rainfall'].sum().reindex(month_order)
    
    print("Total Rainfall by Month:")
    print(monthly_rain)

    # Plot 3: Bar Chart for Monthly Rainfall
    plt.figure(figsize=(10, 5))
    monthly_rain.plot(kind='bar', color='teal')
    plt.title('Total Monthly Rainfall')
    plt.ylabel('Rainfall (mm)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('monthly_rainfall.png')
    plt.show()

# STEP 6: Export

def export_data(df):
    """Exports the cleaned dataset."""
    output_file = 'cleaned_weather_data.csv'
    df.to_csv(output_file, index=False)
    print(f"\nCleaned data exported to '{output_file}'.")


# MAIN EXECUTION BLOCK

if __name__ == "__main__":
    # Point this to your uploaded file
    file_path = 'weatherAUS.csv'
    
    # Execute the pipeline
    weather_df = load_data(file_path)
    
    if weather_df is not None:
        weather_df = clean_data(weather_df)
        analyze_statistics(weather_df)
        visualize_data(weather_df)
        group_and_aggregate(weather_df)
        export_data(weather_df)
        print("\nAll tasks completed successfully!")