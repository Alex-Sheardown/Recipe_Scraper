
import os
import time
import shutil
import pandas as pd
import numpy as np


def get_number_of_elements(list):
    count = 0
    for element in list:
        count += 1
    return count

def create_DateFrame():
    data = {'id': []}
    return pd.DataFrame(data)


"""
Finds the folder with the aproprieate ingredient column
alse creates file if several criterea 
"""
def find_Ingredient_Folder(thread_id, ingredint):
    first_Character = ingredint[0]
    current_path = os.getcwd()
    file_path_3 = current_path + '/recipe_info/Group_' +  str(thread_id) +'/A-Z/'
    final_Path = file_path_3 + first_Character + "/"
    res = []
    for path in os.listdir(final_Path):
        # check if current path is a file
        if os.path.isfile(os.path.join(final_Path, path)):
            res.append(path)
    number_of_files_in_folder = get_number_of_elements(res)
    # print("This should be zero! : " + str(number_of_files_in_folder) )
    if number_of_files_in_folder == 0:
        create_DateFrame().to_csv(final_Path + first_Character + "_0.tsv", sep="\t",index=False)
        return number_of_files_in_folder
    else:
        count = 0
        for file in res:
            df = pd.read_table(final_Path + file,  dtype='unicode')
            if ingredint in list(df.columns):
                return count
            count = count + 1

        df = pd.read_table(final_Path + res[-1],  dtype='unicode')
        if len(df.columns) < 500:
            return number_of_files_in_folder-1
        else:
            create_DateFrame().to_csv(final_Path + first_Character + "_" + str(number_of_files_in_folder) +".tsv", sep="\t",index=False)
            return number_of_files_in_folder

"""
Uses info gained from find_Ingredient_Folder to create append to folder by editing data frame 
"""
def append_Row_Ingredient(thread_id, id, ingredint, proportion):
    # id, ingredint, proportion
    first_Character = ingredint[0]
    current_path = os.getcwd()
    file_path_3 = current_path + '/recipe_info/Group_' +  str(thread_id) +'/A-Z/'
    final_Path = file_path_3 + first_Character + "/"
    final_file = final_Path + first_Character + "_" + str(find_Ingredient_Folder(thread_id, ingredint)) + ".tsv"

    add_In_Row = []
    df = pd.read_table(final_file, dtype='unicode')  

    #Updated to fix multiple ids being used in the same file. 8/31/23  
    if ingredint not in df.columns:
        df[ingredint] = 0
    # Check if the ID already exists in the DataFrame
    if id in df["id"].values:
        # Update the existing row with new values
        existing_row = df[df['id'] == id]
        existing_value = existing_row[ingredint].values[0]
        if existing_value == '0':
            # Replace the existing row with the new proportion value
            df.loc[existing_row.index, ingredint] = proportion
        else:
            df.loc[existing_row.index, ingredint] = existing_value + ' ' + str(proportion)
    else:
        # Add a new row to the DataFrame
        add_In_Row = [0] * len(df.columns)
        add_In_Row[df.columns.get_loc("id")] = id
        add_In_Row[df.columns.get_loc(ingredint)] = proportion
        df.loc[len(df.index)] = add_In_Row


    df.to_csv(final_file,index=False, sep="\t")


def add_recipe_TSV(thread_id, id, name, host, link, time, yeild, photo, nutrients, instructions, number_ingredients, ingredients_and_proportions):
   
    alphebet = {'_': 0, 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}

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
            append_Row_Ingredient(thread_id, id, ingredients_and_proportions[1][update_i], ingredients_and_proportions[0][update_i])
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
        print("Problem has occuered")
        with open('recipe_info/Group_' +  str(thread_id) +'/links/error.txt', 'a') as file:
            file.write(str(link) + "\n")
            file.close 
    

