import os
import sys
import initial_test as it
# Define the base directory path
base_path = os.getcwd() + "\Database and Cleaning\Table_Organizer\Ingredient_processing"

# Insert base path into sys.path
sys.path.insert(1, base_path)

import measurement_check as mc

folder = "measurements"

test_measurement_finder =  False
special_test = False

test_measurement_enhanced = True
test_smallest_filter_result = False

#In order to determine if the regex method is able to detect the right measurement 
"""
Alright seems to go in order so it should be good for next test.

We are able to clean and determine properly the aspects of the data

Now we need to run it all together
"""
remove_proper_section = False


if test_measurement_finder:
    it.overall_test_modifier(folder)

if special_test:

    base_pattern = False#r'\b(?:pint|pt)s?\.?(?:\s|$)'

    print(base_pattern)
    pattern_number_over_head = 6
    match_type_over_head = True

    
    it.test_pattern(base_pattern, pattern_number_over_head, match_type_over_head, folder)

if test_measurement_enhanced:
    folder = "\Database and Cleaning\Table_Organizer\\test_cases\measurements_cleaning\general_test.csv"
    it.overall_determine_measurement(os.getcwd() + folder)


if test_smallest_filter_result:
    text =  '2 jars of sugar'
    filter = mc.filter_check_specified("jars", text)
    
    print(filter)
    #initial_result, cleaned_text, portion = ic.check_portion(filter, text)
    #print(cleaned_text)

if remove_proper_section:
    folder = "\Database and Cleaning\Table_Organizer\\test_cases\measurements_cleaning\general_test.csv"
    it.overall_test_measurements_enhanced(os.getcwd() + folder)