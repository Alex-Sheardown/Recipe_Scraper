#This file is for testing links processing


import re
import os
import time
from recipe_scrapers import scrape_me
#from translate import Translator
from googletrans import Translator
import pandas as pd
from fractions import Fraction

from fuzzywuzzy import fuzz

def test_link(link):
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
        print("fail")

    overview = "title: " + title + "\n"
    overview += "totalTime: " + str(totalTime) + "\n"
    overview += "yeilds: " + str(yeilds) + "\n"
    overview += "ingredients: " + str(ingredients) + "\n"
    overview += "instructions: " + str(instructions) + "\n"
    overview += "image: " + image + "\n"
    overview += "host: " + host + "\n"
    #print(overview)
    return ingredients
    



#made 8/25/23
def split_string_and_number(input_string):
    for i, char in enumerate(input_string):
        if char.isdigit():
            first_part = input_string[:i]
            j = i
            while j < len(input_string) and (input_string[j].isdigit() or input_string[j] == "." or input_string[j] == "/"or input_string[j] == "_"or input_string[j] == "-"):
                j += 1
            number = input_string[i:j]
            second_part = input_string[j:]
            return first_part, number, second_part
    return input_string, None, ""

#Determine what actually needs to be replaced
def clean_ingredient_characters(ingredient):
    
    ing = ingredient.lower()
    ing = ing.replace("+", "_add_")
    ing = ing.replace("%", "_percent_")
    ing = ing.replace("é", '_é')
    ing = ing.replace("Pray or pray where", "salt_or_fine_salt")
    ing = ing.replace("lawyer", "avocado")
    
    #ing = ing.replace(" ", "_")

    
    #ing = re.sub(r'\W+', '', ing)

    ing = re.sub(r'⅒','1/10', ing)
    ing = re.sub(r'¼','1/4', ing)
    ing = re.sub(r'½','1/2', ing)
    ing = re.sub(r'¾','3/4', ing)
    ing = re.sub(r'⅓','1/3', ing)
    ing = re.sub(r'⅔','2/3', ing)
    ing = re.sub(r'⅗','3/5', ing)
    ing = re.sub(r'⅘','4/5', ing)
    ing = re.sub(r'¼','1/4', ing)
    ing = re.sub(r'⅙','1/6', ing)
    ing = re.sub(r'⅝','5/8', ing)
    ing = re.sub(r'⅞','7/8', ing)
    ing = re.sub(r'⅕','1/5', ing)
    ing = re.sub(r'⅛','1/8', ing)
    ing = re.sub(r'⅜','3/8', ing)

    ing = re.sub(r'⅖','2/5', ing)
    ing = re.sub(r'⅐','1/7', ing)
    ing = re.sub(r'⅑','1/9', ing)
    ing = re.sub(r'⅜','3/8', ing)


   
    return ing

#Needs the code for where the data is stored though the logic is sound
def seperate_to_ingredient_proportion(first_part, number, second_part):
    
    status = "not_determined"
    # All empty: 000
    if first_part == "" and number == None and second_part == "":
        status = "000"
    # Probably Imposible second part only : 001
    elif first_part == "" and number == None and len(second_part) > 0:
        status = "001"
    # Only proportion given : 010
    elif first_part == "" and number != None and second_part == "":
        status = "010"
    # Proportion the ingredient : 011
    elif first_part == "" and number != None and len(second_part) > 0:
        status = "011"
    # No found proportion ingredient found : 100 
    elif len(first_part) > 0 and number == None and second_part == "":
        status = "100"
    # Probabaly imposible ingredient found in second and fisrt section no proportion : 101
    elif len(first_part) > 0 and number == None and len(second_part) > 0:
        status = "101"
    # Ingrdient and number : 110
    elif len(first_part) > 0 and number != None and second_part == "":
        status = "110"
    # Ingrdient and number : 111
    elif len(first_part) > 0 and number != None and len(second_part) > 0:
        status = "111"
    return status

