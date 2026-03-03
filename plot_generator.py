import geopandas as gpd
import matplotlib.pyplot as plt


class PlotGenerator:


    def plot_countries_and_cities(self, countries: gpd.GeoDataFrame,
                                  cities: gpd.GeoDataFrame,
                                  title: str = "Cities and Countries") -> None:

        ax = countries.plot(color="lightgrey", edgecolor="black", figsize=(12, 7))

        cities.plot(ax=ax, color="red", markersize=5, alpha=0.7)

        ax.set_title(title)
        ax.set_axis_off()

        plt.show()