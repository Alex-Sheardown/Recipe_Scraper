
#import json
#import hashlib
#import mysql.connector
from recipe_scrapers import scrape_me

ingredients_Dict = {

}
"""
def loop_Through_Website_Allrecipe(start, end):
    for x in range(start, end):
        scrape_site = 'https://www.allrecipes.com/recipe/' + str(x)
        scraper = scrape_me(scrape_site)
        title = scraper.title()
        ingredients = scraper.ingredients()
        if 0 == (title == ""):
            all_Ingredients(ingredients)
        print(scrape_site) 
    
    
    write_To_File()

def all_Ingredients(ingredients):
    for inged in ingredients: 
        
        for i in range(len(inged)):
            #print(inged) 
            if  inged[i].isalpha() or inged[i] == '(':
                #print(inged[i:])
                if 0 == (inged[i:] in ingredients_Dict):
                    ingredients_Dict[inged[i:].lower()] = 1
                    #print(inged[i:])
                else:
                     ingredients_Dict[inged[i:]] += 1
                break
    

def write_To_File():
    with open('file.txt', 'w') as file:
        for x in sorted (ingredients_Dict.keys()):
          file.write("%s\n" % x)
    print("file completed")

"""
units_of_measurementss = []

def set_up_units_of_measurement():
    global units_of_measurementss
    with open(str("units_of_measurements.txt"), encoding='UTF8', errors='ignore') as fp:
        Lines = fp.readlines()
        for line in Lines:
            units_of_measurementss.append(line)
        


def check_for_unit_of_measurement(first_part):
    global units_of_measurementss
    for unit in units_of_measurementss:
        if unit in first_part:
            return True
        else:
            return False


def main():
    
    scraper = scrape_me('https://www.bbc.co.uk/food/recipes/christmas_gingerbread_84244')
    title = scraper.title()
    totalTime = scraper.total_time()
    yeilds = scraper.yields()
    ingredients = scraper.ingredients()
    instructions = scraper.instructions()
    scraper.image()
    scraper.host()
    scraper.links()
    
    print(title)

    if title == "":
        print("not recipe")
    #print(ingredients[1])
   
    #loop_Through_Website_Allrecipe(240000, 240010)
    # 


    for inged in ingredients: 
        for step in range(1,3):

        #for i in range(len(inged)):
            number = 0
            #if  inged[i].isalpha() or inged[i] == '(' :#or check_for_unit_of_measurement(inged[:i]):

        """
    for inged in ingredients: 
        for i in range(len(inged)):
            #print(inged[i]) 
            if  inged[i].isalpha() or inged[i] == '(' :#or check_for_unit_of_measurement(inged[:i]):
                print(inged[i:])
                break
        for i in range(len(inged)):
            x = 1
        """

    print(" ") 
    """
    print("hi")
    print(title)
    print(ingredients)
    print(totalTime)
    print(yeilds)
    print(instructions)"""

if __name__ == '__main__':
    main()