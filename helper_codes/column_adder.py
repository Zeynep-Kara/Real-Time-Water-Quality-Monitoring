
## column adder ##
import pandas as pd

# Read the CSV file into a DataFrame

path = "experiment_logs/"

ppm = 10000
file = path + f'{ppm}_ppm_MgSO4.csv'
#file = path + f'{ppm}_ppm_NaCl.csv'
#file= 'pure_water.csv'
df = pd.read_csv(file)

# Add a new column named 'new_column' with all values set to 1
#df['ppm'] = ppm
df['Type'] = 'MgSO4'

# Write the DataFrame back to the CSV file
df.to_csv(file, index=False)  # This will create or overwrite 'updated_dataset.csv' with the updated DataFrame


