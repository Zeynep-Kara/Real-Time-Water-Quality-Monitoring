import pandas as pd

# Load the CSV file
input_csv_file = 'experiment_logs_UPDT/merged_experiments.csv'
output_csv_file = 'experiment_logs_UPDT/merged_experiments_fixed_iter.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(input_csv_file)

# Add an 'Iteration' column with line numbers (starting from 1)
df['Iteration'] = (df.index // 201)

# Save the modified DataFrame to a new CSV file
df.to_csv(output_csv_file, index=False)

print(f"The file has been saved as {output_csv_file} with an 'Iteration' column.")
