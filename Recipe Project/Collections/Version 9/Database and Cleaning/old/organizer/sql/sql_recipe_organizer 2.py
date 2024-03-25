
import os
import time

def start_fresh(cursor, host, hash_Table):
    
    #Create fresh table recipe_project
    for key, value in hash_Table.iteritems():

        query = ""
        query = query + "DROP TABLE `recipe_project`.`" + str(key) +  "'information_about_recipe`;"
        
        try:
            cursor.execute(query)
        except:
            print(query)


    query = ""
    query = query + "CREATE TABLE information_about_recipe(id int , name CHAR(100), host  CHAR(40), link CHAR(250) , time  CHAR(40) , yeild  CHAR(40), photo   CHAR(250) , nutrients   CHAR(140) , instructions   VarCHAR(5000), number_ingredients  int not null )"
    
    try:
        cursor.execute(query)
    except:
        print(query)

    query = ""
    query = query + "ALTER TABLE `recipe_project`.`information_about_recipe` CHANGE COLUMN `id` `id` INT NOT NULL , ADD PRIMARY KEY (`id`);"
    
    try:
        cursor.execute(query)
    except:
        print(query)

    

    

def count_rows(cursor):
    cursor.execute("SELECT COUNT(*) FROM recipe_project.information_about_recipe")

def clear_table(cursor):
    cursor.execute("DROP TABLE IF EXISTS information_about_recipe")

def create_table():
    #CREATE TABLE information_about_recipe(id int, name CHAR(100), host  CHAR(40), link CHAR(250) , time  CHAR(40) , yeild  CHAR(40), photo   CHAR(250) , nutrients   CHAR(140) , instructions   VarCHAR(2500), number_ingredients  int not null )information_about_recipe
    """
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
    """

#Needs to be updated to include different tables 
#Get rid of
def set_up_tables(cursor, host):
    
    query = ""
    query = query + "DROP TABLE `recipe_project`.`information_about_recipe`;"
    
    try:
        cursor.execute(query)
    except:
        print(query)
    query = ""
    query = query + "CREATE TABLE information_about_recipe(id int , name CHAR(100), host  CHAR(40), link CHAR(250) , time  CHAR(40) , yeild  CHAR(40), photo   CHAR(250) , nutrients   CHAR(140) , instructions   VarCHAR(5000), number_ingredients  int not null )"
    
    try:
        cursor.execute(query)
    except:
        print(query)

    query = ""
    query = query + "ALTER TABLE `recipe_project`.`information_about_recipe` CHANGE COLUMN `id` `id` INT NOT NULL , ADD PRIMARY KEY (`id`);"
    
    try:
        cursor.execute(query)
    except:
        print(query)

    alphebet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '_']


    for character in alphebet:

        query = ""
        query = query + "DROP TABLE `recipe_project`.`list_of_ingredients_" + host + "_" +  character +"`;"
        
        try:
            cursor.execute(query)
        except:
            print(query)


        query = ""
        query = query + "CREATE TABLE `recipe_project`.`list_of_ingredients_" +  host + "_" +  character +"` ( `id` INT NOT NULL) row_format = dynamic;"
        try:
            cursor.execute(query)
        except:
            print(query)

        query = ""
        query = query + "ALTER TABLE `recipe_project`.`list_of_ingredients_" +  host + "_" +  character +"` ADD PRIMARY KEY (`id`);"
        try:
            cursor.execute(query)
        except:
            print(query)


def add_column_if_does_not_exist(mydb, cursor, column_name, value, host, number):
    query = ""
    query = query + "ALTER TABLE recipe_project.list_of_ingredients_" +  host + "_" +  str(column_name[0]) + "_" + str(number) + " ADD COLUMN " +  str(column_name) +  " varchar("+ str(len(value)+2) +");"
    
    try:
        cursor.execute(query)
    except:
        print(query)
        print("Problem adding: " + str(column_name))
        

def update_indgredients(mydb, cursor, id, ingredient, value, host, number):

   
    query = "" 
    query = query + "UPDATE recipe_project.list_of_ingredients_" +  host + "_" +  str(ingredient[0]) + "_" + str(number)  + " " 
    query = query + "SET " +  str(ingredient) +   " = " +  "'" + str(value) + "' " 
    query = query + "Where id = " + str(id)

    try:
        #print("Iam working")
        cursor.execute(query)
        return True
    except:
        print(query)
        print("Problem updating " + str(ingredient) + " at id " + str(id) + " with value " + str(value))
        return False

