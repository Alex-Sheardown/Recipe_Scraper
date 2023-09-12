#This file is for testing links processing


import re
import os
import time
from recipe_scrapers import scrape_me
#from translate import Translator
from googletrans import Translator
import pandas as pd
from fractions import Fraction

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

