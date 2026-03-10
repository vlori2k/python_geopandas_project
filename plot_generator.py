import geopandas as gpd  # Importerer GeoPandas for å jobbe med geografiske datasett (GeoDataFrames)
import matplotlib.pyplot as plt  # Importerer matplotlib sitt plottingbibliotek for å vise figurer
from pydantic import BaseModel  # Importerer BaseModel fra Pydantic for å definere en strukturert modellklasse


class PlotGenerator(BaseModel):  # Definerer en Pydantic-modell som skal håndtere plotting av geodata

    def plot_countries_and_cities(self, countries: gpd.GeoDataFrame, cities: gpd.GeoDataFrame, title: str = "Cities and Countries") -> None:  # Metode som plottar land og byer på samme kart

        ax = countries.plot(color="lightgrey", edgecolor="black", figsize=(12, 7))  # Plotter landpolygoner først og lagrer aksen slik at flere lag kan tegnes på samme figur

        cities.plot(ax=ax, color="red", markersize=5, alpha=0.7)  # Plotter byene oppå landkartet ved å bruke samme akse (ax)

        ax.set_title(title)  # Setter tittelen på kartet ved hjelp av parameteren "title"

        ax.set_axis_off()  # Fjerner akseverdier og rutenett slik at kartet blir renere visuelt

        plt.show()  # Viser plottet i et vindu eller i notebook-output