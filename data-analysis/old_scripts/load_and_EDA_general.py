import tools
import pandas as pd
from ydata_profiling import ProfileReport

# Constant definitions
fribourg = '175'
basel = '081'
aigle = '250'
camorino = '780'
payerne = '222'
lugano = '507'

# --------------------------------------#
station_id = payerne
# --------------------------------------#


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
if station_id == fribourg:
    air_df_pm10 = tools.Tools.load_FR_air_data("data/raw/FR_air/PM10")
    air_df_pm10 = air_df_pm10.rename(columns={"Value": "PM10"})
    print("PM10 Data loaded successfully")
    air_df_NO2 = tools.Tools.load_FR_air_data("data/raw/FR_air/NO2")
    air_df_NO2 = air_df_NO2.rename(columns={"Value": "NO2"})
    print("NO2 Data loaded successfully")
    air_df_O3 = tools.Tools.load_FR_air_data("data/raw/FR_air/O3")
    air_df_O3 = air_df_O3.rename(columns={"Value": "O3"})
    print("O3 Data loaded successfully")
    
    df = traffic_df.rename(columns={"Trafic": "Traffic"})  # fix name first
    df = pd.merge(df, air_df_pm10, on="Date", how="left")
    df = pd.merge(df, air_df_NO2, on="Date", how="left")
    df = pd.merge(df, air_df_O3, on="Date", how="left")


elif station_id == basel:
    air_df_pm10 = tools.Tools.load_BASEL_air_data_PM10("data/raw/BASEL_air/Luft_PM10-PM25-NO2_01012000.csv")
    print("PM10 loaded successfully")
    air_df_pm25 = tools.Tools.load_BASEL_air_data_PM25("data/raw/BASEL_air/Luft_PM10-PM25-NO2_01012000.csv")
    print("PM25 loaded successfully")
    air_df_NO2 = tools.Tools.load_BASEL_air_data_NO2("data/raw/BASEL_air/Luft_PM10-PM25-NO2_01012000.csv")
    print("NO2 loaded successfully")
    traffic_df = traffic_df.rename(columns={"Value (PM10 [µg/m³])": "MP10", "Value (PM2.5 [µg/m³])": "MP25", "Value (NO2 [µg/m³])": "NO2"})  # fix name first
    
    df = traffic_df.rename(columns={"Trafic": "Traffic"})  # fix name first
    df = pd.merge(df, air_df_pm10, on="Date", how="left")
    df = pd.merge(df, air_df_pm25, on="Date", how="left")
    df = pd.merge(df, air_df_NO2, on="Date", how="left")

elif station_id == aigle:
    air_df_pm10 = tools.Tools.load_AIGLE_air_data("data/raw/AIGLE_air/PM10")
    air_df_pm10 = air_df_pm10.rename(columns={"Value": "PM10"})
    print("PM10 Data loaded successfully")
    air_df_NO2 = tools.Tools.load_AIGLE_air_data("data/raw/AIGLE_air/NO2")
    air_df_NO2 = air_df_NO2.rename(columns={"Value": "NO2"})
    print("NO2 Data loaded successfully")
    air_df_O3 = tools.Tools.load_AIGLE_air_data("data/raw/AIGLE_air/O3")
    air_df_O3 = air_df_O3.rename(columns={"Value": "O3"})
    print("O3 Data loaded successfully")
    
    df = traffic_df.rename(columns={"Trafic": "Traffic"})  # fix name first
    df = pd.merge(df, air_df_pm10, on="Date", how="left")
    df = pd.merge(df, air_df_NO2, on="Date", how="left")
    df = pd.merge(df, air_df_O3, on="Date", how="left")

elif station_id == payerne:
    air_df_CO = pd.read_csv('data/raw/ID38_CO.csv', delimiter=';', skiprows=6, names=["Date", "Lausanne", "Lugano", "Payerne"], parse_dates=["Date"])
    air_df_CO['Date'] = pd.to_datetime(air_df_CO['Date'], dayfirst=True, errors='coerce')  # handle odd formats
    air_df_CO = air_df_CO.drop(columns=["Lausanne", "Lugano"])  # drop Lausanne and Lugano columns
    air_df_CO = air_df_CO.rename(columns={"Payerne": "CO"})

    df = traffic_df.rename(columns={"Trafic": "Traffic"})  # fix name first
    df = pd.merge(df, air_df_CO, on="Date", how="left")
    
elif station_id == lugano:
    air_df_CO = pd.read_csv('data/raw/ID38_CO.csv', delimiter=';', skiprows=6, names=["Date", "Lausanne", "Lugano", "Payerne"], parse_dates=["Date"])
    air_df_CO['Date'] = pd.to_datetime(air_df_CO['Date'], dayfirst=True, errors='coerce')  # handle odd formats
    air_df_CO = air_df_CO.drop(columns=["Lausanne", "Payerne"])  # drop Lausanne and Lugano columns
    air_df_CO = air_df_CO.rename(columns={"Lugano": "CO"})

    df = traffic_df.rename(columns={"Trafic": "Traffic"})  # fix name first
    df = pd.merge(df, air_df_CO, on="Date", how="left")
    

print(df.head())
print("Data merged successfully")

# EDA
profile = ProfileReport(df, title=f"{station_id}_EDA_Report", 
                        explorative=True, 
                        correlations={"spearman": {"calculate": True},
                                      "pearson": {"calculate": True}})
profile.to_file(f"{station_id}_EDA_Report")
print(f"EDA report generated: {station_id}_EDA_Report")