def ingredient_proportions_test():
    test_strings = [
        "123Hello456World789",    # Number at the beginning
        "Hello123456World789",    # Number in the middle
        "HelloWorld123456789",    # Number at the end
        "Hello123World",          # Number at the beginning
        "HelloWorld",             # No number
        "123",                    # Number only
        "456World",               # Number at the beginning
        "789",                    # Number only
        "hello123test456world789",# Number three times throughout
        "",                       # Empty
        "hello 1.2 world",        # decimal
        "Hello123",               # Word then Number
        "Hello1/23"               # Fraction


    ]

    for test_string in test_strings:
        first_part, number, second_part = split_string_and_number(test_string)
        print("Input:", test_string)
        print("First Part:", first_part)
        print("Number:", number)
        print("Second Part:", second_part)
        print("Status:", seperate_to_ingredient_proportion(first_part, number, second_part))
        print("=" * 30)

#This one fixes the fraction problem
def clean_ingredient_fraction(ingredient):
    # Define a dictionary to map fraction strings to their numeric values
    fraction_map = {
        "⅒": 1/10,
        "¼": 1/4,
        "½": 1/2,
        "¾": 3/4,
        "⅓": 1/3,
        "⅔": 2/3,
        "⅕": 1/5,
        "⅖": 2/5,
        "⅗": 3/5,
        "⅘": 4/5,
        "⅙": 1/6,
        "⅝": 5/8,
        "⅞": 7/8
        # Add more fractions as needed
    }
    
    # Regular expression pattern to match fraction strings
    fraction_pattern = r'_(⅒|¼|½|¾|⅓|⅔|⅕|⅖|⅗|⅘|⅙)_'
    
    # Find fraction strings in the ingredient and replace them with their numeric values
    matches = re.findall(fraction_pattern, ingredient)
    for match in matches:
        fraction_value = fraction_map.get(match)
        if fraction_value is not None:
            ingredient = ingredient.replace(f'_{match}_', f'{fraction_value}')
    
    return ingredient

# Regular expression pattern to match fractions and mixed numbers
fraction_pattern = r'(\d+\s+\d+/\d+|\d+/\d+)'

def clean_replace_fractions_with_decimals(input_string):
    def fraction_to_decimal(match):
        fraction_str = match.group(0)
        if ' ' in fraction_str:
            whole_part, fraction_part = fraction_str.split(' ', 1)
            mixed_number = str(float(whole_part) + Fraction(fraction_part))
            return mixed_number
        else:
            return str(float(Fraction(fraction_str)))

    # Define the regex pattern to match fractions like "1/2" or "1 1/2"
    fraction_pattern = r'\d+\s+\d+/\d+|\d+/\d+'
    
    # Use re.sub to find and replace fractions with decimals in the input string
    result_string = re.sub(fraction_pattern, fraction_to_decimal, input_string)
    return result_string


input_string = "This is 1/2 of a pie and 1 1/2 cups of flour."
output_string = clean_replace_fractions_with_decimals(input_string)
#print(output_string)


def remove_prefix_underscores(input_string):
    cleaned_string = input_string
    while cleaned_string.startswith('_'):
        cleaned_string = cleaned_string[1:]



    return cleaned_string.rstrip('_')


# Find the first non-zero value in 'input_column' and get its corresponding 'id'
def find_first_non_zero_id(df, column_name):
    for index, row in df.iterrows():
        if row[column_name] != 0:
            return row['id']
    return None  # Return None if no non-zero value is found







