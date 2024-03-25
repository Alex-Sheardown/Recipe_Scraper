from cmath import nan
import csv
import re
import os
import time
from recipe_scrapers import scrape_me
from googletrans import Translator
import pandas as pd
from fractions import Fraction
from fuzzywuzzy import fuzz

import sys

from seperate_ingrdeints import  remove_number_after_or, removeInvalidParenthesis, split_on_and_not_surrounded_by_numbers, split_on_comma_not_surrounded_by_numbers, split_on_or_not_surrounded_by_numbers

# Define the directory path
directory_path = os.getcwd() + "\Database and Cleaning\Table_Organizer\Ingredient_processing"

# Insert the directory path into sys.path
sys.path.insert(1, directory_path)

# Import the required module
import measurement_check as mc
import modifier_check as modc


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

def remove_prefix_underscores(input_string):
    cleaned_string = input_string
    while cleaned_string.startswith('_'):
        cleaned_string = cleaned_string[1:]
    return cleaned_string.rstrip('_')

def test_measurements(ingredient_strings, test_for_true, measurement, given_number):
    # Initialize counters for passed and total tests
    passed_tests = 0
    total_tests = len(ingredient_strings)

    # Iterate through ingredient strings and check for tablespoons
    for ingredient_string in ingredient_strings:
        #turn into method
        has_measurement, altered_text, found_number = mc.find_measurments(ingredient_string, measurement)
        if test_for_true == has_measurement: 
            if test_for_true and given_number == found_number:
                passed_tests += 1
            elif test_for_true:
                print(ingredient_string)
            else:
                passed_tests += 1
        else:
            print(ingredient_string)

    # Calculate the fraction of passed tests
    pass_fraction = passed_tests / total_tests

    if test_for_true:
        message = "contains"
    else:
        message = "does not contain"

    # Print the summary with the determined message
    print(f"\nSummary: {passed_tests} out of {total_tests} tests {message} given measurements. ({pass_fraction:.2%})")

def create_seperation(measurement, info):
    positive_test_case = []
    false_test_case = []
    portion_case = []
    name = ""
    for i in info:
            
        if i[0] == measurement:
            
            name =  i[1]  
            positive_test_case += i[2]
            portion_case += i[3]
        else:
            false_test_case += i[2]

    
    return name, positive_test_case, false_test_case, portion_case

def word_to_num(text):

    text = " " + text
    word_digit_pairs = [
        (' zero ', ' 0 '),
        (' one ', ' 1 '),
        (' two ', ' 2 '),
        (' three ', ' 3 '),
        (' four ', ' 4 '),
        (' five ', ' 5 '),
        (' six ', ' 6 '),
        (' seven ', ' 7 '),
        (' eight ', ' 8 '),
        (' nine ', ' 9 '),
        (' dozen ', ' 12 '),
        (' thirty', ' 30 ')
    ]
    
 
    # Iterate over each word-digit pair and replacing
    # the words with digits in the input string
    for word, digit in word_digit_pairs:
        text = text.replace(word, digit)

    return text

