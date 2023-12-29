import re
import pandas as pd
"""
# File path
file_path = 'your_file.csv'

# Sample data
data = {'ID': []}

# Create or read the DataFrame from the file
try:
    df = pd.read_csv(file_path)
except FileNotFoundError:
    df = pd.DataFrame(data)

# Function to update the DataFrame
def update_dataframe(dataframe, id_value, columns_to_mark_true):
    # Check if the ID already exists in the DataFrame
    if id_value in dataframe['ID'].values:
        print(f"ID {id_value} already exists. Skipping update.")
        return dataframe

    for possible_new_column in columns_to_mark_true:
        if possible_new_column not in dataframe.columns:
            dataframe[possible_new_column] = False

    # Add a new row with the given ID
    new_row = {'ID': id_value}
    for col in dataframe.columns[1:]:  # Exclude 'ID' column
        new_row[col] = col in columns_to_mark_true

    dataframe = dataframe._append(new_row, ignore_index=True)

    return dataframe

# Example usage
id_value_to_update = 12
columns_to_update = ['Column_A', 'Column_C', 'New_Column']

# Update the DataFrame
df = update_dataframe(df, id_value_to_update, columns_to_update)

# Save the updated DataFrame to the file
df.to_csv(file_path, index=False)

# Display the updated DataFrame
print(df)
"""

def process_measurement(input_text):
    # Use regex to separate numbers and 'g' and replace 'g' with 'grams'
    result = re.sub(r'(\d+)\s*(g|G)', r'\1 grams', input_text, flags=re.IGNORECASE)
    return result

input_text = '250g of sugar and 2G of salt'

processed_text = process_measurement(input_text)
print(processed_text)