import pandas as pd

# Constants (replace these values with actual constants as needed)
top_ml = 30  # starting value in ml (example value)
top_ppm_nacl = 50000  # top ppm value
top_ppm_mgso = 15000  # top ppm value
bottom_ppm_nacl = 0
bottom_ppm_mgso = 15000
bottom_ml = 70  # starting value in ml (example value)

# Load the CSV file into a DataFrame
file_name = 'experiment_4'
path_name = "experiment_logs/"
input_file = path_name = path_name + f'{file_name}.csv'  
df = pd.read_csv(input_file)

iterations = df['Iteration'].max()+30
# Calculate V
V = top_ml / iterations #ppm change speed

# Calculate ppm values using the provided formula
df['NaCl_ppm'] = df['Iteration'].apply(lambda i: ((bottom_ml * bottom_ppm_nacl) + (top_ppm_nacl * (min(i+30,iterations) * V))) / (bottom_ml + (min(i+30,iterations) * V)))
df['MgSO4_ppm'] = df['Iteration'].apply(lambda i: ((bottom_ml * bottom_ppm_mgso) + (top_ppm_mgso * (min(i+30,iterations) * V))) / (bottom_ml + (min(i+30,iterations) * V)))

# Save the updated DataFrame back to a new CSV file
path_name_UPD = "experiment_logs_UPDT/"
output_file = path_name_UPD + f'{file_name}.csv'    
df.to_csv(output_file, index=False)

print(f'Updated CSV file saved as {output_file}')
