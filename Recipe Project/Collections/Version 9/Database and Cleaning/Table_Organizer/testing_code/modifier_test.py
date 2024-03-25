import os
import sys

# Define the base directory path
base_path = os.getcwd() + "\Database and Cleaning\Table_Organizer\Ingredient_processing"

# Insert base path into sys.path
sys.path.insert(1, base_path)
import initial_check as ic


test_measurement_finder =  True
special_test = False
folder = "\Database and Cleaning\Table_Organizer\\test_cases\modifiers\general_test.csv"

if test_measurement_finder:
    ic.overall_test_modifier(os.getcwd() + folder)

"""
if special_test:
    pattern_over_head =  r'\b(\d+(?:_?\d+)?)\s*(g(?:ram)?s?)\b'
    pattern_number_over_head = 10
    match_type_over_head = True
    ic.test_pattern(pattern_over_head, pattern_number_over_head, match_type_over_head, folder)
"""