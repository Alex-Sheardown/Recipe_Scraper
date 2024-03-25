
import json
import hashlib
#import mysql.connector
from recipe_scrapers import scrape_me
from sql_recipe_organizer import add_recipe
import os

ingredients_Dict = {}
id_number = 0

err_Set = set()
err_Set = {'test'}

def write_To_File(file_name, link):
    with open(file_name + '.txt', 'a') as file:
        file.write(link + "\n")
        file.close

#CREATE TABLE information_about_recipe(id int, name CHAR(40), host  CHAR(40), link CHAR(250) , time  CHAR(20) , yeild  CHAR(40), photo   CHAR(250) , nutrients   CHAR(40) , instructions   VarCHAR(1500), number_ingredients  int not null )
def scrape(link):

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
                ingredients_and_portions[0].append(inged[:position])
                ing = inged[position:].replace("'", "_")
                ing = ing.replace(")", "_")
                ing = ing.replace("(", "_")
                ing = ing.replace(".", "")
                ing = ing.replace(" ", "_")
                if ing[0] == "_":
                    ing = ing[1:]
                ingredients_and_portions[1].append(ing)
                #print(inged[:position] + " : " + ing)
            else:
                ingredients_and_portions[0].append("not_given")
                ing = inged.replace("'", "_")
                ing = ing.replace(")", "_")
                ing = ing.replace("(", "_")
                ing = ing.replace(".", "")
                ing = ing.replace(" ", "_")
                if ing[0] == "_":
                    ing = ing[1:]
                ingredients_and_portions[1].append(ing)
                #print(ing)
        
       
    
        if title == "":
            write_To_File('Database and Cleaning/links/rejected_links', link)
        else:
            add_recipe(id_number, title, host, link, totalTime, yeilds, image, nutrients, instructions, count_ingredients, ingredients_and_portions)
            id_number = id_number + 1
            print("this part is being processed")
            
            #os.system("pause")
        
    except:
        write_To_File('Database and Cleaning/links/rejected_links', link)
        
    
    
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
    id_number = 0
    with open(str(path + ".txt"), encoding='UTF8', errors='ignore') as fp:
        Lines = fp.readlines()
        for line in Lines:
            id_number = id_number + 1
            #print("reading")
            err_Set.add(line.replace("\n", ""))
    #print(err_Set)

def main():
    file_name = "750g"
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
    read_Err_File('Database and Cleaning/links/rejected_links')
    read_Err_File('Database and Cleaning/links/scraped_links')
    #main()
    scrape("https://www.750g.com/lasagnes-au-fromage-rape-bello-gratinato-giovanni-ferrari-r83076.htm")
    #write_To_File('Database and Cleaning/links/rejected_links', "link")