def remove_unecessary_data(text):
    
    combined_patterns = [

        r"\s*dish\(es\)",
        r"\s*decorative\s*elements",
        r"\s*according",
        r"\s*desires",
        r"it's\s*good\s*when\s*it's\s*beautiful",
        r"it\'s\s*",
        r"\s*when",
        r"\s*for\s*me",
        r"\s*for\s*the\s*soup\b",
        r'\s*on\s*top\s*of\s*the\s*lasagna\b',
        r'\s*on\s*top\s*of\s*the\b',
        r'\s*on\s*top\s*of\b',
        r'\s*on\s*top\b',

        r'\s*for\s*the\s*energy\s*bars?\b',
        r'\s*for\s*the\s*energy\b',
        r'\s*for\s*the\b',
        r"\s*for\s*top\b",

        r'\s*main\s*course\b',
        r'\s*make\s*omelette\b',
        r'\s*in\s*granola\b', 
         
        r'\s*make\s*the\s*omelette\b'
         
         
        r'\s*to\s*make\s*the\s*meatballs\b', 
        r'\s*to\s*make\s*the\b', 
        r'\s*to\s*make\b',  

         
        r'\s*to\s*the\s*sautéed\s*mushrooms\b',  
        r'\s*to\s*the\s*sautéed\b',
        r'\s*to\s*the\b', 

        r'\s*combine\b', 

        r'\s*can\s*enhance\s*the\s*flavor\s*of\s*the\s*soup\b',
        r'\s*for\s*the\s*soup\b',
         
          
        #r'\bthe\s*meatballs\s*',

        r'\s*in\s*the\s*granola\s*for\s*extra\s*crunch\b',
        r'\s*in\s*the\s*granola\s*for\s*extra\b',
        r'\s*in\s*the\s*granola\s*for\b',

        r'\s*extra\s*crunch\b',
        r'\s*for\s*a\s*generous\s*serving\b',
        r'\s*on\s*the\s*pizza\b',

        r"\s*long\s*piece\b",

        r"\s*to\s*sweeten\s*the\s*tea\s*",

        #r'\s*decorate\s*cake\s*with\b',
        #r'\s*decorate\s*cake\s*',
        r"decorate\s*the\s*cake\s*with\s*",
        r'\s*decorate\b'

        r'\bassembling\b',
        r'\s*for\s*assembling\s*tacos\b',
        r'\s*top\s*with\b',

        r"\s*you'll\s*need\b",
        r"\bdessert\b",


        r"\s*measure\s*out\b",
        
        r"\s*you'll\s*bneed\b",
        r'\s*with\s*a\b',
        r"\s*shape\s*bread\s*into\b",
        r"\s*bread\s*into\b",
        

       
        r'\barrange\b',
       
       
        r'\s*can\s*enhance\s*',
        #r'\bsandwich\b',
        r'\badded\b',
        
        
        r'\bplatter\b',
        r'\barrange\b',
        r'\bplatter\b',
        
        
        r'\bsweeten\b',
        
        r'\bthem\b',
        r'\bcarefully\b',
        r'\binclude\b',
        
        
    
        r'\b(bowl)\s*of\b',
        r'\bused\b',
        r'\bshe\b',
        r'\bhe\b',
        r'\badd\b',
        r'\bfor\b',
        r'\bthe\b',
        r'\bto\s*(stuff|cook)\b',
        #r'\bhot\b',
        r'\bpan\b',

        
        r'\bon\b',
        r'\bhis\b',
        r'\btea\b',
        r'\buse\b',
        r'\blay\b',
        r"\bwith\b",
        r"\bcreate\b",
        r"\blayer\b",
        r"\bform\b",
        r"\bstack\b",
        r"\babout\b",
        #extra space
        
        


        #experimental
        r"\binto\b",
        r"\bshape\b",
        r"\bthick\b",

        
        r'\s*weighting\b',
        r"\bweighing\b",
        
        r"\s*from\s*mandy,\s*done\\b",
        r"\s*,\s*done\b",
        r"\s*portioned\s*in\b",
        

        r"\s*,?_?\s*approximately_?\b",
        r"\bœ\b",

        r"^\s*and\b",
        r"\s*approx.\b",
        r'\b(\s*and\s*)\s*$',
        r"\b(\s*or\s*)\s*$",

        r"^\s*at\b",
        r"^\s*by\b"
        r"\s*(\(\s*taste\s*\)|taste)\b",
        
        #butter_,_
        
        r"\s*\.?amount\b",
        r"\s*roux\b",
        #r"\s*i\bvalpiform\bbread\band\bpastry\bmix\)\bquantity\bknead\bdough\bcorrectly\b",
        
        r"\babout\b",
        
        r"of",
        r"ingredients?",
        r"from",
        r"and\s*other\s*decorations?",
        r"don’?'?t\s*forget\s*",
        r"see\s*tip",
        r"cooking",
        r"amount\s*your\s*liking!",
        r"oriental\s*grocery\s*stores",
        
        r"\s*st\s*morêt",
        r",\s*,\s*.",

        r"by\s*grating\s*chocolate\s*peeler\s*",



        r"\s*supermarket\b",
        r"\s*be\s*aware\b",
        r",?however,?" ,
        r"\s*that\s*moquec\s*is\s*eaten\s*very\b",
        r"\s*childhood\b",
        r"®",
        
        r"\s*in\s*supermarkets\s*or\s*barry\s*in\s*specialist\s*stores",
        r"sold\s*in\s*supermarkets",

        r"\s*between\b",
 
        #r"\s*container",
        r"\s*if\s*you\s*cannot\s*find\s*this\s*cheese,?",
        r'\s*etc\b',

        r'\bextra?\b.*$',

        r"\s*\(\s*or",
        r"\(\s*fat",
        r"\s*made\s*above",
        r"\s*it\s*all\s*depends\s*quantity",
        r"\s*ready\s*to\s*",
        #"\s*a?\s*(few)?\s*(for)?\s*",
        r"\s*few",
        r"\s*cooked\s*at\s*home\s*or\s*in\s*a\s*can\s*",
        r"\s*to\s*your",
        r"\s*in\s*this\s*case\s*you\s*need\s*",
        r"\s*in\s*asia?n?\s*grocery\s*stores\s*",
        r"\s*strength\s*coloring\s*",
        r"\s*brand",
        r'\s*made\s*this\s*summer',
        r'\s*put\s*in\s*',
        r'\s*size',
        r'\s*diagonally',
        r'\s*but\s*as',
        r'\s*you\s*have',
        r'\s*dark/',
        r'\s*they\s*are',
        r'\s*and\s*very',
        r'\s*whatever\s*you\s*have\s*will\s*do',
        r'\s*store',
        r'\s*siphon',
        

        

        r"\s*\.\s*\.\s*\.\s*",
        #r"\s*.\s*.\s*.",

        r"\(\s*\,*\s*\.*\)",

        
    ]
    


    text = " " + text

    for cp in combined_patterns:
        text = re.sub(cp,'', text, re.IGNORECASE)
        
   
    text  = text.replace("-", " ")
    text  = text.replace(" a ", " ")
    text  = text.replace("( )", " ")
    text  = text.replace("( )", " ")
    #experimental ()
    #text  = text.replace("(", " ")
    #text  = text.replace(")", " ")
    
    #quoutes
    text  = text.replace("“", " ")
    text  = text.replace("”", " ")
    text  = text.replace("’", "'")
    text  = text.replace("é", "e")

    
    text  = text.replace("( |", " ")
    text  = text.replace("| )", " ")
    text  = text.replace("(s)", " ")
    text  = text.replace("( s)", " ")
    text  = text.replace("(s )", " ")
    text  = text.replace("( s )", " ")
    text  = text.replace(":", " ")
    
    text = text.rstrip("()")
    text = text.lstrip()
    text = text.rstrip()
    text = text.rstrip(";")
    text = text.lstrip("\\")
    text = text.lstrip("/")
    text = text.rstrip(".")
    text = text.lstrip(".")
    text = text.lstrip(",")
    
    #text = text.lstrip("a ")
    text = text.lstrip()
    text = text.rstrip()
    #interesting 
    #text = text.rstrip("and")
    text = text.rstrip()

    

    text  = ' '.join(text.split())
    return text

