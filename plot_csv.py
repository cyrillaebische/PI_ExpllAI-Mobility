import pandas as pd
import matplotlib
matplotlib.use("TkAgg")  # or "Qt5Agg" if you have PyQt installed
import matplotlib.pyplot as plt
import argparse
from sklearn.preprocessing import StandardScaler

# Set up argument parsing
parser = argparse.ArgumentParser(description="Plot traffic count from a CSV file.")
parser.add_argument("csv_file", type=str, nargs='+', help="Paths to the CSV file")

# Parse arguments
args = parser.parse_args()
csv_file = args.csv_file  # Get file path from command line

# Plot the data
plt.figure(figsize=(10, 5))

for i, csv_file in enumerate(csv_file):
    df = pd.read_csv(csv_file, parse_dates=["Date"])
    df = df.sort_values(by="Date")
    
    # Normalize the data
    scaler = StandardScaler()
    df.iloc[:,1:] = scaler.fit_transform(df.iloc[:,1:])
    plt.plot(df["Date"], df.iloc[:,1], linewidth=1, label=f"Dataset {i+1} - {csv_file.split('/')[-1]}")

# Formatting the plot
plt.xlabel("Date")
plt.ylabel("Values to plot")
plt.title("Timeseries plot")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

# Show the plot
plt.show()
