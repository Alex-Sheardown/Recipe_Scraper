
import os
import re
import sys
import pandas as pd



base_path = os.getcwd() + "\Database and Cleaning\Table_Organizer\Ingredient_processing"

# Insert base path into sys.path
sys.path.insert(1, base_path)
import initial_check as ic


# Define the directory path
directory_path = os.getcwd() + "\Database and Cleaning\Table_Organizer\Ingredient_processing"

# Insert the directory path into sys.path
sys.path.insert(1, directory_path)

# Import the required module
import measurement_check as mc
import modifier_check as modc


test_decimal_conversion = False
test_measurement_finder = True


test_cases1 = [
    ("This is ⅒ of a whole.", "this is 0.1 of a whole."),  # Test 1
    ("1 ⅓ cups of sugar", "1.3333333333333333 cups of sugar"),  # Test 2
    ("2 ½ teaspoons of salt", "2.5 teaspoons of salt"),  # Test 3
    ("⅗ of the pie", "0.6 of the pie"),  # Test 4
    ("3 ⅝ hours", "3.625 hours"),  # Test 5
    ("⅙ of a pizza", "0.16666666666666666 of a pizza"),  # Test 6
    ("4 ¾ miles", "4.75 miles"),  # Test 7
    ("⅞ of the cake", "0.875 of the cake"),  # Test 8
    ("⅓ cup of flour", "0.3333333333333333 cup of flour"),  # Test 9
    ("2 ¼ pounds of apples", "2.25 pounds of apples"),  # Test 10
    ("¾ teaspoon of salt", "0.75 teaspoon of salt"),  # Test 11
    ("5 ⅝ meters of fabric", "5.625 meters of fabric"),  # Test 12
    ("⅛ of the pizza", "0.125 of the pizza"),  # Test 13
    ("3 ⅞ hours", "3.875 hours"),  # Test 14
    ("⅕ of a cake", "0.2 of a cake"),  # Test 15
    ("1 ⅝ inches", "1.625 inches"),  # Test 16
    ("⅙ of a pie", "0.16666666666666666 of a pie"),  # Test 17
    ("4 ⅕ tablespoons of sugar", "4.2 tablespoons of sugar"),  # Test 18
    ("⅜ of the cookies", "0.375 of the cookies"),  # Test 19
    ("7 ⅓ ounces of chocolate", "7.333333333333333 ounces of chocolate"),  # Test 20
    ("⅞ of the cake", "0.875 of the cake"),  # Test 21
    ("9 ½ cups of coffee", "9.5 cups of coffee"),  # Test 22
    ("⅗ of a pizza", "0.6 of a pizza"),  # Test 23
    ("12 ⅝ yards of fabric", "12.625 yards of fabric"),  # Test 24
    ("⅝ of a cake", "0.625 of a cake"),  # Test 25
    ("10 ⅓ tablespoons of flour", "10.333333333333334 tablespoons of flour"),  # Test 26
    ("⅓ of a pound of cheese", "0.3333333333333333 of a pound of cheese"),  # Test 27
    ("2 ⅛ cups of milk", "2.125 cups of milk"),  # Test 28
    ("⅞ of a pizza", "0.875 of a pizza"),  # Test 29
    ("3 ⅜ teaspoons of salt", "3.375 teaspoons of salt"),  # Test 30
    ("⅕ of a pie", "0.2 of a pie"),  # Test 31
    ("5 ⅝ pounds of apples", "5.625 pounds of apples"),  # Test 32
    ("⅙ of a gallon of juice", "0.16666666666666666 of a gallon of juice"),  # Test 33
]
test_cases2 = [
    ("⅒ of a whole.", "0.1 of a whole."),  # Test 1
    ("1 ⅓ cups of sugar", "1.3333333333333333 cups of sugar"),  # Test 2
    ("2 ½ teaspoons of salt", "2.5 teaspoons of salt"),  # Test 3
    ("⅗ of the pie", "0.6 of the pie"),  # Test 4
    ("3 ⅝ hours", "3.625 hours"),  # Test 5
    ("⅙ of a pizza", "0.16666666666666666 of a pizza"),  # Test 6
    ("4 ¾ miles", "4.75 miles"),  # Test 7
    ("⅞ of the cake", "0.875 of the cake"),  # Test 8
    ("⅝ of a cake", "0.625 of a cake"),  # Test 9
    ("10 ⅓ tablespoons of flour", "10.333333333333334 tablespoons of flour"),  # Test 10
    ("⅓ of a pound of cheese", "0.3333333333333333 of a pound of cheese"),  # Test 11
    ("2 ⅛ cups of milk", "2.125 cups of milk"),  # Test 12
    ("⅞ of a pizza", "0.875 of a pizza"),  # Test 13
    ("3 ⅜ teaspoons of salt", "3.375 teaspoons of salt"),  # Test 14
    ("⅕ of a pie", "0.2 of a pie"),  # Test 15
    ("5 ⅝ pounds of apples", "5.625 pounds of apples"),  # Test 16
    ("⅙ of a gallon of juice", "0.16666666666666666 of a gallon of juice"),  # Test 17
    ("⅓ ⅖ ⅗ ⅘ ⅙ ⅐ ⅛ ⅑ ⅒", "0.3333333333333333 0.4 0.6 0.8 0.16666666666666666 0.14285714285714285 0.125 0.1111111111111111 0.1"),  # Test 18
    ("1 ⅜ 2 ½ 3 ⅝ 4 ¾ 5 ⅝ 6 ⅞ 7 ⅐ 8 ⅛ 9 ⅑ 10 ⅒", "1.375 2.5 3.625 4.75 5.625 6.875 7.142857142857143 8.125 9.11111111111111 10.1"),  # Test 19
    ("⅛ ⅛ ⅛ ⅛ ⅛ ⅛ ⅛ ⅛ ⅛ ⅛ ⅛ ⅛ ⅛ ⅛ ⅛ ⅛ ⅛ ⅛", "0.125 0.125 0.125 0.125 0.125 0.125 0.125 0.125 0.125 0.125 0.125 0.125 0.125 0.125 0.125 0.125 0.125 0.125"),  # Test 20
]