def check_portion(base_pattern, text):
    
    text = word_to_num(text)
    proportion = -1
    #text = text.replace('_', ' ')
    #text = text.lower()
    has_pattern = False
    altered_text = text

    """
    I will need to add my own list of special cleaning
    """
   
    combined_patterns = [
        #got to fix
        #r'between_(\d+)_and_(\d+)'
        r'(\d+(?:_\d+)?(?:\.\d+)?)\s*(?:-|to|or|and)\s*(\d+(?:_\d+)?(?:\.\d+)?)\s*',
        r'(\d+\.\d+)\s*',
        r'\s*\d+\s*',
        #r'(\d+(?:_\d+)?)\s*',/^\d*\.?\d*$/
        r'a\s*few\s*',
        #r'\b(?:few)\s*',
        r'(?:a|an)\s*',
        
        
    ]
    pattern = [base_pattern] + combined_patterns

    #print("before issue", base_pattern, text)
    match_0 = re.search(pattern[0], text, re.IGNORECASE)
    #print("after issue")
    if base_pattern == "":
        #print("First hurdle passed")
        match_0 = True
    match_1 = re.search(pattern[1] + pattern[0], text, re.IGNORECASE)        
    match_2 = re.search(pattern[2] + pattern[0], text, re.IGNORECASE)
    
    match_2_num_a = 0
    if match_2:
        match_2_num_a = match_2.group(0)
        
    match_3 = re.search(pattern[3] + pattern[0], text, re.IGNORECASE)
    match_4 = re.search(pattern[4] + pattern[0], text, re.IGNORECASE)
    match_5 = re.search(pattern[5] + pattern[0], text, re.IGNORECASE)

    #print("Pattern", pattern[5] + pattern[0], "text", text, "match", match_5)
   
    if match_0:
        altered_text = re.sub(pattern[0], ' ', text, count=1)
        has_pattern = True
        if match_1 :
            start_range = float(match_1.group(1).replace("_", " "))
            end_range = float(match_1.group(2).replace("_", " ")) if match_1.group(2) else start_range
            average = (start_range + end_range) / 2
            proportion = average
            altered_text = re.sub(pattern[1] + pattern[0], ' ', text, count=1)
        elif match_2 :
            portions = re.findall(r"\d+\.\d+",match_2.group(0))
            proportion = portions[0]
            altered_text = re.sub(pattern[2] + pattern[0], ' ', text, count=1)
        elif match_3:
            portions = re.findall(r"\d+",match_3.group(0))
            altered_text = re.sub(pattern[3] + pattern[0], ' ', text, count=1)
            proportion = portions[0]
        elif match_4:
            proportion = 3
            altered_text = re.sub(pattern[4] + pattern[0], ' ', text, count=1)
        elif match_5:
            proportion = 1
            altered_text = re.sub(pattern[5] + pattern[0],' ', text,  count=1)
        

    #remove for testing should be done after the measurement is found
    #altered_text = remove_unecessary_data(altered_text)

    #print("portion:", proportion)
    return has_pattern, altered_text, float(proportion)