# Define a regular expression pattern to match tablespoons variations
tablespoon_pattern = r"\d+(?:[_\s]*t(?:\.|able)?\s*(?:b\s*(?:\.\s*)?s?\s*)?(?:p\s*(?:\.\s*)?o\s*(?:\.\s*)?o\s*(?:\.\s*)?n?)?)?"
teaspoon_pattern = r"(\d+(?:_\d+)?)\s*[_\s]*(?:[tT](?:ea)?[_\s]*[sS](?:[pP](?:\.(?:s|ful)?)?|\.?\s*p|\.?[sS]|\.?[pP]_[sS])?|t\s*s\.?\s*p|t\s*p\.?s|t\s*[._]?\s*[sS]\s*[._]?\s*[pP]|t\s*[._]?\s*[sS]\s*)\s*(?:of)?\s*"#r"(tea *spoon|tsp(?:\.|n(?:\.|s)?)?|tblsp)"
oz_pattern = r"(ounce|oz(?:\.|s)?)"
fl_oz_pattern = r"(fl(?:\.|uid)?[\s_]*oz|fluid[\s_]*ounce)"#r"(fl(?:\.|uid)?\s*oz|fluid\s*ounce)"
cup_pattern = r"(?:\d+[\s_]*c(?:\.|ups)?(?:[\s_]+of)?)"#r"(?:\d+\s*c(?:\.|ups)?(?:\s+of)?)"
qt_pattern = r"(?:\d+[\s_]*q(?:uarts?|t)(?:\.|s)?)"
pint_pattern = r"(pint|pt)[\s_]*(?:n(?:\.|s)?)?"
gallon_pattern = r"(gallon|gal)[\s_]*(?:n(?:\.|s)?)?"
lb_pattern = r"(pound|lb|lbs|lb\.s|lbs\.)[\s_]*(?:n(?:\.|s)?)?"
mL_pattern = r"(milliliter|mL|mLs)[\s_]*(?:n(?:\.|s)?)?"
g_pattern = r"(\d+(?:_?\d+)?)[\s_]*(gram|g|gs|g\.s|gs\.)[\s_]*"
kg_pattern = r"(kilogram|kg|kgs|kg\.s|kgs\.)[\s_]*(?:n(?:\.|s)?)?"
l_pattern = r"(\d+)[\s_]*(liter|l|ls|l\.s|ls\.)(?:s|s\.|s\.)?\b"


#Not tested
drops_pattern = r"(\d+)_*(drop|droplet|drops)(?:s|s\.|s\.)?\b"
dash_pattern = r"(\d+)_*(dash)(?:es|es\.|es\.)?\b"
dab_pattern = r"(\d+)_*(dab)(?:s|s\.|s\.)?\b"
dl_pattern = r"(\d+_*(?:deciliter|dl)(?:s)?)(?:\.|n(?:\.|s)?)?"
squeeze_pattern = r"(\d+)_*(squeeze(?:s)?)"
clove_pattern = r"(\d+)_*(clove(?:s)?)"
few_sprigs_pattern = r"(\d+)_*(a\s*few\s*sprigs)"
handful_pattern = r"(\d+)_*(a\s*handful)"

#find pattern not added to find_measurments(ingredient_string, measurement)
bunch_pattern = r"(\d+)_*(a\s*handful)"
pinch_pattern = r"(\d+)_*(a\s*handful)"#a_small_pinch
pats_pattern = r"(\d+)_*(a\s*handful)"#a_few_pats
piece_pattern = r"(\d+)_*(a\s*handful)"#a_piece few



"""
We'll go from here
"""
#little might need some work
little_pattern = r"(\d+)_*(a\s*handful)"#a_little_medium

sprigs_pattern = r"(\d+)_*(a\s*handful)"#a_few_sprigs
knob_pattern = r"(\d+)_*(a\s*handful)"#knob
bit_pattern = r"(\d+)_*(a\s*handful)"
cl_pattern = r"(\d+)_*(a\s*handful)"#about_6_cl_of_water_(salma_used_milk_but_i_wanted_to_change)
slice_pattern = r"(\d+)_*(a\s*handful)" # a_small_slice
can_pattern = r"(\d+)_*(a\s*handful)" 



# tough ones cause its a multi pattern
approximately_pattern = r"(\d+)_*(a\s*handful)" #might be connected to a patttern
about_pattern = r"(\d+)_*(a\s*handful)" #might be connected to a patttern
#o 500


"""
about_5_or_6_tablespoons
about_2_or_3_thick?
about_twenty_

approx._8_dl

also_2_tsp_of_

or

_and_

_and/or_

percent__
,
_your_choice

up_to_
_or_(optional)# replace or none
or_less_depending_on_taste
i.e._
or_other
"""
# end catch all multi non standard cause of different endings
few_pattern = r"(\d+)_*(a\s*handful)" #might be connected to a patttern
a_pattern = r"(\d+)_*(a\s*handful)"#Lastone 


