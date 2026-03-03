from pathlib import Path
import geopandas as gpd




class CSVGenerator:
    def __init__(self, output_dir: Path):
        self.output_dir = output_dir
        self.output_dir.mkdir(exist_ok=True)


    def save(self, gdf: gpd.GeoDataFrame, filename: str) -> None:
        df = gdf.copy()

        # Convert geometry to WKT for CSV compatibility
        df["geometry"] = df["geometry"].apply(lambda geom: geom.wkt if geom is not None else None)

        output_path = self.output_dir / filename
        df.to_csv(output_path, index=False)

        print(f"CSV saved to {output_path}")