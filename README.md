Python GeoPandas Project

This project demonstrates a clean and modular Python workflow for working with geospatial data using GeoPandas.
It focuses on typical GIS tasks such as reading geospatial datasets, performing spatial joins, exporting results for downstream use, and visualizing data for validation.

The project is intentionally kept small and focused, with an emphasis on readability, structure, and production-friendly design.

Features

Read geospatial data from shapefiles using GeoPandas

Perform a spatial join between point and polygon datasets

Export joined geospatial data to CSV with geometry stored as WKT

Visualize results using Matplotlib

Modular, object-oriented code structure with clear separation of responsibilities

Project Structure
python_geopandas_project/
├── data/                 # Input geospatial datasets (shapefiles)
├── output/               # Generated output files
├── datareader.py         # Responsible for reading geospatial data
├── csv_generator.py      # Responsible for exporting data to CSV
├── plot_generator.py     # Responsible for visualization
├── main.py               # Orchestrates the workflow
└── README.md
Workflow Overview

Geospatial datasets are loaded from disk using the DataReader class

A spatial join is performed to associate point features with polygon features based on spatial relationships

The resulting dataset is exported to CSV using the CSVGenerator, with geometry converted to WKT

A simple map visualization is generated using the PlotGenerator for quality control

Technologies Used

Python 3

GeoPandas

Shapely

Matplotlib