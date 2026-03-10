from pathlib import Path  # Importerer Path-klassen fra pathlib for å jobbe med fil- og mappestier på en plattformuavhengig måte

import geopandas as gpd  # Importerer GeoPandas og gir det aliaset gpd, brukes til å håndtere geodata (GeoDataFrame)
from pydantic import BaseModel, ConfigDict, field_validator  # Importerer Pydantic-klasser for datavalidering og modellstruktur



class CSVGenerator(BaseModel):  # Definerer en Pydantic-modell som skal brukes til å generere CSV-filer

    output_dir: Path  # Definerer en attributt som representerer katalogen der CSV-filer skal lagres

    model_config = ConfigDict(arbitrary_types_allowed=True)  # Tillater bruk av egendefinerte typer som Path i Pydantic-modellen

    @field_validator("output_dir")  # Angir at metoden under skal validere feltet "output_dir"
    @classmethod  # Gjør metoden til en klassemetode slik at den kan brukes av Pydantic under validering
    def create_output_dir(cls, v: Path) -> Path:  # Valideringsmetode som mottar output_dir-verdien
        v.mkdir(parents=True, exist_ok=True)  # Oppretter katalogen hvis den ikke finnes, inkludert eventuelle foreldremapper
        return v  # Returnerer den validerte og eventuelt opprettede katalogstien


    def save_to_CSV(self, gdf: gpd.GeoDataFrame, filename: str) -> None:  # Metode som lagrer en GeoDataFrame til en CSV-fil
        df = gdf.copy()  # Lager en kopi av GeoDataFrame for å unngå å endre originaldata

        # Convert geometry to WKT for CSV compatibility  # Kommentar: Konverterer geometri til WKT-format slik at det kan lagres i CSV
        df["geometry"] = df["geometry"].apply(  # Bruker apply på geometry-kolonnen for å transformere hver geometri
            lambda geom: geom.wkt if geom is not None else None
            # Konverterer geometri til WKT-streng hvis den finnes, ellers None
        )

        output_path = self.output_dir / filename  # Lager full filsti ved å kombinere output_dir og filnavnet
        df.to_csv(output_path, index=False)  # Skriver DataFrame til CSV-fil uten å inkludere indekskolonnen

        print(f"CSV saved to {output_path}")  # Skriver ut melding i konsollen som viser hvor CSV-filen ble lagret