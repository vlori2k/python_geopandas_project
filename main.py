import geopandas as gpd

countries = gpd.read_file("data/countries/ne_110m_admin_0_countries.shp")
cities = gpd.read_file("data/cities/ne_110m_populated_places.shp")

joined = gpd.sjoin(cities, countries, how="left", predicate="within")
print(joined.head())