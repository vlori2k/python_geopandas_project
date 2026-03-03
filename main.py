import geopandas as gpd
import matplotlib.pyplot as plt
from pathlib import Path

# -----------------------------
# Paths
# -----------------------------
DATA_DIR = Path("data")
OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)

COUNTRIES_PATH = DATA_DIR / "countries" / "ne_110m_admin_0_countries.shp"
CITIES_PATH = DATA_DIR / "cities" / "ne_110m_populated_places.shp"

# -----------------------------
# Load data
# -----------------------------
countries = gpd.read_file(COUNTRIES_PATH)
cities = gpd.read_file(CITIES_PATH)

print(f"Loaded {len(countries)} countries")
print(f"Loaded {len(cities)} cities")

# -----------------------------
# Spatial join
# -----------------------------
joined = gpd.sjoin(
    cities,
    countries,
    how="left",
    predicate="within"
)

print("Spatial join completed")
print(joined.head())

# -----------------------------
# Save to CSV
# -----------------------------
joined_csv = joined.copy()

# Convert geometry to WKT so it can be stored in CSV
joined_csv["geometry"] = joined_csv["geometry"].apply(
    lambda geom: geom.wkt if geom is not None else None
)

csv_path = OUTPUT_DIR / "cities_with_countries.csv"
joined_csv.to_csv(csv_path, index=False)

print(f"CSV saved to {csv_path}")

# -----------------------------
# Plot result
# -----------------------------
ax = countries.plot(
    color="lightgrey",
    edgecolor="black",
    figsize=(12, 7)
)

cities.plot(
    ax=ax,
    color="red",
    markersize=5,
    alpha=0.7
)

ax.set_title("Cities and Countries (GeoPandas Spatial Join)")
ax.set_axis_off()

plt.show()