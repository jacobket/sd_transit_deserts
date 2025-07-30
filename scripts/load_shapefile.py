import geopandas

shapefile_path = "data/raw/tl_2023_06_tract/tl_2023_06_tract.shp"
gdf = geopandas.read_file(shapefile_path)

