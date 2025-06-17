import pandas as pd
import glob
import matplotlib.pyplot as plt

def load_air_data(folder_path):
    dir_path = "data/FR_air"
    csv_files = glob.glob(dir_path + "/*.csv")

    air_df = pd.DataFrame()
    for file in csv_files:
        df = pd.read_csv(file, delimiter=';', skiprows=5, names=["Date", "Value"], parse_dates=["Date"])
        df['Date'] = pd.to_datetime(df['Date'])
        air_df = pd.concat([air_df, df], ignore_index=True)
    
    print(air_df.head())
# Plot onl from 2018 to 2023
air_df_short = air_df[(air_df['Date'] >= '2018-01-01') & (air_df['Date'] <= '2023-12-31')]
air_df_short.set_index('Date', inplace=True)
air_df_short.plot()
plt.xlabel('Date')
plt.ylabel('Valuer journalières')
plt.title('Poussières  en  suspension  (PM10) microgrammes  par  m3 ')