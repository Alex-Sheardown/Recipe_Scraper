

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
from tsv_recipe_organizer_3 import add_recipe_TSV, append_Row_Ingredient

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

    return ingredient

def clean_ingredient(ingredient):
    
    ing = ingredient.lower()
    ing = ing.replace("'", "_")
    ing = ing.replace(")", "_")
    ing = ing.replace("(", "_")
    ing = ing.replace(".", "")
    ing = ing.replace(" ", "_")
    ing = ing.replace(",", "_")
    ing = ing.replace(":", "_")
    ing = ing.replace("&", "_and_")
    ing = ing.replace("/", "_divide_")
    ing = ing.replace("+", "_add_")
    ing = ing.replace("%", "_percent_")
    ing = ing.replace("½", "_half_")
    ing = ing.replace("é", '_é')
    ing = ing.replace("_¼_", "_quater_")
    ing = ing.replace(" ", "_")
    
    ing = re.sub(r'\W+', '', ing)
   
    return ing

def scrape(thread_id, translation_Needed,  number_of_Cores):
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
    
        length_per_thread = int(len(int_set)/number_of_Cores)
        start= int(thread_id * length_per_thread)
        end = start+length_per_thread-1

        if thread_id == 3:
            end = len(int_set)

        print(str(start) + " " + str(end))

        count = 0
        for i in range(start, (start+length_per_thread)):
        

            link = int_set[i]
            if link == "test":
                continue
            if link in er_set:
                continue
            if link in rl_set:
                continue
            if link in sl_set:
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
                        instructions = translator.translate(instructions).text
                        #problem here new file needed incase becuase translations can be fixed and is causing missed recipes
                    except Exception as e:
                            print(e)
                            write_To_File('recipe_info/Group_' +  str(thread_id) +'/links/translation_error', link)
                            translation_error_caught = True    
                
                count_ingredients = 0
                ingredients_and_portions = [[],[]]
                for inged in ingredients:
                    
                    if translation_Needed:
                        time.sleep(1)
                        try:
                            translated_Ingredient = translator.translate(str(inged)).text
                            inged = translated_Ingredient
                        except Exception as e:
                            if translation_error_caught == False :
                                write_To_File('recipe_info/Group_' +  str(thread_id) +'/links/translation_error', link)
                                
                    inged =  clean_ingredient(inged)
                    count_ingredients = count_ingredients + 1
                    position = -1
                    #Need to fix first number pull
                    #Find the first number !1?
                    first_Number_Found = False
                    for i in range(len(inged)):
                        if inged[i] in numbers_Check: 
                            if first_Number_Found == False:
                                position = i
                            position = i+1
                            
                    if position > -1 :
                        #part 1
                        ing =  remove_Excess(inged[:position])
                        ingredients_and_portions[0].append(ing)

                        #part 2
                        ing = remove_Excess(inged[position:])
                        ingredients_and_portions[1].append(ing)
                    else:
                        #part 3
                        ingredients_and_portions[0].append("N_S")
                        ingredients_and_portions[1].append(remove_Excess(inged))
                        
                if title == "" or count_ingredients < 1 or "" in ingredients_and_portions[1] or "" in ingredients_and_portions[0]:
                    write_To_File('recipe_info/Group_' +  str(thread_id) +'/links/rejected_links', link)
                else:    
                    duplicates = False
                    complete_array_of_ingredients= [[],[]]
                    for ingredient_1 in ingredients_and_portions[1]:
                        updated_Valeu = ""
                        if ingredient_1 not in complete_array_of_ingredients[1]:
                            complete_array_of_ingredients[1].append(ingredient_1)
                            count_1 = 0
                            for ingredient_2 in ingredients_and_portions[1]:
                                if ingredient_1 == ingredient_2:
                                    if updated_Valeu == "":
                                        updated_Valeu = updated_Valeu +  ingredients_and_portions[0][count_1] 
                                    else:
                                        updated_Valeu = updated_Valeu + " + " +  ingredients_and_portions[0][count_1] 

                                count_1 = count_1 + 1
                            complete_array_of_ingredients[0].append(updated_Valeu)
                        else:
                            duplicates = True

                    if duplicates == True:
                        write_To_File('recipe_info/Group_' +  str(thread_id) +'/links/recipes_with_duplicates', link)

                    #print(complete_array_of_ingredients)   
                    add_recipe_TSV(thread_id, id_number, title, host, link, totalTime, yeilds, image, nutrients, instructions, count_ingredients, complete_array_of_ingredients)
                    id_number = id_number + 1
                    if thread_id == 0:
                        printProgressBar(previous_Count + count, length_per_thread,  prefix = 'Progress:', suffix = 'Complete', length = 50)

            if count % 1000 and id_number == 0:
                create_backup()
            count = count + 1
            #print("Thread ID: " + str(thread_id))
            #printProgressBar(previous_Count + count, length_per_thread,  prefix = 'Progress:', suffix = 'Complete', length = 50)
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
    print("I exist")
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
    print("Files are created!")




def main(translation_Needed, file_name, number_of_Cores):
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
    list_of_Threads = []

    
    for thread_id in range(number_of_Cores):    
        print(thread_id)
        thread = threading.Thread(target=scrape, args=(thread_id, translation_Needed, number_of_Cores), name='Task_' + str(thread_id))
        list_of_Threads.append(thread)
        thread.start()
            


    for thread in list_of_Threads:
        thread.join()
     

    print("I have finished")


def create_backup():

    current_path = os.getcwd()
    src = current_path + '/recipe_info/'
    dst = current_path + '/back_up/'
    shutil.copyfile(src, dst)


if __name__ == '__main__':

    file_name = "750g"
    number_of_Cores = 4
    translation_Needed = True
    main(translation_Needed, file_name, number_of_Cores)
    print("The code is done")
