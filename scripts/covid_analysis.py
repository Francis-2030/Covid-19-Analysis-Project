import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# 1. Set up paths correctly
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path = os.path.join(project_root, 'data', 'raw', 'owid-covid-data.csv')

# 2. Load data with error handling
try:
    print(f"Looking for data at: {data_path}")
    covid_data = pd.read_csv(data_path)
    print("Successfully loaded COVID-19 data!")
except FileNotFoundError:
    print("\nERROR: Missing data file!")
    print("Please ensure:")
    print(f"1. A file named 'owid-covid-data.csv' exists in {os.path.dirname(data_path)}")
    print("2. You've downloaded it from: https://ourworldindata.org/covid-cases")
    exit()

# 3. Configure display
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

# 4. Data Exploration
print("\n=== Data Overview ===")
print(f"Dataset contains {len(covid_data)} rows with columns:")
print(covid_data.columns.tolist())

# 5. Data Cleaning
selected_countries = ['United States', 'India', 'Brazil', 'Germany', 'Kenya']
key_columns = ['date', 'location', 'total_cases', 'new_cases', 'total_deaths', 
               'new_deaths', 'total_vaccinations', 'people_vaccinated', 'population']

clean_data = (
    covid_data[covid_data['location'].isin(selected_countries)][key_columns]
    .sort_values(['location', 'date'])
)
clean_data['date'] = pd.to_datetime(clean_data['date'])

# 6. Analysis
latest_data = clean_data[clean_data['date'] == clean_data['date'].max()]

# 7. Visualization
plt.figure(figsize=(12, 6))
for country in selected_countries:
    country_data = clean_data[clean_data['location'] == country]
    plt.plot(country_data['date'], country_data['total_cases'], label=country)
plt.title("Total COVID-19 Cases by Country")
plt.xlabel("Date")
plt.ylabel("Cases")
plt.legend()
plt.tight_layout()
plt.show()