def check_modifier(base_pattern, text):
    
    found_modifier = False
    text = text.replace('_', ' ')
    cleaned_text = text
    #print("pattern:", base_pattern, "text:", text)
    found_mod = re.search(base_pattern, text, re.IGNORECASE)
    while found_mod:
        found_modifier = True
        text = cleaned_text
        cleaned_text = re.sub(base_pattern, ' ', cleaned_text, re.IGNORECASE)
        found_mod = re.search(base_pattern, cleaned_text, re.IGNORECASE)


    # Use a regular expression to match spaces before another character
    cleaned_text = re.sub(r' +', ' ', cleaned_text).strip()
    

    #print(found_modifier, cleaned_text)
    return found_modifier, cleaned_text

def clean_ingredient(ingredient):
    cleaning_error = False
    try:
        ingredient = clean_ingredient_fraction(ingredient)
        ingredient = clean_ingredient_characters(ingredient)
        ingredient = clean_replace_fractions_with_decimals(ingredient)
        ingredient = ingredient.replace(" ", "_")
        #ingredient = re.sub(r'\W+', '', ingredient)
    except Exception as e:
        
        cleaning_error = True

    return ingredient, cleaning_error

def translate_edge_cases(text):
    text = text.replace("tbsp. to c. ", "tablespoon ")
    text = text.replace("tbsp._to_c._", "tablespoon ")
    
    text = text.replace("tbsp. to s.", "tablespoon ")
    text = text.replace("tbsp._to_s._", "tablespoon ")
    
    text = text.replace("c._tablespoon", "tablespoon ")
    text = text.replace("c._teaspoon", "teaspoon ")
    
    text = text.replace("c._to_s._", "tablespoon ")
    text = text.replace("c._to_c._", "teaspoon ")
    text = text.replace("c. to c.", " teaspoon ")
    text = text.replace("C. to c. ", "teaspoon ")


   
    text = text.replace("tsp._to_c._", "teaspoon ")
    text = text.replace("goat_droppings", "goat_cheese")
    text = text.replace("pork_in_the_loin_or_blade", "pork_loin_or_pork_blade")
    #c._to_c.
    #de langue de chat translates to cat tongue
    text = text.replace("cat's_tongue", "langue de chat")

    return text

