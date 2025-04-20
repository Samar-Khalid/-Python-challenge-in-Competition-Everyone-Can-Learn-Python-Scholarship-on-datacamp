# Import required libraries
import pandas as pd

# Load the dataset
df = pd.read_csv('CO2 Emissions_Canada.csv')

# Convert the 'Engine Size(L)' column to numeric type
df['Engine Size(L)'] = pd.to_numeric(df['Engine Size(L)'], errors='coerce')

# Convert the 'Fuel Consumption Comb (mpg)' column to numeric type
df['Fuel Consumption Comb (L/100 km)'] = pd.to_numeric(df['Fuel Consumption Comb (L/100 km)'], errors='coerce')

# Convert the 'CO2 Emissions(g/km)' column to numeric type
df['CO2 Emissions(g/km)'] = pd.to_numeric(df['CO2 Emissions(g/km)'], errors='coerce')

# Median engine size in liters
print('Median engine size in liters:', df['Engine Size(L)'].median())

# Average fuel consumption for each fuel type
fuel_types = ['X', 'Z', 'E', 'D']
for fuel_type in fuel_types:
    fuel_type_df = df[df['Fuel Type'] == fuel_type]
    avg_fuel_consumption = fuel_type_df['Fuel Consumption Comb (L/100 km)'].mean()
    print(f'Average fuel consumption for fuel type {fuel_type}: {avg_fuel_consumption:.2f} L/100 km')

# Correlation between fuel consumption and CO2 emissions
correlation = df['CO2 Emissions(g/km)'].corr(df['Fuel Consumption Comb (L/100 km)'])
print('Correlation between fuel consumption and CO2 emissions:', correlation)

# Average CO2 emissions for each vehicle class
vehicle_classes = ['SUV - SMALL', 'MID-SIZE']
for vehicle_class in vehicle_classes:
    class_df = df[df['Vehicle Class'] == vehicle_class]
    avg_co2_emissions = class_df['CO2 Emissions(g/km)'].mean()
    print(f'Average CO2 emissions for vehicle class {vehicle_class}: {avg_co2_emissions:.2f} g/km')

# Average CO2 emissions for all vehicles and vehicles with an engine size of 2.0 liters or smaller
all_vehicles_avg_co2_emissions = df['CO2 Emissions(g/km)'].mean()
print('Average CO2 emissions for all vehicles:', all_vehicles_avg_co2_emissions)

small_engine_df = df[df['Engine Size(L)'] <= 2.0]
small_engine_avg_co2_emissions = small_engine_df['CO2 Emissions(g/km)'].mean()
print('Average CO2 emissions for vehicles with an engine size of 2.0 liters or smaller:', small_engine_avg_co2_emissions)

# Additional insights
# We can find the top 10 vehicles with the lowest CO2 emissions using the following code
top_10_lowest_co2_emissions = df.nsmallest(10, 'CO2 Emissions(g/km)')
print('Top 10 vehicles with the lowest CO2 emissions:')
print(top_10_lowest_co2_emissions[['Make', 'Model', 'Vehicle Class', 'CO2 Emissions(g/km)']])
