import pandas as pd
import matplotlib
matplotlib.use('TkAgg') 
import matplotlib.pyplot as plt

df = pd.read_csv("data/raw/ASTRA_BESTAND/electrical_all.csv", encoding="latin1", sep=";")
year_columns = [col for col in df.columns if col.isdigit()]
df_electrical = df[year_columns].sum()

df = pd.read_csv("data/raw/ASTRA_BESTAND/all_all.csv", encoding="latin1", sep=";")
year_columns = [col for col in df.columns if col.isdigit()]
df_all = df[year_columns].sum()

# create new dataframe with the years as index and df_electrical and df_all as columns
df_total = pd.DataFrame({"electrical": df_electrical, "all": df_all})

# save to csv
df_total.to_csv("data/processed/vehicules_in_circulation.csv", index=True)

#plot the data with legend and labels
plt.plot(df_total.index, df_total["electrical"], label="Electrical")
plt.plot(df_total.index, df_total["all"], label="All")
plt.xlabel("Year")
plt.ylabel("Number of vehicles in Mio")
plt.title("Number of vehicles in circulation")
plt.legend()
plt.grid()
plt.show()