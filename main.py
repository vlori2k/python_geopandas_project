import geopandas as gpd
from pathlib import Path

from datareader import DataReader
from csv_generator import CSVGenerator
from plot_generator import PlotGenerator



# Directories
data_dir = Path("data")
output_dir = Path("output")

# Initialize helpers
reader = DataReader(data_dir)
csv_generator = CSVGenerator(output_dir)
plot_generator = PlotGenerator()

# Read data
countries = reader.read_countries()
cities = reader.read_cities()

print(f"Loaded {len(countries)} countries")
print(f"Loaded {len(cities)} cities")

# Spatial join
joined = gpd.sjoin(cities, countries, how="left", predicate="within")

print("Spatial join completed")
print(joined.head())

# Save result to CSV
csv_generator.save(gdf=joined, filename="cities_with_countries.csv")

# Plot
plot_generator.plot_countries_and_cities(countries=countries, cities=cities, title="Cities and Countries (GeoPandas Spatial Join)")