import tools

# air_loader = correlation.AirDataLoader("data/raw/FR_air")  
air_df = tools.Tools.load_FR_air_data("data/raw/FR_air/O3")
print("Data loaded successfully")

air_df.to_csv("data/processed/air_O3_data_fribourg.csv", index=False)
print("Data saved to CSV files")