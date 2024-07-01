import json
import re
import pandas as pd
from collections import Counter

import sys
sys.path.insert(1, 'G:\Code\Recipe Project\Stage_3_Database and Cleaning\Table_Organizer\Ingredient_processing')  # Replace '/path/to/directory' with the actual directory path

from  process_ingredient import raw_translated_ingredient
from step_4_measurements import check_portion

# Convert list to string format
def list_to_string(lst):
    return ', '.join(lst)

def word_counter_in_json(json_file, list_key):
    # Initialize an empty Counter object to store word counts
    word_counter = Counter()
    first_occurrence_ids = {}
    processing_comparison_df = pd.DataFrame(columns=['status', 'Original_Word', 'Processed_Word', "modifiers", "measurements"])
    # Open the JSON file and process each line (each line is a JSON object)
    count = 0
    with open(json_file, 'r') as f:
        for line in f:
            # Load the JSON object from the line
            data = json.loads(line)

            # Check if the specified key exists in the JSON data
            if list_key in data and isinstance(data[list_key], list):
                # Iterate through each item in the list
                for item in data[list_key]:
                    # Check if the item is a string
                    item_break_down_current = raw_translated_ingredient(item, False, False)
                    item_break_down_new = raw_translated_ingredient(item, False, True)
                    if len(item_break_down_current) > 0 :
                        fmo, fme, text, mod_hash, name, portion, mpis, ignore_this = item_break_down_current[0]
                        list_of_Ingredients = [t[0] for t in fme]
                        """
                        print("modifiers:", fmo,", measurements:", fme)
                        print(list_of_Ingredients)
                        print(list_to_string(list_of_Ingredients))
                        """
                        
                        processing_comparison_df.loc[len(processing_comparison_df)]  = {'status':"0", 'Original_Word': item, 'Processed_Word': text, "modifiers": list_to_string(fmo), "measurements": str(list_to_string(list_of_Ingredients))}
                        
                        fmo, fme, text, mod_hash, name, portion, mpis, ignore_this = item_break_down_new[0]
                        list_of_Ingredients = [t[0] for t in fme]
                        processing_comparison_df.loc[len(processing_comparison_df)]  = {'status': "1", 'Original_Word': item, 'Processed_Word': text, "modifiers": list_to_string(fmo), "measurements": str(list_to_string(list_of_Ingredients))}
                        
                        item = text
                        #print(item)
                    else:
                        item = "ignore"
                    #print(text)
                    if isinstance(item, str):
                        # Split the string into words (splitting on "_") and update the word counter
                        words = item.split()
                        word_counter.update(words)
                        
                        # Keep track of the ID of the first occurrence of each word
                        """
                        for word in words:
                            if word not in first_occurrence_ids:
                                first_occurrence_ids[word] = data['id']
                        """
            count = count + 1
            if count > 2:
                break

    # Convert the Counter object to a DataFrame
    df = pd.DataFrame.from_dict(word_counter, orient='index', columns=['Count'])
    df.index.name = 'Word'
    df.reset_index(inplace=True)
    """
    # Add the ID of the first occurrence to the DataFrame
    df['First_Occurrence_ID'] = df['Word'].map(first_occurrence_ids)
    """
    # Sort the DataFrame based on word count in descending order
    df = df.sort_values(by='Count', ascending=False)
    df = reversed_df = df[df.columns[::-1]]
    return df, processing_comparison_df

def filter_word(word_df, filter_word):
    # Filter the DataFrame based on whether the original word contains the filter word
    filtered_df = word_df[word_df['Original_Word'].str.contains(filter_word)].copy()

    return filtered_df

def filter_patterns_based_on_strings(df_patterns, df_strings, pattern_column, string_column):
    # Extract regex patterns from df_patterns
    patterns = df_patterns[pattern_column].tolist()
    
    # Initialize a list to hold the indices of matching patterns
    matching_indices = []

    # Create a copy of df_strings to work on
    df_strings_copy = df_strings.copy()
    
    # Iterate over each pattern
    for index, pattern in enumerate(patterns):
        # Check if the pattern matches any string in df_strings_copy
        for i, string in df_strings_copy[string_column].items():
            if re.search(pattern, string):
                # Update the string with the applied pattern
                updated_string = re.sub(pattern, '', string)
                df_strings_copy.at[i, string_column] = updated_string
                matching_indices.append(index)
    
    # Remove duplicates from matching_indices while preserving order
    matching_indices = list(dict.fromkeys(matching_indices))
    
    # Filter df_patterns based on matching indices
    filtered_df = df_patterns.loc[matching_indices]
    
    return filtered_df

def filter_individual_names(names_df, processing_df, name_column, processing_column):

    # Collect all unique modifiers from the processing_comparison_df
    all_modifiers = set()
    for modifiers in processing_df[processing_column]:
        for modifier in modifiers.split(', '):
            all_modifiers.add(modifier)
    
    # Filter the individual names DataFrame based on the collected modifiers
    filtered_df = names_df[names_df[name_column].isin(all_modifiers)]
    return filtered_df

def apply_regex_patterns(value, patterns):
    """
    Apply a list of regex patterns to a value and return the altered version if there is a match.
    
    Args:
        value (str): The input string to be altered.
        patterns (list): A list of regex patterns (either single patterns or lists of patterns).
    
    Returns:
        str: The altered version of the input string.
    """
    original_value = value
    
    if isinstance(patterns, list):
        print("5a list ")
        for sub_pattern in patterns:
            print("5a sub pattern", sub_pattern)
            print("5a sub value  ", original_value)
            has_pattern, value, proportion = check_portion(sub_pattern, original_value)
    else:
        print("5a not list ")
        has_pattern, value, proportion = check_portion(patterns, original_value)
    
    # Check if the value was altered
    if value != original_value:
        return value
    else:
        return None