#Test builders
def find_test_set_info(file):
    directory_path = os.getcwd()  # Current directory
    directory_path += "\Database and Cleaning\Table_Organizer\\test_cases\\" + file
    #print(directory_path)
    
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
    
def compare_and_categorize_mod(row):
    #print(modc.find_modifier(row['original'], row['modifier']))
    initial_result, cleaned_text = mc.filter_check_specified(row['modifier'], row['original'])
    #found_modifier, cleaned_text = initial_result
    #print("altered  :", row['altered'])
    #print("result   :", cleaned_text)
    if cleaned_text == row['altered']:
        return 'success'
    else:
        return 'failure'
        
def cleaned_test_mod(row):
    initial_result, cleaned_text = modc.filter_check_specified(row['modifier'], row['original'])
    #found_modifier, cleaned_text = initial_result
    return cleaned_text

def overall_test_modifier(folder):
    #G:\Code\Machine Learning\Recipe Project\Database and Cleaning\Table_Organizer\test_cases\modifiers
    #print(folder)
    data = pd.read_csv(folder)
    data['Result'] = data.apply(compare_and_categorize_mod, axis=1)
    data['altered_result'] = data.apply(cleaned_test_mod, axis=1)
    success_count = data['Result'].value_counts().get('success', 0)
    print(f'Success Cases: {success_count}')

    failure_cases = data[data['Result'] == 'failure']
    print('Failure Cases:')
    print(failure_cases)

def compare_and_categorize_measurements(row):
    #print(modc.find_modifier(row['original'], row['modifier']))
    initial_result, cleaned_text, portion = mc.filter_check_specified(row['modifier'], row['original'])
    #found_modifier, cleaned_text = initial_result
    #print("altered  :", row['altered'])
    #print("result   :", cleaned_text)
    if len(cleaned_text) == len(str(row['altered'])) and len(str(row['altered'])) == 0:
        return 'success'
    elif cleaned_text == row['altered']:
        return 'success'
    else:
        return 'failure'
    
