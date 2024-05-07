
from fractions import Fraction
import json
import re

#Stage 0 A
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

#Stage 0 B
#Determine what actually needs to be replaced
def clean_ingredient_characters(ingredient):
    
    ing = ingredient.lower()
    ing = ing.replace("+", " add ")
    ing = ing.replace("%", " percent ")
    ing = ing.replace("é", 'e')
    ing = ing.replace("Pray or pray where", "salt or fine salt")
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

# Regular expression pattern to match fractions and mixed numbers
#fraction_pattern = r'(\d+\s+\d+/\d+|\d+/\d+)'
#Stage 0 C
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

#Stage 0 D
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
        (' fifteen ', ' 15 '),
        (' thirty', ' 30 '),
        (' forty ', ' 40 ')
    ]
    
 
    # Iterate over each word-digit pair and replacing
    # the words with digits in the input string
    for word, digit in word_digit_pairs:
        text = text.replace(word, digit)

    return text

# Stage 0
def clean_ingredient(ingredient):
    cleaning_error = False
    try:
        ingredient = clean_ingredient_fraction(ingredient)
        ingredient = clean_ingredient_characters(ingredient)
        ingredient = clean_replace_fractions_with_decimals(ingredient)
        #ingredient = ingredient.replace(" ", "_")
        ingredient = word_to_num(ingredient)
        #ingredient = re.sub(r'\W+', '', ingredient)
    except Exception as e:
        cleaning_error = True
    return ingredient, cleaning_error

#Stage 1
def edge_cases(text):
    text = text.replace('\u200b', '')
    text = text.replace("tbsp. to c. ", "tablespoon ")
    text = text.replace("tbsp. to s.", "tablespoon ")
    
    text = text.replace("c. tablespoon", "tablespoon ")
    text = text.replace("c. teaspoon", "teaspoon ")
    
    text = text.replace("c. to s. ", "tablespoon ")
    text = text.replace("c. to c. ", "teaspoon ")
    text = text.replace("c. to c.", " teaspoon ")
    text = text.replace("C. to c. ", "teaspoon ")
    text = text.replace("tsp. to c. ", "teaspoon ")
    text = text.replace("goat droppings", "goat cheese")


    text = text.replace("duck or goose foie gras", "duck foie gras or goose foie gras")
    
    text = text.replace("pork in the loin or blade", "pork loin or pork blade")

    return text

#Stage 2
def process_measurement(input_text):
    # Use regex to separate numbers and 'g' and replace 'g' with 'grams'
    nput_text = re.sub(r'(\d+)_?\s*(mg)\b', lambda match: f"{match.group(1)} milligram", input_text, flags=re.IGNORECASE)
    input_text = re.sub(r'(\d+)_?\s*(gr.|g)\b', lambda match: f"{match.group(1)} grams", input_text, flags=re.IGNORECASE)
    #input_text = re.sub(r'(\d+)\s*(g)', lambda match: f"{match.group(1)} grams ", input_text, flags=re.IGNORECASE)
    
    input_text = re.sub(r'(\d+)\s*(ml)\b', lambda match: f"{match.group(1)} milliliters", input_text, flags=re.IGNORECASE)
    input_text = re.sub(r'(\d+)\s*(kg)\b', lambda match: f"{match.group(1)} kilo gram", input_text, flags=re.IGNORECASE)
    input_text = re.sub(r'(\d+)\s*(cl)\b', lambda match: f"{match.group(1)} centiliters", input_text, flags=re.IGNORECASE)
    input_text = re.sub(r'(\d+)\s*(l)\b', lambda match: f"{match.group(1)} liters", input_text, flags=re.IGNORECASE)
    input_text = re.sub(r'(\d+)\s*(%)\b', lambda match: f"{match.group(1)} percent", input_text, flags=re.IGNORECASE)
    return input_text


#Stage 3
def load_patterns_from_json(filename):
    with open(filename, 'r') as json_file:
        patterns_data = json.load(json_file)
    patterns = [pattern_entry["pattern"] for pattern_entry in patterns_data]
    return patterns

def remove_unnecessary_data(text, patterns_filename):
    text = " " + text
    patterns = load_patterns_from_json(patterns_filename)
    for pattern in patterns:
        text = re.sub(pattern, '', text, re.IGNORECASE)
    text = ' '.join(text.split())
    return text



    