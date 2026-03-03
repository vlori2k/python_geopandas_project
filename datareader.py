import geopandas as gpd
from pathlib import Path




class DataReader:
    def __init__(self, data_dir: Path):

        self.data_dir = data_dir

        print("hva er denne?", self.data_dir)


    def read_countries(self) -> gpd.GeoDataFrame:
        path = self.data_dir / "countries" / "ne_110m_admin_0_countries.shp"

        return gpd.read_file(path)


    def read_cities(self) -> gpd.GeoDataFrame:
        path = self.data_dir / "cities" / "ne_110m_populated_places.shp"

        return gpd.read_file(path)
