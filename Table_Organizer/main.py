"""
Cleaning up files needs to be automated and simple.
I should be able to add to it without much effort.
perhaps a text file with the added info

Also a conversion method would be good standard with conversion 

"""
import os
import time
import pandas as pd
from recipe_scrapers import scrape_me
import numpy as np
import Linkchecker
"""
Now that the folder is readable at least on the last folder.   
"""
def move_through_folder(floder_location):
    res = []

    # Iterate directory
    for file_path in os.listdir(floder_location):
        # check if current file_path is a file
        if os.path.isfile(os.path.join(floder_location, file_path)):
            # add filename to list
            res.append(file_path)
    print(res)

"""
Alright my next move is to read all the columns and create a list of differences.
"""

def print_column_data_from_file(file_location):
    df = pd.read_table(file_location)
    columns_in_file = df.columns
    #print(df.columns)



    """
    Alright now I need to do a check for ['N_S' '0']
    With this discrepancy we can figure out which one have a simple number system
    This allows and interesting change we can make of a new column of never specified. 
    """


    print(df['_¼_chives_or_quater_flatleaf_parsley'].unique())



def collect_column_data_for_file(directory_path, phantom_status_df):

    log_need = False
    if not os.path.exists("log") and log_need:
        # if the demo_folder directory is not present 
        # then create it.
        os.makedirs("log")
        # Create a document to log changes
        changes_log = open("log/changes_log" + str(time.time()) +".txt", "w" , encoding="utf-8")

    # Iterate through each TSV file in the directory
    data = []

    for filename in os.listdir(directory_path):
        if filename.endswith(".tsv") and filename != 'column_overview.tsv':
            file_path = os.path.join(directory_path, filename)
            
            # Read the TSV file into a pandas DataFrame
           
            
            df = pd.read_csv(file_path, sep="\t")
           
            # Merge the ingredient DataFrame with the phantom status DataFrame based on the recipe id
            merged_df = df.merge(phantom_status_df, on='id', how='left')
            # Filter out rows associated with phantom recipes (where 'phantom' is True)
            non_phantom_ingredients = merged_df[merged_df['phantom'] == False].drop(columns=['phantom'])

            # Iterate through each column and count unique values
            for column in df.columns:
                

                


                if column != "id":
                    if log_need :
                        changes_log.write(f"File: {filename}, Column: {column}, Unique Values Count: {unique_values_count}, Column_values: {unique_values}\n")

                    unique_values_count = non_phantom_ingredients[column].nunique()
                    unique_values = non_phantom_ingredients[column].unique()
                    values_count = (non_phantom_ingredients[column] != 0).sum()


                    first_non_zero_id = Linkchecker.get_first_non_zero_id(non_phantom_ingredients, column)
                    print(first_non_zero_id)
                    status = 2222
                    
                    replacement = "N_S"
                    final_column_name = column

                    fraction_detected = False
                    inapropriate_row_values = False
                    row_holding_ingredients = False
                    column_name_check_possible_issue = False
                    more_complicated_need_dedicated_folder = False


                    is_present = np.isin('0', unique_values)
                    dead_column = False

                    if unique_values_count == 1 and is_present:
                        dead_column = True


                    #This check for seeing if the column is holding a fraction in its values that went un checked
                    if unique_values_count == 2 and np.isin('0', unique_values) and np.isin('N_S', unique_values):
                        
                        clean_column = Linkchecker.clean_ingredient(column)
                        if clean_column != column:
                            fraction_detected = True

                        
                        clean_column = Linkchecker.remove_prefix_underscores(clean_column)
                        first_part, number, second_part = Linkchecker.split_string_and_number(clean_column)

                        status = Linkchecker.seperate_to_ingredient_proportion(first_part, number, second_part)
                        
                          
                        
                        if status == "011":
                            final_column_name = second_part
                            replacement = number
                        else:
                            more_complicated_need_dedicated_folder = True
                    

                    data.append({
                        "file": filename,
                        "column": column,
                        "final_column_name": final_column_name,

                        "values_count": values_count,
                        "unique_values_count": unique_values_count,
                        "column_values": unique_values,
                        
                        "more_complicated_need_dedicated_folder": more_complicated_need_dedicated_folder ,
                        "N_S_Replace":  replacement,

                        "Status": status,
                        "measurement": "hold",
                        "dead_column": dead_column,
                        "first_non_zero_id": first_non_zero_id, 
                        "Fraction_detected": fraction_detected

                    })
    # Close the changes log file
    if log_need :
        changes_log.close()
    result_df = pd.DataFrame(data)
    result_df.to_csv(directory_path + 'column_overview.tsv', sep="\t",index=False)
    return result_df


