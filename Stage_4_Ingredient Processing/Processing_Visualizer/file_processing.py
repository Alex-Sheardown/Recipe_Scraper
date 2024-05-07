import json
import pandas as pd
from collections import Counter

import sys
sys.path.insert(1, 'G:\Code\Recipe Project\Stage_3_Database and Cleaning\Table_Organizer\Ingredient_processing')  # Replace '/path/to/directory' with the actual directory path

from  process_ingredient import raw_translated_ingredient


def word_counter_in_json(json_file, list_key):
    # Initialize an empty Counter object to store word counts
    word_counter = Counter()
    first_occurrence_ids = {}
    processing_comparison_df = pd.DataFrame(columns=['Original_Word', 'Processed_Word'])
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
                    item_break_down = raw_translated_ingredient(item, False)
                    if len(item_break_down) > 0 :
                        fmo, fme, text, mod_hash, name, portion, mpis, ignore_this = item_break_down[0]
                        
                        processing_comparison_df.loc[len(processing_comparison_df)]  = {'Original_Word': item, 'Processed_Word': text}
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
            if count > 1:
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