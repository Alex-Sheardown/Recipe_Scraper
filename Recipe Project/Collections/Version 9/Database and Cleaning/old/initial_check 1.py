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

# Find the first non-zero value in 'input_column' and get its corresponding 'id'
def find_first_non_zero_id(df, column_name):
    for index, row in df.iterrows():
        if row[column_name] != 0:
            return row['id']
    return None  # Return None if no non-zero value is found

#Test builders
def find_test_set_info(file):
    directory_path = os.getcwd()  # Current directory
    directory_path += "\Database and Cleaning\Table_Organizer\\test_cases\\" + file
    print(directory_path)
    
    # Create a regular expression pattern to match numbers
    number_pattern = re.compile(r'\d+')
    result = []
    # Iterate over the files in the directory
    for filename in os.listdir(directory_path):
        # Check if the file is a regular file (not a directory)
        if os.path.isfile(os.path.join(directory_path, filename)):
            # Use regex to find the first number in the file name
            match = number_pattern.search(filename)
            if match:
                # Extract and print the first number found in the file name
                first_number = match.group()
                df = pd.read_csv(directory_path + "\\" + filename)
                #print(directory_path + "\\" + filename)
                #print(df.columns)
                original = df['original'].tolist()
                
                proportion = df['portion'].tolist()
                """
                with open(directory_path + "\\" + filename, newline='') as csvfile:
                    csv_reader = csv.reader(csvfile)
                    csv_data = []
                    # Iterate over each row in the CSV file
                    # Use a list comprehension to flatten the list
                    csv_data = [item for sublist in csv_reader for item in sublist]
                """
                result.append([int(first_number), filename, original, proportion])
                #print(f"File: {filename}, First Number: {first_number}")


    return result

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

def check_process(pattern, text):
    #print(text)
    number = 0
    text = text.replace('_', ' ')
    matches = re.findall(pattern, text, re.IGNORECASE)
    has_pattern = bool(re.search(pattern, text, re.IGNORECASE))
    altered_text = re.sub(pattern, '', text)
    """
    if matches:
        caught_quantity, caught_measurement = matches
        if caught_quantity:
            number = caught_quantity[0].strip()
    """ 
    
    """
    aprox_place_holder = "aprox"
    for match in matches:
        quantity, a_an, few, aprox, measurement = match
        #print(f"Quantity: {quantity.strip() if quantity else 'N/A'}, Measurement: {measurement.strip()}")
        if quantity:
            print(f"Quantity: {quantity}")
        
        if aprox:
            print(f"Approximation: {aprox}")
        
        if a_an:
            print(f"Indefinite Article: {a_an}")
        
        if few:
            print(f"Few: {few}")
    
        if measurement:
            print(f"Measurement: {measurement}")
            if quantity:
                number = quantity
            elif a_an and few:
                number = 3
            elif a_an:
                number = 1

            aprox_place_holder = aprox
"""

    print(aprox_place_holder)

    return has_pattern, altered_text, int(number)

def overall_test(folder):
    info = find_test_set_info(folder)
    for i in range(0, len(info)): # len(info)
        measurement, positive_test_case, false_test_case, portion_case =  create_seperation(i, info)
        print("")
        print(measurement, i)
        print("="*30)
        
        test_measurements(positive_test_case, portion_case, True, i)
        test_measurements(false_test_case,portion_case, False, i)
        #input("next batch")

def test_pattern(pattern, pattern_number, match_type, folder):
        # Test cases with different valid formats
        info = find_test_set_info(folder)
        name, positive_test_case, false_test_case, number_cases =  create_seperation(pattern_number, info)
        testCase = [ positive_test_case, false_test_case]
        print("")
        print("Special: " + name)
        print("="*30)

        type_P_or_F = 1
        if match_type:
            type_P_or_F = 0
        count = 0
        #Alter here
        count = 0
        passed_tests = 0
        #print(number_cases)
        for input_string in testCase[type_P_or_F]:
            # Find all matches using the simplified regex pattern

            #turn into method
            has_measurement, altered_text, found_number = check_process(pattern, input_string)
            if match_type == has_measurement: 
                if match_type and found_number == number_cases[count]:
                    passed_tests += 1
                elif match_type:
                    print("fail 2:",input_string, found_number, number_cases[count])
                else:
                    passed_tests += 1
            else:
                print("fail 1:",input_string, found_number)
            count += 1

            """
            matches = bool(re.search(pattern, input_string.replace('_', ' '), re.IGNORECASE))
            check_process()
            if matches == match_type:
                count += 1
                #print(input_string)
            else:
                #print(match_type, matches)
                print(input_string.replace('_', ' '))

            """
        print("")
        print(passed_tests)
        print(len(testCase[type_P_or_F]))
        print("")

def column_overview_processing():
    x = 0
