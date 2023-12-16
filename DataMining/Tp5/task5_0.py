import pandas as pd

# Load the CSV file into a pandas DataFrame
input_file = 'output/preprocessed.csv'
df = pd.read_csv(input_file)

# Split the DataFrame into two parts
df_40k = df.head(40000)
df_10k = df.tail(10000)

# Save the two DataFrames to separate CSV files
output_file_40k = 'output/training_data.csv'
output_file_10k = 'output/test_data.csv'

df_40k.to_csv(output_file_40k, index=False)
df_10k.to_csv(output_file_10k, index=False)
