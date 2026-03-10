import geopandas as gpd
from pathlib import Path

from datareader import DataReader
from csv_generator import CSVGenerator
from plot_generator import PlotGenerator


# Directories
data_dir = Path("data")  # leser fra "data" mappa, som er i prosjektet her
output_dir = Path("output") # mappen hvor resultatene (CSV fila skal lagres)

# Initialize helpers
reader = DataReader(data_dir=data_dir)  # lager en ny objekt/instanse av klassen DataReader som er fra datareader.py
csv_generator = CSVGenerator(output_dir=output_dir) # lager en ny objekt/instanse av klassen CSVGenerator som er fra csv_generator.py
plot_generator = PlotGenerator() # lager en ny objekt/instanse av klassen PlotGenerator som er fra plot_generator.py

# Read data
countries = reader.read_countries()  # kaller funksjonen "read_countries" som er inne i DataReader klassen, denne leser filen "ne_110m_admin_0_countries.shp" som ligger inne i mappa : data/countries
                                     # deretter returnerer den data som en GeoDataFrame

cities = reader.read_cities()        # kaller funksjonen "read_cities" som mer inne i DataReader klassen, denne leser filen "ne_110m_populated_places.shp"  som ligger inn i mappa : data/cities
                                     # deretter returnerer den data som en GeoDataFrame

print(f"Loaded {len(countries)} countries") #printer antall land som er lastet
print(f"Loaded {len(cities)} cities")       #printer antall byer som er lastet

# Spatial join
"""
En spatial join betyr:

Vi kobler to datasett basert på geografisk posisjon, ikke tekst.

hva er spatial join og hvorfor er dette viktig i GIS?:

Spatial join brukes til å svare på spørsmål som:

hvilken kommune ligger et hus i?
hvilket land ligger en by i?
hvilken skogtype ligger en vei i?
hvilken sone ligger et område i?

Dette brukes i:
kart
byplanlegging
miljøanalyse
statistikk
navigasjon

enkelt og greit betyr spatial join: "Hvilket område ligger dette punktet i?"

"""
joined = gpd.sjoin(cities, countries, how="left", predicate="within")  # finner hvilket land hver by ligger i og kobler dataene sammen

print("Spatial join completed")
print(joined.head())

# Save result to CSV
csv_generator.save_to_CSV(gdf=joined, filename="cities_with_countries.csv") # lagrer resultatet av spatial joinen (byer + landet de ligger i) til en CSV fil

# Plot
plot_generator.plot_countries_and_cities(countries=countries, cities=cities, title="Cities and Countries (GeoPandas Spatial Join)")  # til slutt plotter den kart av land og byer