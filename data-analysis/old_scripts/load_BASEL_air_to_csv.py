import tools

air_df = tools.Tools.load_BASEL_air_data_PM10("data/raw/BASEL_air/Luft_PM10-PM25-NO2_01012000.csv")
print("Data loaded successfully")

air_df.to_csv("data/processed/air_PM10_data_basel.csv", index=False, encoding="utf-8")
print("Data saved to CSV files")