def phantom_recipe_check(folder):
    # Open the TSV file for reading
    log_needed = False
    folder_overview = folder + "Overview\\overview.tsv"
    # Read the TSV file into a dataframe
    df = pd.read_csv(folder_overview, sep='\t')
    # Create a new column 'Phantom' based on whether the keyword is in the Link column
    new_df = df[['id']].copy()  # Create a new DataFrame with the 'ID' column

    #750g web
    keyword = 'recettes'  # Keyword to check in link column
    website = '750g.com'  # Website to check in host column

    

    new_df['phantom'] = (df['link'].str.contains(keyword, case=False)) & (df['host'].str.contains(website, case=False))
    #new_df['phantom'] = (df['link'].str.contains(keyword, case=False)) |  (df['host'].str.contains(website, case=False)) 
    new_df.to_csv(folder + "\\Overview\\" +'phantom_status.tsv', sep='\t', index=False)
    # Display the resulting DataFrame
    #print(new_df)

    if log_needed == True:
        if not os.path.exists("log_Phantom_recipe_check"):
            # if the demo_folder directory is not present 
            # then create it.
            os.makedirs("log_Phantom_recipe_check")
        # Create a document to log changes
        for col in df.columns:
            print(col)
        # Create a log file and write the results
        with open("log_Phantom_recipe_check/changes_log" + str(time.time())  + "txt", 'w') as log_file:
            for index, row in df.iterrows():
                link = row['link']
                #phantom = row['phantom']
                id = row['id']

                if 'recettes' in str(link):
                    log_file.write(f"{link} - Phantom recipe, {str(id)}\n")
                else:
                    log_file.write(f"{link} - Not a phantom recipe, {str(id)}\n")
        print("Log file created successfully.")
    return new_df

def general_column_cleaning(directory_path, colum_overview):
    for index, row in colum_overview.iterrows():
        if row["dead_column"] != True:
            x = 0

        else:
            print(f"Column '{row['column']}' is a alive column.")
            print(f"Column values: {row['column_values']}")
            print("")


    colum_overview.to_csv(directory_path + 'column_overview.tsv', index=False)
    #print(colum_overview)


def main(floder_location):
    #move_through_folder(floder_location)
    #print_column_data_from_file("G:\Code\Machine Learning\Recipe Project\\recipe_info\Group_0\A-Z\_\__0.tsv")
    #print("Hello World!")
    #create_log("G:\Code\Machine Learning\Recipe Project\\recipe_info\Group_0\A-Z\_")
    #test_link()

    #Alright so this is a double forloop which will go through the given folders and there sub files
    group_Number = 0
    group_f = "Group_" + str(group_Number) + "\\"
    group_folder_location = floder_location + group_f

    
    alphabet_list = ['_', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alphabet_list_index = 0

    phantom_df = phantom_recipe_check(group_folder_location)
    current_column_overview = collect_column_data_for_file(group_folder_location + "A-Z\\" +alphabet_list[alphabet_list_index] + "\\", phantom_df)
    #general_column_cleaning(group_folder_location + "A-Z\\" +alphabet_list[alphabet_list_index] + "\\", current_column_overview)




if __name__ == "__main__":

    #floder_location = "G:\\Code\Machine Learning\\Recipe Project\\recipe_info\\Group_0\\A-Z\\_"

    floder_location = "G:\Code\Machine Learning\Recipe Project\\recipe_info\\"

    main(floder_location)