#needs to read through list of tables in order to determine the table size wether it be through hash or other means.
def find_right_table(host, hash_table, first_letter):
    start_table_Name = "list_of_ingredients_" + host +  "_" +  str(first_letter) + "_" 

    #print(start_table_Name)
    
    keys = hash_table.keys()

    hold = "0"
    #print(keys)
    for key in keys:
        print(key)
        """
        if start_table_Name in key:
            #hold = str(key).replace(start_table_Name, '')
            print(key)
        """
    print(hold)
    """
    if start_table_Name in hash_table:


        for key in keys:
            hold = str(key).replace(start_table_Name, '')

    return "hold"
    """

def add_id(mydb, cursor, id, ingredient, host, hash_table):


    find_right_table(host, table_hash, first_letter)
    number = 1
    query = ""
    query = query + "INSERT INTO recipe_project.list_of_ingredients_" +  host + "_" +  str(ingredient[0]) + "_" + str(number)  + " (id) values( " + str(id) + ")"

    try:
        cursor.execute(query)
    except:
        print(query)
        print("Problem has adding id " + str(id))
        

def add_recipe(mydb, cursor, id, name, host, link, time, yeild, photo, nutrients, instructions, number_ingredients, ingredients_and_portions, host_2 , hash):
    
    
    name = str(name).replace("'", "_")
    name = str(name).replace(")", "_")
    name = str(name).replace("(", "_")

    instructions = str(instructions).replace("'", "_")
    instructions = str(instructions).replace(")", "_")
    instructions = str(instructions).replace("(", "_")

    
            

    query = ""
    query = query + "INSERT INTO recipe_project.information_about_recipe (id, name, host, link, time, yeild, photo, nutrients, instructions, number_ingredients "
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
    query = query + "); "

           
            #print("This works")
            #cursor.execute(query)
    #print(query)
    
    final_result = True

    try:
        cursor.execute(query)
        
    except:
        print("Problem has occuered with " + link)
        #print(query)
        final_result = False
        print(query)
        print("----break----")
        time.sleep(30)
      

    

    count = 0
    update_i = 0
    
    
    for ingredints in ingredients_and_portions[1]:
        count = count + 1
        add_id(mydb, cursor, id, ingredients_and_portions[1][update_i], host_2, hash)
        add_column_if_does_not_exist(mydb, cursor, ingredints, ingredients_and_portions[0][update_i], host_2)
        
        #print("This works")
                    #print(ingredients_and_portions[1][update_i])
                    #print(ingredients_and_portions[0][update_i])
        result = update_indgredients(mydb, cursor, id, ingredients_and_portions[1][update_i], ingredients_and_portions[0][update_i], host_2)
        update_i = update_i + 1

        if result == False:
            final_result = False

    if final_result == True:
        with open('Database and Cleaning/links/scraped_links.txt', 'a') as file:
            file.write(str(link) + "\n")
            file.close
    else:
        with open('Database and Cleaning/links/error.txt', 'a') as file:
            file.write(str(link) + "\n")
            file.close


def create_hash_map_of_tables(cursor):
    #mydb
    #cursor.execute("Show tables;")

    cursor.execute("SELECT max(id)  FROM recipe_project.information_about_recipe;")
    
    myresult = cursor.fetchall()

    row_count = myresult[0][0];

    cursor.execute(" SELECT table_name, count(*) FROM information_schema.columns GROUP BY table_name;")
    
    myresult = cursor.fetchall()

    list_of_tables_SQL = {
        "information_about_recipe" : row_count
    }
    


    #Need if else statement to clean out specific tables 
    for x in myresult:
        number_count = str(x[0]).count("list_of_ingredients")
        if number_count == 1:
            list_of_tables_SQL[str(x[0])] = x[1]
            #print(str(x[0]) + " " + str(x[1]))
    #print(list_of_tables_SQL)

    return list_of_tables_SQL



"""
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
    """