def fix_edge_case(text):
    text = text.replace('\u200b', '')
    
    #sheets
    text = text.replace("pastilla sheets", "pastilla 'sheets'")
    
    #sticks
    text = text.replace("cinnamon stick", "cinnamon 'stick/s'")
    text = text.replace("surimi sticks", "surimi 'stick/s'")

    text = text.replace("(i_used_the_valpiform_bread_and_pastry_mix)__add__a_small_quantity_to_knead_the_dough_correctly", " ")
    
    text = text.replace("cornstarch_cornstarch", "cornstarch")
    return text

def process_measurement(input_text):
    # Use regex to separate numbers and 'g' and replace 'g' with 'grams'
    nput_text = re.sub(r'(\d+)_?\s*(mg)', lambda match: f"{match.group(1)} milligram", input_text, flags=re.IGNORECASE)
    input_text = re.sub(r'(\d+)_?\s*(gr.|g)', lambda match: f"{match.group(1)} grams", input_text, flags=re.IGNORECASE)
    #input_text = re.sub(r'(\d+)\s*(g)', lambda match: f"{match.group(1)} grams ", input_text, flags=re.IGNORECASE)
    
    input_text = re.sub(r'(\d+)\s*(ml)', lambda match: f"{match.group(1)} milliliters", input_text, flags=re.IGNORECASE)
    input_text = re.sub(r'(\d+)\s*(kg)', lambda match: f"{match.group(1)} kilo gram", input_text, flags=re.IGNORECASE)
    input_text = re.sub(r'(\d+)\s*(cl)', lambda match: f"{match.group(1)} centiliters", input_text, flags=re.IGNORECASE)
    input_text = re.sub(r'(\d+)\s*(l)', lambda match: f"{match.group(1)} liters", input_text, flags=re.IGNORECASE)
    input_text = re.sub(r'(\d+)\s*(%)', lambda match: f"{match.group(1)} percent", input_text, flags=re.IGNORECASE)
    return input_text

def extract_repeated_word_or_original(s):
    # Use regular expression to match repeated words
    match = re.match(r'^\s*(\b\w+\b)\s*\1\s*$', s)

    if match:
        # If a match is found, return the repeated word
        return match.group(1)
    else:
        # If no match is found, return the original string unchanged
        return s

def average_same_numbers(data):
    # Create a dictionary to store cumulative sum and count for each unique word
    word_data = {}
    
    # Process each tuple in the input list
    for word, number in data:
        if word in word_data:
            # Update cumulative sum and count for the existing word
            word_data[word][0] += number
            word_data[word][1] += 1
        else:
            # Add a new entry for the word
            word_data[word] = [number, 1]

    # Calculate the average for each word and create a list of tuples
    averaged_data = [(word, total / count) for word, (total, count) in word_data.items()]

    return averaged_data

def seperate_ingredients(text):
    
    
  
    old_status = "NA"
    multi_part_ingredient_status = "comma"
    text_list = split_on_comma_not_surrounded_by_numbers(text)
    print("comma    :", text_list)
    if len(text_list) == 1:
        #print("check 3")
        multi_part_ingredient_status = "NA"
    else:
        old_status = "comma"

    

    text_list_a = []
    multi_part_ingredient_status = "or"
    for tl in text_list:
        text_list_a+=split_on_or_not_surrounded_by_numbers(tl)

    if len(text_list_a) == len(text_list):
        multi_part_ingredient_status = old_status
    else:
        old_status = "or"

    print("or       :", text_list_a)




    
    text_list_b = []
    multi_part_ingredient_status = "and"
    for tl in text_list_a:
        text_list_b+=split_on_and_not_surrounded_by_numbers(tl)

    if len(text_list_a) == len(text_list_b):
        multi_part_ingredient_status = old_status
    else:
        old_status = "and"
    print("and      :", text_list_b)

    if "with" in text:
        multi_part_ingredient_status = "with"

    return text_list_b, multi_part_ingredient_status

def divide_numbers_in_tuples(data, divisor):
    # Divide each number in the tuples by the divisor
    result = [(unit, value / divisor) for unit, value in data]
    return result

