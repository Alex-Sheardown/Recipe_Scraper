
import json
import hashlib
#import mysql.connector
from recipe_scrapers import scrape_me
from sql_recipe_organizer import add_recipe
from sql_recipe_organizer import update_indgredients
import os
import collections

from sql_recipe_organizer import set_up_tables
from sql_recipe_organizer import create_hash_map_of_tables
from sql_recipe_organizer import find_right_table

import time
import re
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="2eTavern",
  database="recipe_project",
  autocommit=True
)
cursor = mydb.cursor()

ingredients_Dict = {}
id_number = 0

err_Set = set()
err_Set = {'test'}

file_name = "750g"


def write_To_File(file_name, link):
    with open(file_name + '.txt', 'a') as file:
        file.write(link + "\n")
        file.close


def clean_ingredient(ingredient):
    ing = ingredient.replace("'", "_")
    ing = ing.replace(")", "_")
    ing = ing.replace("(", "_")
    ing = ing.replace(".", "")
    ing = ing.replace(" ", "_")
    ing = ing.replace(",", "_")
    ing = ing.replace(":", "_")
    ing = ing.replace("&", "and")
    ing = ing.replace("/", "divide")
    ing = ing.replace("+", "add")


    while ing[0] == "_" and ing.length > 0:
        ing = ing[1:]

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

        print (title)
        print (ingredients)

        #print(mydb.is_connected())

    except:
        write_To_File('Database and Cleaning/links/rejected_links', link)
            

    count_ingredients = 0
    ingredients_and_portions = [[],[]]
    for inged in ingredients: 
        count_ingredients = count_ingredients + 1
        position = -1
        for i in range(len(inged)):
            #if inged[i].isnumeric():#ord(inged[i]) >= 48 and ord(inged[i]) <= 57:#
            if inged[i] == "0" or inged[i] == "1" or inged[i] == "2" or inged[i] == "3" or inged[i] == "4" or  inged[i] == "5" or inged[i] == "6" or inged[i] == "7" or inged[i] == "8" or inged[i] == "9": 
                position = i+1
                #print(inged[i])
            
        #print(inged)
            
        if position > -1 :
            
            #Replace to methods
    
            #part 1

            """
            ing = inged[:position].replace("'", "_")
            ing = ing.replace(")", "_")
            ing = ing.replace("(", "_")
            ing = ing.replace(".", "")
            ing = ing.replace(" ", "_")
            ing = ing.replace(",", "_")
            ing = ing.replace(":", "_")
            ing = ing.replace("&", "and")
            ing = ing.replace("/", "divide")
            ing = ing.replace("+", "add")
            """
            ing =  clean_ingredient(inged[:position])
            
            ing = re.sub(r'\W+', '', ing)
            ingredients_and_portions[0].append(ing.lower())

            #part 2
            """
            ing = inged[position:].replace("'", "_")
            ing = ing.replace(")", "_")
            ing = ing.replace("(", "_")
            ing = ing.replace(".", "")
            ing = ing.replace(" ", "_")
            ing = ing.replace(",", "_")
            ing = ing.replace(":", "_")
            ing = ing.replace("&", "and")
            ing = ing.replace("/", "divide")
            ing = ing.replace("+", "add")
            """
            
            ing =  clean_ingredient(inged[position:])
            
            ing = re.sub(r'\W+', '', ing)
            ingredients_and_portions[1].append(ing.lower())
            #print(inged[:position] + " : " + ing)
        else:
            ingredients_and_portions[0].append("N_S")
            
            #part 3
            """
            ing = inged.replace("'", "_")
            ing = ing.replace(")", "_")
            ing = ing.replace("(", "_")
            ing = ing.replace(".", "")
            ing = ing.replace(" ", "_")
            ing = ing.replace(",", "_")
            ing = ing.replace(":", "_")
            ing = ing.replace("&", "and")
            ing = ing.replace("/", "divide")
            ing = ing.replace("+", "add")

            """
           
            ing =  clean_ingredient(inged)
                
            ing = re.sub(r'\W+', '', ing)
            ingredients_and_portions[1].append(ing.lower())
                #print(ing)
        
        
        
    
    if title == "" or count_ingredients < 1 or "" in ingredients_and_portions[1] or "" in ingredients_and_portions[0]:
        write_To_File('Database and Cleaning/links/rejected_links', link)
    else:
        
        #Need to merge duplicates
        complete_array_of_ingredients= [[],[]]
        count_1 = 0
        for ing in ingredients_and_portions[1] :

            if ing in complete_array_of_ingredients[1]:
                continue
            complete_array_of_ingredients[1].append(ing)
            complete_array_of_ingredients[0].append("")                       
                
            count_1 = count_1 + 1
            count_2 = 0
            for ingredient_number_2 in ingredients_and_portions[0] :
                    #print("I work ")
                if ing == ingredient_number_2:
                    if "" == ingredient_number_2:
                        complete_array_of_ingredients[0][count_1] = str(ingredient_number_2)
                    else:
                        complete_array_of_ingredients[0][count_1] = str(complete_array_of_ingredients[0][count_1]) + " + " + str(ingredient_number_2)
                count_2 = count_2 + 1
                    
        hold = [item for item, count in collections.Counter(ingredients_and_portions[1]).items() if count > 1]

        if len(hold) > 0 :
            write_To_File("recipes_with_duplicates", link)

            
            #print(complete_array_of_ingredients)

            #Adjust in order to add straight list of ingredients 
            
            #Creative list of ingredients
        add_recipe(mydb, cursor, id_number, title, host, link, totalTime, yeilds, image, nutrients, instructions, count_ingredients, ingredients_and_portions, file_name)
            #add_recipe(mydb, cursor, id_number, title, host, link, totalTime, yeilds, image, nutrients, instructions, count_ingredients, ingredients_and_portions)
            

        id_number = id_number + 1
        print("link should've work " + link)
            #os.system("pause")
        
    
        

    #quiwrite_To_File('scraped_links', link)

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


def read_Err_File(path):
    global err_Set
    global id_number
    id_number = 1
    with open(str(path + ".txt"), encoding='UTF8', errors='ignore') as fp:
        Lines = fp.readlines()
        for line in Lines:
            id_number = id_number + 1
            #print("reading")
            err_Set.add(line.replace("\n", ""))
    #print(err_Set)

def main():
    global file_name
    
    int_set = read_Int_File('Collections/Version 8/Project/' + file_name)
    for int_link in int_set:
        for link in int_link:
            if link == "test":
                continue
            if str(link) not in err_Set:
                print(str(link))
                scrape(link)
        break
    


if __name__ == '__main__':

    #set_up_tables(cursor, "750g")
  
    #read_Err_File('Database and Cleaning/links/rejected_links')
    #read_Err_File('Database and Cleaning/links/scraped_links')
    #main()
    #scrape("https://www.750g.com/tartines-de-chevre-boursault-r82975.htm")
    #write_To_File('Database and Cleaning/links/rejected_links', "link")
    dictionary_of_tables = create_hash_map_of_tables(cursor)
    find_right_table("750g", dictionary_of_tables, "a")