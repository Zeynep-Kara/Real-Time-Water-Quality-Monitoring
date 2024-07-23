import pandas as pd

# Load the CSV file into a DataFrame
input_file = 'experiment_results_with_ppm.csv'  # replace with your actual file name
df = pd.read_csv(input_file)

# Get the minimum and maximum ppm values
min_ppm = df['ppm'].min()
max_ppm = df['ppm'].max()

# Define class boundaries and labels
class_labels = ["very low salt", "low salt", "medium salt", "high salt", "very high salt"]
bins = [min_ppm, min_ppm + (max_ppm - min_ppm) * 0.2, min_ppm + (max_ppm - min_ppm) * 0.4,
        min_ppm + (max_ppm - min_ppm) * 0.6, min_ppm + (max_ppm - min_ppm) * 0.8, max_ppm + 1]  # Adjusted last bin

# Classify the existing ppm values into the defined classes
df['class'] = pd.cut(df['ppm'], bins=bins, labels=class_labels, right=False)

# Save the updated DataFrame back to a new CSV file
output_file = 'experiment_results_with_class.csv'  # replace with your desired output file name
df.to_csv(output_file, index=False)

print(f'Updated CSV file saved as {output_file}')
