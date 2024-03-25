

from recipe_scrapers import scrape_me
import os
import collections
import pandas as pd
from tsv_recipe_organizer import add_recipe_TSV
import re
from os.path import exists

ingredients_Dict = {}
id_number = 0

err_Set = set()
err_Set = {'test'}

file_name = "750g"
alphebet = ['_', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' ]


def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    
    # Print New Line on Complete
    """if iteration == total: 
        #print()
        x=0
    """

def write_To_File(file_name, link):
    with open(file_name + '.txt', 'a') as file:
        file.write(link + "\n")
        file.close


def clean_ingredient(ingredient):
    global alphebet
    ing = ingredient.replace("'", "_")
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
    
    
    if len(ing) > 2:
        
        while ing[0] == "_" and len(ing) > 0:
            ing = ing[1:]

         
        if ing[0].upper() not in alphebet:
            ing = "_" + ing
                
        
        #print("cleaning ingredient error" )

    return ing

#CREATE TABLE information_about_recipe(id int, name CHAR(40), host  CHAR(40), link CHAR(250) , time  CHAR(20) , yeild  CHAR(40), photo   CHAR(250) , nutrients   CHAR(40) , instructions   VarCHAR(1500), number_ingredients  int not null )
def scrape(link):
    global file_name
    global id_number
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

    try:
        scraper = scrape_me(link)
        title = scraper.title()
        totalTime = scraper.total_time()
        yeilds = scraper.yields()
        ingredients = scraper.ingredients()
        instructions = scraper.instructions()
        image = scraper.image()
        host = scraper.host()
        scraper.links()

        #print (title)
        #print (ingredients)

        #print(mydb.is_connected())

    except:
        write_To_File('recipe_info/links/rejected_links', link)
            

    count_ingredients = 0
    ingredients_and_portions = [[],[]]
    for inged in ingredients: 
        count_ingredients = count_ingredients + 1
        position = -1
        #Need to fix first number pull
        
        for i in range(len(inged)):
            #if inged[i].isnumeric():#ord(inged[i]) >= 48 and ord(inged[i]) <= 57:#
            if inged[i] == "0" or inged[i] == "1" or inged[i] == "2" or inged[i] == "3" or inged[i] == "4" or  inged[i] == "5" or inged[i] == "6" or inged[i] == "7" or inged[i] == "8" or inged[i] == "9": 
                position = i+1
            
        if position > -1 :
    
            #part 1
            ing =  clean_ingredient(inged[:position])
            ing = re.sub(r'\W+', '', ing)
            ingredients_and_portions[0].append(ing.lower())

            #part 2
            ing =  clean_ingredient(inged[position:])
            ing = re.sub(r'\W+', '', ing)
            ingredients_and_portions[1].append(ing.lower())
            #print(inged[:position] + " : " + ing)
        else:
            ingredients_and_portions[0].append("N_S")
            #part 3
            ing =  clean_ingredient(inged)
            ing = re.sub(r'\W+', '', ing)
            ingredients_and_portions[1].append(ing.lower())
        
        
    
    if title == "" or count_ingredients < 1 or "" in ingredients_and_portions[1] or "" in ingredients_and_portions[0]:
        write_To_File('recipe_info/links/rejected_links', link)
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
            write_To_File("recipe_info/links/recipes_with_duplicates", link)

        #print(complete_array_of_ingredients)   
        add_recipe_TSV(id_number, title, host, link, totalTime, yeilds, image, nutrients, instructions, count_ingredients, complete_array_of_ingredients)
        
        #print("link should've work " + link)

        id_number = id_number + 1
        


def read_Int_File(path):
    int_Set = set()
    int_Set = {'test' : -1}
    with open(str(path + "/internal_links.txt"), encoding='UTF8', errors='ignore') as fp:
        Lines = fp.readlines()
        for line in Lines:
            #print(line)
            
            for element in range(0, len(line)):
                try:
                    if ':' == (line[element]):
                        url = str(line[2+element:-1])
                        number = int(float(line[:element]))
                        int_Set[str(url)] = str(number)
                        count_Urls = count_Urls + 1
                except:
                    break
    
    result = [int_Set]
    return result 


def set_id():
    global id_number
    id_number = 1
    current_path = os.getcwd()
    file_path_3 = current_path + '/recipe_info/Overview/'
    final_file = file_path_3  + "overview.tsv"
    df = pd.read_table(final_file,   sep='\t') 
    if df.shape[0] > 0:
        id_number = df['id'].max()
    else:
        id_number = 1
     

def file_Check():
    print("I exist")
    global alphebet
    current_path = os.getcwd()
    file_path_1 = current_path + '/recipe_info/'
    file_path_2 = current_path + '/recipe_info/Prices/'
    file_path_3 = current_path + '/recipe_info/A-Z/'
    file_path_4 = current_path + '/recipe_info/Overview/'
    file_path_5 = current_path + '/recipe_info/links/'
    flag1 = os.path.exists(file_path_1)
    flag2 = os.path.exists(file_path_2)
    flag3 = os.path.exists(file_path_3)
    flag4 = os.path.exists(file_path_4)
    flag5 = os.path.exists(file_path_5)

    alphebet = ['_', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' ]
    
    if not flag1:
        os.mkdir(file_path_1)
        
    if not flag2:
        os.mkdir(file_path_2)
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
        file = open(file_path_5 + 'rejected_links.txt', 'w+')
        file = open(file_path_5 + 'scraped_links.txt', 'w+')
    print("Files are created!")

def main():
    global file_name
    
    file_Check()
    set_id()

    er_set = []
    rl_set = []
    sl_set = []

    current_path = os.getcwd()
    file_path_5 = current_path + '/recipe_info/links/'


    int_set = read_Int_File('Collections/Version 8/Project/' + file_name)
    
    file_exists1 = exists(file_path_5 + 'error.txt')
    file_exists2 = exists(file_path_5 + 'rejected_links.txt')
    file_exists3 = exists(file_path_5 + 'scraped_links.txt')

    if file_exists1:
        er_set = set(line.strip() for line in open(file_path_5 + 'error.txt'))
    if file_exists2 :
        rl_set = set(line.strip() for line in open(file_path_5 + 'rejected_links.txt'))
    if file_exists3:
        sl_set = set(line.strip() for line in open(file_path_5 + 'scraped_links.txt'))


    for int_link in int_set:
        for link in int_link:
            if link == "test":
                continue
            if link in er_set:
                continue
            if link in rl_set:
                continue
            if link in sl_set:
                continue
            
            print(str(link))
            scrape(link)
        break
    


if __name__ == '__main__':

    main()