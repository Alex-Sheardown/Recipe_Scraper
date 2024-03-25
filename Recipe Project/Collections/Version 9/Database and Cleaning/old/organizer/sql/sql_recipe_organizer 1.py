import mysql.connector
import os
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="2eTavern",
  database="recipe_project"
)

cursor = mydb.cursor()

def count_rows():
    cursor.execute("SELECT COUNT(*) FROM recipe_project.information_about_recipe")

def clear_table():
    cursor.execute("DROP TABLE IF EXISTS information_about_recipe")

def create_table():
    
    query = ""
    query = query + "CREATE TABLE information_about_recipe( "

    query = query + "id                         int not null "
    query = query + ", name                     CHAR(40) "
    query = query + ", host                     CHAR(40) "
    query = query + ", link                     CHAR(40) "
    query = query + ", time                     CHAR(40) "
    query = query + ", yeild                    CHAR(40) "
    query = query + ", photo                    CHAR(40) "
    query = query + ", nutrients                CHAR(40) "
    query = query + ", instructions             CHAR(500) "
    query = query + ", number_ingredients       int not null "

    query = query + " )"

def add_column_if_does_not_exist(column_name):
    query = ""
    #query = query + "ALTER TABLE information_about_recipe add "
    #query = query + str(column_name)
    #cursor.execute(query)
    query = query + "ALTER TABLE recipe_project.information_about_recipe ADD COLUMN " +  str(column_name) +  " VARCHAR(15);"
    #cursor.execute(query)
    try:
        cursor.execute(query)
    except:
        x = 0

def add_recipe(id, name, host, link, time, yeild, photo, nutrients, instructions, number_ingredients, ingredients_and_proportions):

    query = ""
    query = query + "INSERT INTO recipe_project.information_about_recipe (id, name, host, link, time, yeild, photo, nutrients, instructions, number_ingredients "

    count = 0
    for ingredints in ingredients_and_proportions[1]:
        count = count + 1
        add_column_if_does_not_exist(ingredints)
        query = query + ",  "  +  str(ingredints) # "'" + str(ingredints) + "'" 
        
    if count == number_ingredients:

        instructions = str(instructions).replace("'", "_")
        instructions = str(instructions).replace(")", "_")
        instructions = str(instructions).replace("(", "_")

        name = str(name).replace("'", "_")
        name = str(name).replace(")", "_")
        name = str(name).replace("(", "_")

    
        query = query + ") "
        query = query + "values( " 
        query = query + str(id) 
        query = query + ",  "  + "'" + str(name) + "'" 
        query = query + ",  "  + "'" + str(host) + "'" 
        query = query + ",  "  + "'" + str(link) + "'" 
        query = query + ",  "  + "'" + str(time) + "'" 
        query = query + ",  "  + "'" + str(yeild) + "'" 
        query = query + ",  "  + "'" + str(photo) + "'" 
        query = query + ",  "  + "'" + str(nutrients) + "'"  
        query = query + ",  "  + "'" + str(instructions)+ "'" 
        query = query + ",  "  + str(number_ingredients) 

        for ingredints in ingredients_and_proportions[0]:
            query = query + ",  "  + "'" + str(ingredints) + "'" 

        query = query + "); "
        #print("I am working please see me!")
        print(query)
        try:
            #cursor.execute(query)
            #write_To_File("Database and Cleaning/links/scraped_links", link)
            with open('Database and Cleaning/links/scraped_links.txt', 'a') as file:
                file.write(str(link) + "\n")
                file.close
        except:
            
            print("Problem has occuered")
            with open('Database and Cleaning/links/error.txt', 'a') as file:
                file.write(str(link) + "\n")
                file.close
            #time.sleep(30)
        #print("see me!!!!!")
    else:
        print("There is a problem with the count")

    
    print("I exist")