def cleaned_test_ing_text(row):
    initial_result, cleaned_text, portion = mc.filter_check_specified(row['modifier'], row['original'])
    
    #found_modifier, cleaned_text = initial_result
    return cleaned_text

def cleaned_test_ing_proportion_result(row):
    initial_result, cleaned_text, portion = mc.filter_check_specified(row['modifier'], row['original'])
    if portion == row['portion']:
        return 'success'
    else:
        return 'failure'
    #found_modifier, cleaned_text = initial_result
    
def cleaned_test_ing_proportion(row):
    initial_result, cleaned_text, portion = mc.filter_check_specified(row['modifier'], row['original'])
    return portion
    #found_modifier, cleaned_text = initial_result
    
def find_measurement_test_result(row):
    measurement_type = mc.find_modifier(row['original'])
    if measurement_type == row['modifier']:
        return 'success'
    else:
        return 'failure'
    
def find_measurement_test(row):
    measurement_type = mc.find_modifier(row['original'])
    return measurement_type

def overall_test_measurements_enhanced(folder):
    #G:\Code\Machine Learning\Recipe Project\Database and Cleaning\Table_Organizer\test_cases\modifiers
    #print(folder)
    data = pd.read_csv(folder)
    
    data['Result'] = data.apply(compare_and_categorize_measurements, axis=1)
    data['altered_result'] = data.apply(find_measurement_test, axis=1)
    success_count = data['Result'].value_counts().get('success', 0)
    print(f'Success Cases: {success_count}')

    failure_cases = data[data['Result'] == 'failure']
    print('Failure Cases:')
    print(failure_cases)

    failure_cases.to_csv('ingredient_test_find modifier.csv')

def overall_determine_measurement(folder):
    #G:\Code\Machine Learning\Recipe Project\Database and Cleaning\Table_Organizer\test_cases\modifiers
    #print(folder)
    data = pd.read_csv(folder)
    
    data['Result'] = data.apply(compare_and_categorize_measurements, axis=1)
    data['altered_result'] = data.apply(cleaned_test_ing_text, axis=1)
    data['found_portion'] = data.apply(cleaned_test_ing_proportion, axis=1)
    data['portion_result'] = data.apply(cleaned_test_ing_proportion_result, axis=1)
    
    success_count = data['Result'].value_counts().get('success', 0)
    print(f'Success Cases: {success_count}')

    failure_cases = data[data['Result'] == 'failure']
    print('Failure Cases:')
    print(failure_cases)

    failure_cases.to_csv('ingredient_test_measurement_test.csv')

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


def overall_test(folder):
    info = find_test_set_info(folder)
    for i in range(55, 64): # len(info)
        measurement, positive_test_case, false_test_case, portion_case =  create_seperation(i, info)
        print("")
        print(measurement, i)
        print("="*30)

        #test_pattern(base_pattern, pattern_number_over_head, match_type_over_head, folder)

        
        test_pattern(False, i, True, folder)
        test_pattern(False, i, False, folder)
        #input("next batch")

def test_pattern(given_pattern, pattern_number, match_type, folder):
        
        # Test cases with different valid formats
        info = find_test_set_info(folder)
        name, positive_test_case, false_test_case, number_cases =  create_seperation(pattern_number, info)
        testCase = [ positive_test_case, false_test_case]
        print("")
        print(str(match_type), name)
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
            has_measurement = ""
            altered_text = ""
            found_number= ""
            if given_pattern == False:
                #print("I am running")
                has_measurement, altered_text, found_number = mc.find_measurments(pattern_number, input_string)
            else:
                has_measurement, altered_text, found_number = ic.check_portion(given_pattern, input_string)
            
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

        print("")
        print(passed_tests)
        print(len(testCase[type_P_or_F]))
        print("")

def compare_and_categorize_mod(row):
    #print(modc.find_modifier(row['original'], row['modifier']))
    initial_result, cleaned_text = mc.filter_check_specified(row['modifier'], row['original'])
    #found_modifier, cleaned_text = initial_result
    #print("altered  :", row['altered'])
    #print("result   :", cleaned_text)
    if cleaned_text == row['altered']:
        return 'success'
    else:
        return 'failure'
    