import pandas as pd
import argparse
import os
from ydata_profiling import ProfileReport
parser = argparse.ArgumentParser(description="Generate EDA report for a CSV file.")
parser.add_argument("file_path", type=str, help="Path to the input CSV file.")
parser.add_argument("-o", "--output", help="Path to the output HTML file.")

args = parser.parse_args()
filename = os.path.splitext(os.path.basename(args.file_path))[0]
output_filename = args.output if args.output else f"{filename}_report.html"
df = pd.read_csv(args.file_path, na_values="?")
profile = ProfileReport(df, title=f"{filename}_EDA_Report", explorative=True)
profile.to_file(output_filename)
print(f"EDA report generated: {output_filename}")