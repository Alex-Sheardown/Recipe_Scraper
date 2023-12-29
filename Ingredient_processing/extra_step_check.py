import pandas as pd

# Sample DataFrame
data = {'ID': [1, 2, 3],
        'Name': ['John', 'Jane', 'Bob'],
        'City': ['New York', 'San Francisco', 'Los Angeles']}

df = pd.DataFrame(data)

def add_row_if_unique(dataframe, new_data, unique_columns):
    # Create a DataFrame with the new row
    new_df = pd.DataFrame([new_data])

    # Check if the combination of unique_columns in the new data is unique
    is_unique = ~new_df.set_index(unique_columns).index.isin(dataframe.set_index(unique_columns).index)

    # Check if all rows are unique for the specified columns
    if is_unique.all():
        # Append the new row to the DataFrame
        dataframe = dataframe._append(new_df, ignore_index=True)
        print("Row added successfully.")
    else:
        print("Duplicate found in the specified columns. Row not added.")

    return dataframe

# Example usage
new_row = {'ID': 45, 'Name': 'Alice', 'City': 'San Francisco'}

# Specify the columns to check for uniqueness
unique_columns_to_check = ['ID', 'City']

df = add_row_if_unique(df, new_row, unique_columns_to_check)

# Display the updated DataFrame
print(df)
