import os
import sys

# Define the base directory path
base_path = os.getcwd() + "\Database and Cleaning\Table_Organizer\Ingredient_processing"

# Insert base path into sys.path
sys.path.insert(1, base_path)
import initial_check as ic


test_measurement_finder =  True
special_test = False
folder = "measurements"

if test_measurement_finder:
    ic.overall_test_modifier(folder)

if special_test:

    base_pattern = False#r'\b(?:pint|pt)s?\.?(?:\s|$)'

    print(base_pattern)
    pattern_number_over_head = 6
    match_type_over_head = True

    
    ic.test_pattern(base_pattern, pattern_number_over_head, match_type_over_head, folder)