"""
Idea turn  a and a few into a modifier for determining there is something
a_dozen
a_small_slice
a_few
a_sprig
a_few_drops
a_drizzle
a_stick
a_good
a_tbsp
a_small_handful_
a_small_amount_of_
a_large_
a_good_kilo_of_
a_glass_of_
an_ example an_egg_white
a_bowl_of_
a_splash_of_
a_plate_of_
a_whole_
a_can
a_tbsp
#little is complicated
a_blend
a_dose
a_pod
a_can_of_
a_salad_
a_small_box_of_
a_splash_
a_generous_bunch_of_chopped_
a_touch_of_
a_small_jar_of_
a_packet_of_
a_large_can_of_
a_shoulder_of_
a_few_stalks_of_
a_bunch_of_
a_punnet_of_
a_box_of_
a_glass_of_
a_nice_handful_of_
a_hint_of_
a_zest_of_grated_
a_few_spoons_of_extra_
a_small_bottle_of_
a_little_
a_whole_head_of_
a_pot_of_
a_slice_of_
a_large_box_of_
a_sachet_of_
a_roll_of_
a_cork_of_
a_bag_of_
a_jar_of_
a_base_of_
a_glass_of_
a_small_brick_of_
a_chopped_
a_store-bought_
a_c._teaspoon_of_
a_log_gutter_instead_of_a_
a_few_small_
a_leftover_
an_infusion_of_
a_bouquet_garni_
a_punnet_of_
a_tray_of_
a_carton_of_
a_cube_of_s
a_brunoise_
an_average_
a_good_handful_of_
a_small_bouquet_
"""

"""
add_
assortment_of_
"""


# Define a function to check for tablespoons in an ingredient string
def find_measurments(ingredient_string, measurement):

    if measurement == 1:
        return bool(re.search(tablespoon_pattern, ingredient_string, re.IGNORECASE))
    elif measurement == 2:
        return bool(re.search(teaspoon_pattern, ingredient_string, re.IGNORECASE))
    elif measurement == 3:
        return bool(re.search(oz_pattern, ingredient_string, re.IGNORECASE))
    elif measurement == 4:
        return bool(re.search(fl_oz_pattern, ingredient_string, re.IGNORECASE))
    elif measurement == 5:
        return bool(re.search(cup_pattern, ingredient_string, re.IGNORECASE))
    elif measurement == 6:
        return bool(re.search(qt_pattern, ingredient_string, re.IGNORECASE))
    elif measurement == 7:
        return bool(re.search(pint_pattern, ingredient_string, re.IGNORECASE))
    elif measurement == 8:
        return bool(re.search(gallon_pattern, ingredient_string, re.IGNORECASE))
    elif measurement == 9:
        return bool(re.search(lb_pattern, ingredient_string, re.IGNORECASE))
    elif measurement == 10:
        return bool(re.search(mL_pattern, ingredient_string, re.IGNORECASE))
    elif measurement == 11:
        return bool(re.search(g_pattern, ingredient_string, re.IGNORECASE))
    elif measurement == 12:
        return bool(re.search(kg_pattern, ingredient_string, re.IGNORECASE))
    elif measurement == 13:
        return bool(re.search(l_pattern, ingredient_string, re.IGNORECASE))
    
    elif measurement == 14:
        return bool(re.search(drops_pattern, ingredient_string, re.IGNORECASE))
    elif measurement == 15:
        return bool(re.search(dash_pattern, ingredient_string, re.IGNORECASE))
    elif measurement == 16:
        return bool(re.search(dab_pattern, ingredient_string, re.IGNORECASE))
    elif measurement == 17:
        return bool(re.search(dl_pattern, ingredient_string, re.IGNORECASE))
    elif measurement == 18:
        return bool(re.search(squeeze_pattern, ingredient_string, re.IGNORECASE))
    elif measurement == 19:
        return bool(re.search(clove_pattern, ingredient_string, re.IGNORECASE))
    elif measurement == 20:
        return bool(re.search(few_sprigs_pattern, ingredient_string, re.IGNORECASE))
    elif measurement == 21:
        return bool(re.search(handful_pattern, ingredient_string, re.IGNORECASE))
    

    else:
        return False


