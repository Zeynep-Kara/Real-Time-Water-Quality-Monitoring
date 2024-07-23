import os
import pandas as pd

# Define the folder paths
folders = ['nacl', 'water', 'mgso4']

# Initialize an empty list to store DataFrames
dfs = []

# Iterate over each folder
for folder in folders:
    # List all CSV files in the folder
    files = [f for f in os.listdir(folder) if f.endswith('.csv')]
    
    # Read each CSV file into a DataFrame and append to the list
    for file in files:
        file_path = os.path.join(folder, file)
        df = pd.read_csv(file_path)
        dfs.append(df)

# Concatenate all DataFrames into one
merged_df = pd.concat(dfs, ignore_index=True)

# Write the merged DataFrame to a new CSV file
merged_df.to_csv('merged_dataset.csv', index=False)

