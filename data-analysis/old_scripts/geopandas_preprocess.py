import geopandas as gpd

# Shapefile laden
gdf = gpd.read_file("data\ID14_SHP_OTC_COMPTAGE_TRAFIC\OTC_COMPTAGE_TRAFIC.shp")



# clean
gdf_clean = gdf[(gdf['TJOM_ANNEE'] != 0) & gdf['TJOM'].notnull()]
# Die ersten 5 Zeilen anzeigen
print(gdf_clean.head())
# Ältestes und neuestes Datum finden 
oldest_date = gdf_clean['TJOM_ANNEE'].min()
newest_date = gdf_clean['TJOM_ANNEE'].max()

print("Ältestes Datum: ", oldest_date)
print("Neuestes Datum: ", newest_date)