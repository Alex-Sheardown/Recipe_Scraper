

import os
from queue import Queue
import re
import threading 
import time
import pandas as pd
from os.path import exists
from recipe_scrapers import scrape_me
#from translate import Translator
from googletrans import Translator
from tsv_recipe_organizer_5 import add_recipe_TSV
import Table_Organizer.Linkchecker as tl

import shutil

int_set = []



def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):

    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    
def write_To_File(file_name, link):
    with open(file_name + '.txt', 'a') as file:
        file.write(link + "\n")
        file.close

def remove_Excess(ingredient):
    alphebet = ['_', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' ]
    numbers_Check = ["0" , "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    if len(ingredient) > 2:
        
        while ingredient[0] == "_" or ingredient[0] == " " and len(ingredient) > 0:
            ingredient = ingredient[1:]

         
        if ingredient[0].upper() not in alphebet and ingredient[0] not in numbers_Check:
            ingredient = "_" + ingredient

        if not ingredient[0].isalpha():
            ingredient = "_" + ingredient


    return ingredient

def clean_ingredient(ingredient):
    
    ingredient = tl.clean_ingredient_fraction(ingredient)
    ingredient = tl.clean_ingredient_characters(ingredient)
    ingredient = tl.clean_replace_fractions_with_decimals(ingredient)
    ingredient = ingredient.replace(" ", "_")
    #ingredient = re.sub(r'\W+', '', ingredient)


    return ingredient

def scrape(thread_id, translation_Needed,  number_of_Cores, source_language):
    try :
        global file_name
        global int_set

        translator = Translator()
        er_set = []
        rl_set = []
        sl_set = []

        file_Check(thread_id)
        id_number = set_id(thread_id)

        current_path = os.getcwd()
        file_path_1 = current_path + '/recipe_info/Group_' +  str(thread_id) +'/' 
        file_path_5 = file_path_1 + 'links/'

        file_exists1 = exists(file_path_5 + 'error.txt')
        file_exists2 = exists(file_path_5 + 'rejected_links.txt')
        file_exists3 = exists(file_path_5 + 'scraped_links.txt')

        if file_exists1:
            er_set = set(line.strip() for line in open(file_path_5 + 'error.txt'))
        if file_exists2 :
            rl_set = set(line.strip() for line in open(file_path_5 + 'rejected_links.txt'))
        if file_exists3:
            sl_set = set(line.strip() for line in open(file_path_5 + 'scraped_links.txt'))
        previous_Count = len(er_set)+len(rl_set)+len(sl_set)
        if thread_id == -1:
            
            print("previous count: " + str(previous_Count))
            print("error count  : " + str(len(er_set)))
            print("rejected count : " + str(len(rl_set)))
            print("scraped count  : " + str(len(sl_set)))

    
        length_per_thread = int(len(int_set)/number_of_Cores)
        start= int(thread_id * length_per_thread)
        end = start+length_per_thread-1

        if thread_id == 3:
            end = len(int_set)

        print("Starting Thread " + str(thread_id) + " processing:" + str(start) + " " + str(end))

        count = 0
        for i in range(start, (start+length_per_thread)):
        
            count = count + 1
            link = int_set[i]
            keyword = 'recettes'
            if link == "test": 
                continue
            if link in er_set:
                continue
            if link in rl_set:
                continue
            if link in sl_set:
                continue
            if keyword in link:
                write_To_File('recipe_info/Group_' +  str(thread_id) +'/links/rejected_links', link)
                continue

            title = ""
            ingredients = "not_given"
            title = "not_given"
            totalTime = "not_given"
            yeilds = "not_given"
            ingredients = "not_given"
            instructions = "not_given"
            image = "not_given"
            host = "not_given"
            nutrients = "not_given"
            numbers_Check = ["0" , "1", "2", "3", "4", "5", "6", "7", "8", "9"]
            link_excepted = True
            translation_error_caught = False
            try:
                time.sleep(1)
                scraper = scrape_me(link)
                title = scraper.title()
                totalTime = scraper.total_time()
                yeilds = scraper.yields()
                ingredients = scraper.ingredients()
                instructions = scraper.instructions()
                image = scraper.image()
                host = scraper.host()
                scraper.links()

            except Exception as e: 
                #print( str(e))
                #print("problem is here") 
                write_To_File('recipe_info/Group_' +  str(thread_id) +'/links/rejected_links', link)
                link_excepted = False
                
            if link_excepted:
                if translation_Needed:
                    try:
                        time.sleep(1)
                        instructions = translator.translate(instructions, src=source_language).text
                        #problem here new file needed incase becuase translations can be fixed and is causing missed recipes
                    except Exception as e:
                            print(e)
                            write_To_File('recipe_info/Group_' +  str(thread_id) +'/links/translation_error', link)
                            translation_error_caught = True    
                
                count_ingredients = 0
                ingredients_and_portions = [[],[],[]]
                error_ingredient_status = False
                for inged in ingredients:
                    
                    if translation_Needed:
                        time.sleep(1)
                        try:
                            translated_Ingredient = translator.translate(str(inged), src=source_language).text
                            inged = translated_Ingredient
                        except Exception as e:
                            if translation_error_caught == False :
                                write_To_File('recipe_info/Group_' +  str(thread_id) +'/links/translation_error', link)
                                
                    inged =  clean_ingredient(inged)
                    count_ingredients = count_ingredients + 1
                    
                    #start
                    first_part, number, second_part = tl.split_string_and_number(inged)
                    status = tl.seperate_to_ingredient_proportion(first_part, number, second_part)

                    
                    ingredients_and_portions[2].append(status)
                    if  status == "100":
                        ingredients_and_portions[0].append("N_S")
                        ingredients_and_portions[1].append(remove_Excess(first_part))

                    elif status == "011":
                        ingredients_and_portions[0].append(tl.remove_prefix_underscores(number))
                        ingredients_and_portions[1].append(remove_Excess(second_part))

                    elif status == "111" or status == "110":
                        ingredients_and_portions[0].append("N_S")
                        ingredients_and_portions[1].append(remove_Excess(first_part + number + second_part))
       
                    else: 
                        error_ingredient_status = True
 
                if error_ingredient_status or title == "" or count_ingredients < 1 or "" in ingredients_and_portions[1] or "" in ingredients_and_portions[0]:
                    write_To_File('recipe_info/Group_' +  str(thread_id) +'/links/rejected_links', link)
                
                else:    
                    
                    add_recipe_TSV(thread_id, id_number, title, host, link, totalTime, yeilds, image, nutrients, instructions, count_ingredients, ingredients_and_portions)
                    id_number = id_number + 1
                    if thread_id == 0:
                        #print("previous count: " + str(previous_Count))
                        #print("added count: " + str(count))
                        printProgressBar(count, length_per_thread,  prefix = 'Progress:', suffix = 'Complete', length = 50)

                    if id_number % 1000 == 0:
                        create_backup(thread_id, id_number/5)
                #count = count + 1
        print("thread " + str(thread_id) + " is done!")
    except Exception as e:
        print(e) 
                       
def read_Int_File(path):
   
    result = []
    with open(str(path + "/internal_links.txt"), encoding='UTF8', errors='ignore') as fp:
        Lines = fp.readlines()
        for line in Lines:
            for element in range(0, len(line)):
                if ':' == (line[element]):
                    url = str(line[2+element:-1])
                    result.append(url)
                    break
    return result 

def set_id(thread_id):
    id_number = 1
    current_path = os.getcwd()
    file_path_3 = current_path + '/recipe_info/Group_' +  str(thread_id) +'/'
    final_file = file_path_3  + "Overview/overview.tsv"
    df = pd.read_table(final_file,   sep='\t') 
    if df.shape[0] > 0:
        id_number = df['id'].max() + 1
    else:
        id_number = 1
    return id_number
     
def file_Check(number):

    global alphebet
    current_path = os.getcwd()

    file_path_1 = current_path + '/recipe_info/Group_' +  str(number) +'/' 
    
    file_path_3 = file_path_1 + 'A-Z/'
    file_path_4 = file_path_1 + 'Overview/'
    file_path_5 = file_path_1 + 'links/'
    flag1 = os.path.exists(file_path_1)
    flag3 = os.path.exists(file_path_3)
    flag4 = os.path.exists(file_path_4)
    flag5 = os.path.exists(file_path_5)

    alphebet = ['_', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' ]
    
    
    if not flag1:
        os.mkdir(file_path_1)
    if not flag3:
        os.mkdir(file_path_3)
        for letter in alphebet:
            os.mkdir(file_path_3 + letter + "/")
            os.mkdir(file_path_3 + letter + "/data")

    if not flag4:
        os.mkdir(file_path_4)
        data = {'id': [], 'name': [], 'host': [], 'link': [], 'time': [], 'yeild': [], 'photo': [], 'nutrients': [], 'instructions': [], 'number_ingredients': []}
        df = pd.DataFrame(data)
        df.to_csv(file_path_4 + "overview.tsv", sep="\t" ,index=False)
    if not flag5:
        os.mkdir(file_path_5)
        file = open(file_path_5 + 'error.txt', 'w+')
        file = open(file_path_5 + 'recipes_with_duplicates.txt', 'w+')
        file = open(file_path_5 + 'translation_error.txt', 'w+')
        file = open(file_path_5 + 'rejected_links.txt', 'w+')
        file = open(file_path_5 + 'scraped_links.txt', 'w+')

    if not flag3:
        for letter in alphebet:
            overview_path = file_path_3 + letter + "\\"
            new_data = {'name': [], 'status': []}
            df = pd.DataFrame(new_data)
            df.to_csv(overview_path + "column_overview.tsv", sep="\t" ,index=False)
            
def main(translation_Needed, file_name, number_of_Cores, source_language):
    global int_set
    current_path = os.getcwd()
    file_path_0 = current_path + '/recipe_info/'
    file_path_2 = current_path + '/recipe_info/Prices/'
    flag0 = os.path.exists(file_path_0)
    flag2 = os.path.exists(file_path_2)


    if not flag0:
        os.mkdir(file_path_0)
    if not flag2:
        os.mkdir(file_path_2)

    int_set = read_Int_File('Collections/Version 8/Project/' + file_name)


    check_groups_and_replace(file_path_0,number_of_Cores)

    list_of_Threads = []
    for thread_id in range(number_of_Cores): 
        thread = threading.Thread(target=scrape, args=(thread_id, translation_Needed, number_of_Cores, source_language), name='Task_' + str(thread_id))
        list_of_Threads.append(thread)
        thread.start()
            
    for thread in list_of_Threads:
        thread.join()

    print("I have finished")
   
def check_groups_and_replace(file_path, number_of_cores):

    for i in range(number_of_cores):
        group_folder = file_path + "\\Group_" + str(i)
        corrupted_files = find_and_check_tsv_files(group_folder)
        if len(corrupted_files) == 0:
            print("No corrupted TSV files found in Group: " + str(i))
        
        else:
            print("Group " + str(i) + " corrupted TSV files:")
            for file_path in corrupted_files:
                print(file_path)

            backup_folder = find_back_up(i)
            
            if replace_folder_with_backup(group_folder, backup_folder):
                print("Group " + str(i) + " has been reset to the last save")
            
def find_back_up(thread):
    current_path = os.getcwd()
    current_path += "//recipe_info_back_up"
    folders = [f for f in os.listdir(current_path) if os.path.isdir(os.path.join(current_path, f))]
    
    largest_value = 0
    
    best_path = ""
    for folder in folders:
        if float(folder) > largest_value:
            group_path = current_path + "//" + folder
            group_folder = [f for f in os.listdir(group_path) if os.path.isdir(os.path.join(group_path, f))]
            
            if "Group_" + str(thread) in group_folder:
                largest_value = float(folder)
                best_path = group_path + "//Group_" + str(thread)

    return best_path

def create_backup(thread_id, count):

    current_path = os.getcwd()
    source_folder = current_path + '/recipe_info/Group_' +  str(thread_id) +'/'
    destination_folder = current_path + '/recipe_info_back_up/' +  str(count) +'/Group_' +  str(thread_id) +'/'

    try:
        shutil.copytree(source_folder, destination_folder)
    except Exception as e:
        print(f'Create_Backup Error: {e}')
        X = 0

def is_tsv_valid(file_path):
    try:
        # Attempt to read the TSV file using pandas
        df = pd.read_csv(file_path, sep='\t',low_memory=False)
        return True  # If successful, consider it valid
    except :
        return False  # Parsing error indicates corruption
    
def find_and_check_tsv_files(folder_path):
    corrupted_files = []

    # Recursively search for TSV files in the folder and its subfolders
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".tsv"):
                file_path = os.path.join(root, file)
                if not is_tsv_valid(file_path):
                    corrupted_files.append(file_path)

    return corrupted_files

def replace_folder_with_backup(original_folder, backup_folder):
    try:
        # Verify that the original folder exists
        if not os.path.exists(original_folder):
            print(f"Original folder '{original_folder}' does not exist.")
            return

        # Verify that the backup folder exists
        if not os.path.exists(backup_folder):
            print(f"Backup folder '{backup_folder}' does not exist.")
            return

        # Delete the original folder and its contents
        shutil.rmtree(original_folder)

        # Copy the backup folder to the original folder's location
        shutil.copytree(backup_folder, original_folder)

        print(f"Folder '{original_folder}' has been replaced with the backup.")
        return True

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False

if __name__ == '__main__':

    file_name = "750g"
    number_of_Cores = 4
    translation_Needed = True
    source_language = 'fr'
    main(translation_Needed, file_name, number_of_Cores, source_language)
    print("The code is done")
