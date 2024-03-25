
import os
import pandas as pd



def get_number_of_elements(list):
    count = 0
    for element in list:
        count += 1
    return count

def create_DateFrame():
    data = {'id': []}
    return pd.DataFrame(data)


def find_Ingredient_Folder(thread_id, ingredint):
    first_Character = ingredint[0]
    alphebet = ['_', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    if first_Character not in alphebet:
        first_Character = "_"
    current_path = os.getcwd()
    file_path_3 = current_path + '/recipe_info/Group_' +  str(thread_id) +'/A-Z/'
    final_Path = file_path_3 + first_Character + "/data/"
    res = []
    
    for path in os.listdir(final_Path):
        # check if current path is a file
        if os.path.isfile(os.path.join(final_Path, path)):
            res.append(path)
    number_of_files_in_folder = len(res)
    #print("This should be zero! : " + str(number_of_files_in_folder) )
    if number_of_files_in_folder == 0:
        create_DateFrame().to_csv(final_Path + first_Character + "_0.tsv", sep="\t",index=False)
        return number_of_files_in_folder
    else:
        count = 0
        for file in res:
            
            df = pd.read_table(final_Path + file,  dtype='unicode')
            if ingredint in list(df.columns) :
                return count
            count = count + 1

        df = pd.read_table(final_Path + res[len(res)-1],  dtype='unicode')
        if len(df.columns) < 150:
            return len(res)-1
        else:
            create_DateFrame().to_csv(final_Path + first_Character + "_" + str(len(res)) +".tsv", sep="\t",index=False)
            return number_of_files_in_folder

"""
Uses info gained from find_Ingredient_Folder to create append to folder by editing data frame 
"""


# Function to update the DataFrame
def update_dataframe(dataframe,  columns_to_mark_true, id_value):
    # Check if the ID already exists in the DataFrame
    if id_value in dataframe['ID'].values:
        #print(f"ID {id_value} already exists. Skipping update.")
        return dataframe

    for possible_new_column in columns_to_mark_true:
        if possible_new_column not in dataframe.columns:
            dataframe[possible_new_column] = False

    # Add a new row with the given ID
    new_row = {'ID': id_value}
    #print("Section 2")

    for col in dataframe.columns[1:]:  # Exclude 'ID' column
        new_row[col] = col in columns_to_mark_true

    dataframe = dataframe._append(new_row, ignore_index=True)

    return dataframe

def add_row_if_unique(dataframe, new_data, value):
    # Create a DataFrame with the new row
    #new_df = pd.DataFrame([new_data])

    # Check if the combination of unique_columns in the new data is unique
    #is_unique = ~new_df.set_index(unique_columns).index.isin(dataframe.set_index(unique_columns).index)

    # Check if all rows are unique for the specified columns
    
    #print(dataframe)
    if value not in dataframe['name'].values:
            # Append the new row to the DataFrame
        dataframe = dataframe._append(new_data, ignore_index=True)
            #print("Row added successfully.")
    
    return dataframe

def append_Row_Ingredient(thread_id, id, ingredint, proportion, fmo, mod_hash):
    # id, ingredint, proportion
    first_Character = ingredint[0]
    alphebet = ['_', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    if first_Character not in alphebet:
        first_Character = "_"
        
    current_path = os.getcwd()
    file_path_3 = current_path + '/recipe_info/Group_' +  str(thread_id) +'/A-Z/'
    final_Path = file_path_3 + first_Character + "/"
    final_file = final_Path +  "/data/" + first_Character +"_" + str(find_Ingredient_Folder(thread_id, ingredint)) + ".tsv"

    add_In_Row = []

    
    df = pd.read_table(final_file, dtype='unicode')
    
     
    #print("here")   
    if ingredint not in list(df.columns):
        df[ingredint] = 0
    for column_Name in df.columns:
        if column_Name == "id":
            add_In_Row.append(id)
        elif column_Name == ingredint:
            add_In_Row.append(proportion)
        else:
            add_In_Row.append(0)
    #print(add_In_Row)
    df.loc[len(df.index)] = add_In_Row
    df.to_csv(final_file,index=False, sep="\t")

    
    file_path_hash_table = current_path + '/recipe_info/Group_' +  str(thread_id) +'/hash_table.tsv'
    
    # Create or read the DataFrame from the file
    data = {'ID': []}
    #print("Section 1")
    try: 
        df = pd.read_csv(file_path_hash_table)
    except FileNotFoundError:
        df = pd.DataFrame(data)
       

    df = update_dataframe(df, mod_hash, fmo)

    # Save the updated DataFrame to the file
    df.to_csv(file_path_hash_table, index=False)
    

    data_frame = pd.read_csv(final_Path + 'column_overview.tsv', dtype='unicode', sep='\t', header=0)
    new_row = {'name': ingredint, 'first_id': id}
    # Specify the columns to check for uniqueness
    #unique_columns_to_check = ['name']
    df = add_row_if_unique(data_frame, new_row, ingredint)
    df.to_csv(final_Path + 'column_overview.tsv',index=False, sep="\t")
   


def add_recipe_TSV(thread_id, id, name, host, link, time, yeild, photo, nutrients, instructions, number_ingredients, ingredients_and_proportions):
   
    
    instructions = str(instructions).replace("'", "_")
    instructions = str(instructions).replace(")", "_")
    instructions = str(instructions).replace("(", "_")
    instructions = str(instructions).replace('\n\n', '')
    instructions = str(instructions).replace('\\n', '')
    instructions = str(instructions).replace('\n', '')
    instructions = str(instructions).replace('\n', '')
    instructions = str(instructions).replace('\n', '')
    instructions = str(instructions).replace('’', "'")
    instructions = str(instructions).replace('`', "'")
    instructions = str(instructions).replace('\r', " ")
    instructions = instructions.replace(r'\n', '')
    instructions = str(instructions).strip()
    instructions = str.join(" ", str(instructions).splitlines())
    instructions = str.join(" ", str(instructions).splitlines())

    name = str(name).replace("'", "_")
    name = str(name).replace(")", "_")
    name = str(name).replace("(", "_")
    name = str(name).replace("\\n", "")
    
    try:
        
        update_i = 0
        for ingredints in ingredients_and_proportions[1]:
            append_Row_Ingredient(thread_id, id, ingredients_and_proportions[1][update_i], ingredients_and_proportions[0][update_i],ingredients_and_proportions[2][update_i], ingredients_and_proportions[3][update_i])
            update_i = update_i + 1

        current_path = os.getcwd()
        file_path_3 = current_path + '/recipe_info/Group_' +  str(thread_id) +'/Overview/'
        final_file = file_path_3  + "overview.tsv"

        df = pd.read_table(final_file,   sep='\t', dtype='unicode')  
        df = df.reset_index(drop=True)
        add_In_Row = []

        add_In_Row.append(id)
        add_In_Row.append(name)
        add_In_Row.append(host)
        add_In_Row.append(link)
        add_In_Row.append(time)
        add_In_Row.append(yeild)
        add_In_Row.append(photo)
        add_In_Row.append(nutrients)
        add_In_Row.append(instructions)
        add_In_Row.append(number_ingredients)


        df.loc[len(df.index)] = add_In_Row
        df.to_csv(final_file, sep="\t",index=False)


        with open('recipe_info/Group_' +  str(thread_id) +'/links/scraped_links.txt', 'a') as file:
            file.write(str(link) + "\n")
            file.close
         
    except Exception as e: 
        print( str(e))
        print("error found !!!")
        with open('recipe_info/Group_' +  str(thread_id) +'/links/error.txt', 'a') as file:
            file.write(str(link) + "\n")
            file.close 
    

