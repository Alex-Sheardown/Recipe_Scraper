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
        (' nine ', ' 9 ')
    ]
    
 
    # Iterate over each word-digit pair and replacing
    # the words with digits in the input string
    for word, digit in word_digit_pairs:
        text = text.replace(word, digit)

    return text

def remove_unecessary_data(text):
    combined_patterns = [

        r"\s*for\s*the\s*soup\b",
        r'\s*on\s*top\s*of\s*the\s*lasagna\b',
        r'\s*on\s*top\s*of\s*the\b',
        r'\s*on\s*top\s*of\b',
        r'\s*on\s*top\b',

        r'\s*for\s*the\s*energy\s*bars?\b',
        r'\s*for\s*the\s*energy\b',
        r'\s*for\s*the\b',

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
        r'\bsandwich\b',
        r'\badded\b',
        
        
        r'\bplatter\b',
        r'\barrange\b',
        r'\bplatter\b',
        
        
        r'\bsweeten\b',

        r'\bthem\b',
        r'\bcarefully\b',
        r'\binclude\b',
        
        
    
        r'\bof\b',
        r'\bused\b',
        r'\bshe\b',
        r'\bhe\b',
        r'\badd\b',
        r'\bfor\b',
        r'\bthe\b',
        r'\bto\b',
        r'\bhot\b',
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

        r'\s*weighting\s*',
        r"\bweighing\b",
        r"\s*from\s*mandy,\s*done\\s*",
        r"\s*,\s*done\s*",
        r"\s*portioned\s*in\s*",


        r"\s*,?_?\s*approximately_?\s*",
        r"\bcreate\b",
        r"\bcreate\b",
        r"\bcreate\b",
        r"\bcreate\b",
        r"\bcreate\b",



    ]
    
    

    text = " " + text

    for cp in combined_patterns:
        text = re.sub(cp,'', text, re.IGNORECASE)
    
    text  = text.replace("-", " ")
    text  = text.replace(" a ", " ")
    text  = text.replace("( )", " ")
    
    text  = text.replace("( |", " ")
    text  = text.replace("| )", " ")
    text  = text.replace("(s)", " ")
    text  = text.replace("( s )", " ")
    text  = text.replace(":", " ")
    
    text = text.lstrip()
    text = text.rstrip()
    text = text.rstrip(".")
    text = text.lstrip(".")
    text = text.lstrip(",")
    
    #text = text.lstrip("a ")
    text = text.lstrip()
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
        
        r'(\d+(?:_\d+)?(?:\.\d+)?)\s*(?:-|to)\s*(\d+(?:_\d+)?(?:\.\d+)?)\s*',
        r'\s*\d+\.\d+\s*',
        r'\s*\d+\s*',
        #r'(\d+(?:_\d+)?)\s*',/^\d*\.?\d*$/
        r'\s*a\s*few\s*',
        #r'\b(?:few)\s*',
        r'\bs(?:a|an)\s*',
        
        
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
    #print("pattern:", base_pattern, "text:", text)

    cleaned_text = re.sub(base_pattern, ' ', text, re.IGNORECASE)
    while text != cleaned_text:
        found_modifier = True
        text = cleaned_text
        cleaned_text = re.sub(base_pattern, ' ', text, re.IGNORECASE)


    # Use a regular expression to match spaces before another character
    cleaned_text = re.sub(r' +', ' ', cleaned_text).strip()
    

    if text != cleaned_text:
        found_modifier = True

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
    text = text.replace("tbsp._to_s. ", "tablespoon ")
    
    text = text.replace("c._tablespoon", "tablespoon ")
    text = text.replace("c._teaspoon", "teaspoon ")
    
    text = text.replace("c._to_s._", "tablespoon ")
    text = text.replace("c._to_c._", "teaspoon ")
    text = text.replace("c. to c.", " teaspoon ")
    text = text.replace("C. to c. ", "teaspoon ")
    #c._to_c.


    return text

def fix_edge_case(text):
    text = text.replace('\u200b', '')
    
    #sheets
    text = text.replace("pastilla sheets", "pastilla 'sheets'")
    
    #sticks
    text = text.replace("cinnamon stick", "cinnamon 'stick/s'")
    text = text.replace("surimi sticks", "surimi 'stick/s'")
    
    return text

def process_measurement(input_text):
    # Use regex to separate numbers and 'g' and replace 'g' with 'grams'

    input_text = re.sub(r'(\d+)\s*(g|G)', lambda match: f"{match.group(1)} grams", input_text, flags=re.IGNORECASE)
    input_text = re.sub(r'(\d+)\s*(ml)', lambda match: f"{match.group(1)} milliliters", input_text, flags=re.IGNORECASE)
    input_text = re.sub(r'(\d+)\s*(kg)', lambda match: f"{match.group(1)} kilo gram", input_text, flags=re.IGNORECASE)
    input_text = re.sub(r'(\d+)\s*(cl)', lambda match: f"{match.group(1)} centiliters", input_text, flags=re.IGNORECASE)
    input_text = re.sub(r'(\d+)\s*(l)', lambda match: f"{match.group(1)} liters", input_text, flags=re.IGNORECASE)
    input_text = re.sub(r'(\d+)\s*(dl)', lambda match: f"{match.group(1)} deciliter", input_text, flags=re.IGNORECASE)
    return input_text

def raw_to_table_clean(text):
    
    
    text, error = clean_ingredient(text)
    #print("0",text)
    text = translate_edge_cases(text)
    #print("1",text)
    text = fix_edge_case(text)
    #print("2",text)
    text = process_measurement(text)
    #print("3",text)
    #print(text)
    found_modifier, text = modc.find_modifier(text)
    #print("4",text)
    found_measurements, cleaned_text = mc.find_modifier_complete(text)
    #print("5",cleaned_text)
    import hashlib
    
    hash_hold = ""
    for f in found_modifier:
        hash_hold+=f    
    hash_obj = hashlib.sha256(hash_hold.encode('utf-8'))
    hex_hash = hash_obj.hexdigest()
    hex_hash = str(hex_hash[:4])

    
    measurement_name = ""
    portion = "NS"

    if len(found_measurements) == 0:
        measurement_name = "Not_Found_"

    
    if len(found_measurements) > 0:
        portion = ""
        for m in found_measurements:
            n,p=m
            measurement_name += n + "_"
            portion += str(p) + "_"

    if len(found_measurements) == 1:
        found_m, portion = found_measurements[0]
        if found_m == "self_count" and portion == -1:
            measurement_name = "Not_Found_"
            portion = "NS"

    name = cleaned_text + "_:_" + measurement_name

    name += ":_" + hex_hash

    name = name.replace(" ", "_")


    #portion = 1
    return found_modifier, found_measurements, cleaned_text, hex_hash, name, portion

