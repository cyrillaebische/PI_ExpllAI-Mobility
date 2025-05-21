import pandas as pd
from tools import Tools 

# Initialize an empty list to collect results
correlation_results = []

# Example CSV files (replace with your actual file paths)
datasets = [
    ("data/processed/traffic_data_basel.csv", "data/processed/air_NO2_data_basel.csv", "data/processed/air_PM10_data_basel.csv")
]

for i, (csv1, csv2, csv3) in enumerate(datasets):
    correlation_matrix_pearson = Tools.correlation3(csv1, csv2, csv3, method='pearson')
    correlation_matrix_spearman = Tools.correlation3(csv1, csv2, csv3, method='spearman') 
    # Create a DataFrame with MultiIndex 
    correlation_df = pd.concat({'Pearson': correlation_matrix_pearson, 'Spearman': correlation_matrix_spearman}, axis=1)
    correlation_results.append(correlation_df)
    
# Convert list of Series into a DataFrame
df_results = pd.concat(correlation_results, axis=1)

print(df_results)  # View results
