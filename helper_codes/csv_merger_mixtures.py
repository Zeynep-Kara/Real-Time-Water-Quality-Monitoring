import pandas as pd
import os

# Define the directory containing the CSV files
path = 'experiment_logs_UPDT/'

# Define the file names
file_names = [f'experiment_{i}.csv' for i in range(1, 8)]

# List to hold DataFrames
dfs = []

# Read and append each CSV file to the list
for file_name in file_names:
    file_path = path + file_name
    df = pd.read_csv(file_path)
    dfs.append(df)

# Concatenate all DataFrames
merged_df = pd.concat(dfs, ignore_index=True)

# Save the merged DataFrame to a new CSV file
output_file = os.path.join(path, 'merged_experiments.csv')
merged_df.to_csv(output_file, index=False)