def remove_direct_repeats(text):
    # Construct the regular expression pattern to find direct repeats of any word
    pattern = re.compile(r'\b(\w+)\s+\1\b', flags=re.IGNORECASE)
    
    # Remove direct repeats of any word
    cleaned_text = re.sub(pattern, r'\1', text)
    
    return cleaned_text

def raw_to_table_clean(text):
    
    text, error = clean_ingredient(text)
    print("0",text)
    text = translate_edge_cases(text)
    print("1",text)
    text = fix_edge_case(text)
    print("2",text)
    text = process_measurement(text)
    print("3",text)
    result_list = []
    text_list, multi_part_ingredient_status = seperate_ingredients(text)

    print(text_list)
            
    print("---------")

    last_meausurement = ""
    summary_modifier, text = modc.find_modifier(text)
    empty_text = False
    found_measurements_list_total = []
    for text in text_list:
        found_modifier, text = modc.find_modifier(text)
        found_measurements, cleaned_text = mc.find_measurement_complete(text)
        cleaned_text = extract_repeated_word_or_original(cleaned_text)
        #print(len(found_measurements))
        if len(found_measurements) != 0:
            found_measurements_list_total += [found_measurements]
        if len(cleaned_text) < 3:
            empty_text = True
            continue 
    with_split = False
    print(found_measurements_list_total, len(found_measurements_list_total))
    if len(found_measurements_list_total)== 1 and multi_part_ingredient_status == "with":
        #print("with split found")
        with_split = True

    
    for text in text_list:
        ignore_this = False
        found_modifier, text = modc.find_modifier(text)
        print("")
        print("4",text)
        found_measurements, cleaned_text = mc.find_measurement_complete(text)
        print("4.5",found_measurements)
        print("5",cleaned_text)
        cleaned_text = extract_repeated_word_or_original(cleaned_text)
        print("6",cleaned_text)
        cleaned_text = removeInvalidParenthesis(cleaned_text)
        print("7",cleaned_text)
        cleaned_text, captured_number = remove_number_after_or(cleaned_text)
        if captured_number != None:
            found_measurements.append(("self_count",captured_number))
        print("8",cleaned_text)
        print("8.5",found_measurements)


        
        hold = remove_direct_repeats(cleaned_text)
        while hold != cleaned_text:
            cleaned_text = hold
            hold = remove_direct_repeats(hold)

        print("8",cleaned_text)


        print("")

        if len(cleaned_text) < 3:
            continue 
        import hashlib
        hash_hold = ""

        if empty_text or len(found_modifier) == 0:
            found_modifier = summary_modifier

        for f in found_modifier:
            hash_hold+=f    
        hash_obj = hashlib.sha256(hash_hold.encode('utf-8'))
        hex_hash = hash_obj.hexdigest()
        hex_hash = str(hex_hash[:4])

        measurement_name = ""
        portion = "NS"



        if len(found_measurements) == 0 and with_split == False:
            
            if len(found_measurements_list_total)== 0:
            
                measurement_name = "'Not_Found'_"
                
                if last_meausurement != "":
                    found_measurements = last_meausurement
                    measurement_name = ""
            else:
                #Not sure why
                found_measurements = found_measurements_list_total[0]

                
        else:
            if with_split:
                ignore_this = True
                 
                if len(found_measurements) > 0:
                    last_meausurement = found_measurements
                    found_measurements = divide_numbers_in_tuples(found_measurements, len(text_list))
                else:
                    found_measurements = divide_numbers_in_tuples(last_meausurement, len(text_list))
            else:
                last_meausurement = found_measurements
        
        if len(found_measurements) > 0:
            portion = ""
            found_measurements = average_same_numbers(found_measurements)
            for m in found_measurements:
                n,p=m
                measurement_name += "'" + n + "'_"
                portion += str(p) + "'_"

        if len(found_measurements) == 1  :
            found_m, portion = found_measurements[0]
            if found_m == "self_count" and portion == -1:
                measurement_name = "Not_Found_"
                portion = "NS"

        name = cleaned_text + "_:_" + measurement_name
        name += ":_" + hex_hash
        name = name.replace(" ", "_")
        result_list.append((found_modifier, found_measurements, cleaned_text, hex_hash, name, portion, multi_part_ingredient_status, ignore_this))

    return result_list
