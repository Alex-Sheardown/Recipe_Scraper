
import re

import os
import sys



# Define the base directory path
base_path = os.getcwd() + "\Database and Cleaning\Table_Organizer\Ingredient_processing"
# Insert base path into sys.path
sys.path.insert(1, base_path)
import initial_check as ic

full_process_specific_test = True

if full_process_specific_test:

    folder = "\Database and Cleaning\Table_Organizer\\test_cases\measurements_cleaning\general_test.csv"
    #ic.overall_test_measurements_enhanced(os.getcwd() + folder)]

    #text = "5_cans_of_natural_tuna"
    #text = "24_oz_5_cans_of_natural_large_tuna"
    #text = "1 - 7_large_ apples"
    #text = "a tablespoon of something"
    #text = "chair"
    #text =  "sliced ​​smoked salmon"
    
    #need fixing
    #remove U+200b
    #text = "5 tbsp sugar"
    #text = "3 tbsp. to s. Amora ketchup"
    #text =  "20ml_milk"
    #text =  "1kg_white_spanish_melon"
    
    #text =  "10cl of white wine"
    #text =  "1l of chicken stock"

    #text =  "1 c. to c. level(s) of baking powder"
    #text =  "4 tbsp. to s. sweetened condensed milk"
    #text =  "500g_fresh_peas_(_175g_shelled)"
    #text =  "8 tbsp. to c. orange marmalade"
    #text =  "1 c. to c. vanilla extract or liquid vanilla"
    text = "8 pats of butter"
    result = ic.raw_to_table_clean(text)
    fmo, fme, text, mod_hash, name, portion = result



    print("modifiers", fmo,"measurements", fme,"text:", text, "hash:", mod_hash,"name", name, "portion", portion)

    


#print(re.sub(r'\s*\d+\s*\s*'," ", "5 pears"))
 
