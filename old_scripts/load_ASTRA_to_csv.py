import tools
import pandas as pd

# Constant definitions
fribourg = '175'
aigle = '250'
camorino = '780'
basel = '081'


station_id = camorino
# Load data from 2018 to 2023
trafic_loader = tools.Tools("data/raw/ASTRA_Bulletins_2018-2023")
traffic_df = trafic_loader.load_traffic_data(station_id)
print("Data loaded successfully")
print(traffic_df.head())

# traffic_df = pd.DataFrame()

# append to this df the data from the folder "data/raw/ASTRA_Bulletins_pre_2018"
trafic_loader = tools.Tools("data/raw/ASTRA_Bulletins_pre_2018")
traffic_df_pre_2018 = trafic_loader.load_traffic_data_pre_2018(station_id)
traffic_df = pd.concat([traffic_df_pre_2018, traffic_df], ignore_index=True)

# Save DataFrames to CSV files
traffic_df.to_csv("data/processed/traffic_data_camorino.csv", index=False)
print("Data saved to CSV files")
