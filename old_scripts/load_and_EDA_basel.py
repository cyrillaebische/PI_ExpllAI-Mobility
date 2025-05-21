import tools
import pandas as pd
from ydata_profiling import ProfileReport

# Constant definitions
basel = '081'


station_id = basel
# Load trafic data from 2018 to 2023
trafic_loader = tools.Tools("data/raw/ASTRA_Bulletins_2018-2023")
traffic_df = trafic_loader.load_traffic_data(station_id)
# append to this df the data from the folder "data/raw/ASTRA_Bulletins_pre_2018"
trafic_loader = tools.Tools("data/raw/ASTRA_Bulletins_pre_2018")
traffic_df_pre_2018 = trafic_loader.load_traffic_data_pre_2018(station_id)
traffic_df = pd.concat([traffic_df_pre_2018, traffic_df], ignore_index=True)
print(traffic_df.head())
print("Trafic data loaded successfully")

# Load air data
air_df_pm10 = tools.Tools.load_BASEL_air_data_PM10("data/raw/BASEL_air/Luft_PM10-PM25-NO2_01012000.csv")
print("PM10 loaded successfully")
air_df_pm25 = tools.Tools.load_BASEL_air_data_PM25("data/raw/BASEL_air/Luft_PM10-PM25-NO2_01012000.csv")
print("PM25 loaded successfully")
air_df_NO2 = tools.Tools.load_BASEL_air_data_NO2("data/raw/BASEL_air/Luft_PM10-PM25-NO2_01012000.csv")
print("NO2 loaded successfully")

# add air_df as column to traffic_df
df = traffic_df.rename(columns={"Trafic": "Traffic", "Value (PM10 [µg/m³])": "MP10", "Value (PM2.5 [µg/m³])": "MP25", "Value (NO2 [µg/m³])": "NO2"})  # fix name first
df = pd.merge(df, air_df_pm10, on="Date", how="left")
df = pd.merge(df, air_df_pm25, on="Date", how="left")
df = pd.merge(df, air_df_NO2, on="Date", how="left")


print(df.head())
print("Data merged successfully")

# EDA
profile = ProfileReport(df, title="basel_EDA_Report", 
                        explorative=True, 
                        correlations={"spearman": {"calculate": True},
                                      "pearson": {"calculate": True}}
                                      )
profile.to_file("basel_EDA_Report")
print("EDA report generated: basel_EDA_Report")





