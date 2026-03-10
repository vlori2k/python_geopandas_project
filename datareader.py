from pathlib import Path  # Importerer Path-klassen fra pathlib for å håndtere fil- og mappestier på en plattformuavhengig måte
import geopandas as gpd  # Importerer GeoPandas og gir det aliaset gpd, brukes til å lese og håndtere geodata
from pydantic import BaseModel, ConfigDict  # Importerer Pydantic-klasser for å definere og konfigurere datamodeller



class DataReader(BaseModel):  # Definerer en Pydantic-modell som skal brukes til å lese geografiske datafiler
    data_dir: Path  # Definerer en attributt som representerer katalogen der datafilene ligger

    model_config = ConfigDict(arbitrary_types_allowed=True)  # Tillater bruk av typer som Path i Pydantic-modellen

    def read_countries(self) -> gpd.GeoDataFrame:  # Metode som leser shapefile med land
        path = self.data_dir / "countries" / "ne_110m_admin_0_countries.shp"  # Lager filstien til shapefilen for land
        return gpd.read_file(path)  # Leser shapefilen og returnerer den som en GeoDataFrame



    def read_cities(self) -> gpd.GeoDataFrame:  # Metode som leser shapefile med byer
        path = self.data_dir / "cities" / "ne_110m_populated_places.shp"  # Lager filstien til shapefilen for byer
        return gpd.read_file(path)  # Leser shapefilen og returnerer den som en GeoDataFrame
