
import os
import pandas as pd
import Linkchecker as lc

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

if test_decimal_conversion:
    # Run the tests
    for i, (input_string, expected_output) in enumerate(test_cases2, start=1):
        input_string = lc.clean_ingredient_fraction(input_string)
        input_string = lc.clean_ingredient_characters(input_string)
        input_string = lc.clean_replace_fractions_with_decimals(input_string)

        result = lc.clean_replace_fractions_with_decimals(input_string)
        if result == expected_output:
            print(f"Test {i}: PASSED")
        else:
            print(f"Test {i}: FAILED")
            print(f"Expected: {expected_output}")
            print(f"Result:   {result}")
        print("=" * 30)


def testcases(measurement):
    
    #tablespoon_pattern
    if measurement == 1:
        name = "tablespoon_pattern"
        ingredient_strings_with_tablespoons = [
        "0_tablespoons_of olive oil",
        "1 tbsp of sugar",
        "3 TBSP of soy sauce",
        "4 tbspoons of flour",
        "5 tblsp of salt",
        "6 tbspn of honey",
        "7 tbsp. of vinegar",
        "8 tbsps of ketchup",
        "9 tbspns of mayonnaise",
        "10 tbspoons of mustard",
        "11 tblsp of Worcestershire sauce",
        "12 tbspn. of peanut butter",
        "13 table spoons of cream cheese",
        "14 table spoonsful of whipped cream",
        "15_tablespoons_of olive oil",
        "16_tbsp of sugar",
        "17_tbs.p.oon.s of soy sauce",
        "18_tbs_o_o_n_s of flour",
        "19_t_b.l_sp of salt",
        "20_t_b_spoon_s of honey",
        "21_tb_spn of vinegar",
        "22_tb_s_p_s of ketchup",
        "23_tbspns_of mayonnaise",
        "24_tbsp_o_ons of mustard",
        "25_tbl_s.p of Worcestershire sauce",
        "26_t_b_l_sp. of peanut butter",
        "27_table_ spoons of cream cheese",
        "28_table_spoons_ful of whipped cream",
        ]
        ingredient_strings_without_tablespoons = [
        "tablecloth",
        "table tennis",
        "tablet",
        "tableware",
        "staple",
        "table of contents",
        "tablets",
        "times table",
        "tableau",
        "vegetable",
        "double table",
        ]
        return [ingredient_strings_with_tablespoons , ingredient_strings_without_tablespoons], name
    #teaspoon_pattern
    elif measurement == 2:
        name = "teaspoon_pattern"
        ingredient_strings_with_teaspoons = [
        "1 teaspoon of salt",
        "2 tsps of sugar",
        "3 TSPs of cinnamon",
        "4 tsp of vanilla extract",
        "5 tsps of lemon juice",
        "6 Tsp of baking powder",
        "7_Tsp_of baking powder",
        "8_tsps_of_lemon juice",
        "9_tea_spoon of salt",
        "10_tsp.s of sugar",
        "11_T.S.P_s of cinnamon",
        "12_tsp of vanilla extract",
        "13_tsp_s of lemon juice",
        "14_Tsp of baking powder",
        "15_Tsp_of baking powder",
        "16_tsps_of_lemon juice",
        "17 teaspoon of salt",
        "18_tsp of sugar",
        "19_ts of cinnamon",
        "20_t.s.p of flour",
        "21 t s of pepper",
        "22_t_s. of honey",
        "23 t_spoons of vinegar",
        "24_tea_s.p_s of ketchup",
        "25 t.s of mayonnaise",
        "26 teaspoons of mustard",
        "27 t.s of Worcestershire sauce",
        "28_tspn of peanut butter",
        "29_t.s of cream cheese",
        "30 t_spoonsful of whipped cream",
        "31_ts of olive oil",
        "32_tsp of sugar",
        "33_ts.p.oon.s of soy sauce",
        "34_tsp_o_o_n_s of flour",
        "35_tea_s.p of salt",
        "36 t.spoon_s of honey",
        "37_t.s.pn of vinegar",
        "38 tsp_s_p_s of ketchup",
        "39_t.spoons of mayonnaise",
        "40_t.spoons of mustard",
        "41_t.s of Worcestershire sauce",
        "42 tspn. of peanut butter",
        "43 ts.p. of cream cheese",
        "44_t.spoonsful of whipped cream",
        ]
        ingredient_strings_without_teaspoons = [
            "1 tablespoons of flour",
            "2 tbspoons of honey",
            "3 tbspn of vinegar",
            "4 tablespoonsful of sugar",
            "5 tbs of olive oil",
        ]

        return [ingredient_strings_with_teaspoons, ingredient_strings_without_teaspoons], name
    #oz_pattern
    elif measurement == 3:
        name = "oz_pattern"
        ingredient_strings_with_ounces = [
        "1 ounce of chocolate chips",
        "2 oz of almonds",
        "3 OZs of cheese",
        "4 ozs of pasta",
        "5 ounce of butter",
        "6 Oz of cream",
        "7_ounce_of butter",
        "8_Oz_of cream",
        "9_ounce_of chocolate chips",
        "10_oz of almonds",
        "11_OZs of cheese",
        "12_ozs of pasta",
        "13_ounce of butter",
        "14_Oz of cream",
        "15_ounce_of butter",
        "16_Oz_of cream",
        ]
        ingredient_strings_without_ounces = [
            "1 teaspoon of salt",
            "2 tablespoons of sugar",
            "3 tbspn of vinegar",
            "4 tablespoonsful of sugar",
            "5 tbs of olive oil",
        ]
        return [ingredient_strings_with_ounces, ingredient_strings_without_ounces], name
    #fl_oz_pattern
    elif measurement == 4:
        name = "fl_oz_pattern"
        ingredient_strings_with_fluid_ounces = [
        "1 fl oz of vanilla extract",
        "2 fluid ounces of lemon juice",
        "3 fl. oz of almond milk",
        "4 fluid ounces of orange juice",
        "5 fl. oz of rum",
        "6_fluid_ounces of orange juice",
        "7_fl._oz_of rum",
        "8_fl oz_of vanilla extract",
        "9_fluid ounces_of lemon juice",
        "10_fl. oz_of almond milk",
        "11_fluid ounces_of orange juice",
        "12_fl oz_of rum",
        "13_fluid_ounces_of orange juice",
        "14_fl._oz_of rum"
        ]
        ingredient_strings_without_fluid_ounces = [
        "1 teaspoon of salt",
        "2 tablespoons of sugar",
        "3 tbspn of vinegar",
        "4 tablespoonsful of sugar",
        "5 tbs of olive oil",
        ]
        return [ingredient_strings_with_fluid_ounces, ingredient_strings_without_fluid_ounces], name
    #cup_pattern
    elif measurement == 5:
        name = "cup_pattern"
        ingredient_strings_with_cups = [
        "1 cup of flour",
        "2 cups of sugar",
        "3 c of milk",
        "4 c. of diced tomatoes",
        "5 cups of water",
        "6_c._of diced tomatoes",
        "7_cups_of water",
        "8_cup_of flour",
        "9_cups_of sugar",
        "10_c of milk",
        "11_c. of diced tomatoes",
        "12_cups_of water",
        "13_c._of diced tomatoes",
        "14_cups_of water",
        ]

        ingredient_strings_without_cups = [
        "1 teaspoon of salt",
        "2 tablespoons of honey",
        "3 tbspn of vinegar",
        "4 tablespoonsful of sugar",
        "5 tbs of olive oil",
        ]

        return [ingredient_strings_with_cups, ingredient_strings_without_cups], name
    #qt_pattern
    elif measurement == 6:
        name = "qt_pattern"
        ingredient_strings_with_quarts = [
        "1 quart of milk",
        "2 qts of soup",
        "3 QTs of apple juice",
        "4 qt of tomato sauce",
        "5 quarts of water",
        "6_qt_of tomato sauce",
        "7_quarts_of water",
        "8_quart_of milk",
        "9_qts_of soup",
        "10_QTs_of apple juice",
        "11_qt_of tomato sauce",
        "12_quarts_of water",
        "13_qt_of tomato sauce",
        "14_quarts_of water",
        ]

        ingredient_strings_without_quarts = [
            "1 teaspoon of salt",
            "2 tablespoons of honey",
            "3 tbspn of vinegar",
            "4 tablespoonsful of sugar",
            "5 tbs of olive oil",
        ]

        return [ingredient_strings_with_quarts, ingredient_strings_without_quarts], name
    #pint_pattern
    elif measurement == 7:
        name = "pint_pattern"
        ingredient_strings_with_pints = [
        "1 pint of strawberries",
        "2 pts of cream",
        "3 PTs of milk",
        "4 pt of chicken broth",
        "5 pints of water",
        "6_pt_of chicken broth",
        "7_pints_of water",
        "8_pints_of water",
        "9_PTs_of tomato soup",
        "10_pint_of heavy cream",
        "11_pts_of chocolate sauce",
        "12_PT_of chicken stock",
        "13_pt_of chicken broth",
        ]

        ingredient_strings_without_pints = [
            "1 teaspoon of salt",
            "2 tablespoons of honey",
            "3 tbspn of vinegar",
            "4 tablespoonsful of sugar",
            "5 tbs of olive oil",
        ]

        return [ingredient_strings_with_pints, ingredient_strings_without_pints], name
    #gallon_pattern
    elif measurement == 8:
        name = "gallon_pattern"
        ingredient_strings_with_gallons = [
        "1 gallon of milk",
        "2 gals of water",
        "3 gal of apple juice",
        "4 gals. of vinegar",
        "5 gallons of olive oil",
        "6_gals._of vinegar",
        "7_gallons_of olive oil",
        "8_gals_of vinegar",
        "9_gallon_of orange juice",
        "10_gals. of vegetable oil",
        "11 gallons of soy sauce",
        "12_GAL_of chocolate syrup",
        "13_GALS_of mayonnaise",
        ]

        ingredient_strings_without_gallons = [
            "1 teaspoon of salt",
            "2 tablespoons of honey",
            "3 tbspn of sugar",
            "4 tablespoonsful of flour",
            "5 tbs of lemon juice",
        ]

        return [ingredient_strings_with_gallons, ingredient_strings_without_gallons], name
    #lb_pattern
    elif measurement == 9:
        name = "lb_pattern"
        ingredient_strings_with_pounds = [
        "1 pound of beef",
        "2 lbs of chicken",
        "3 lb of pork",
        "4 lbs. of salmon",
        "5 pounds of shrimp",
        "6_lbs. of salmon",
        "7_pounds of shrimp",
        "8_pound_of butter",
        "9_lbs of ground beef",
        "10 lbs. of chicken thighs",
        "11 pound of turkey",
        "12_lbs_of pork belly",
        "13_pounds_of bacon",
        ]

        ingredient_strings_without_pounds = [
            "1 teaspoon of salt",
            "2 tablespoons of honey",
            "3 tbspn of vinegar",
            "4 tablespoonsful of sugar",
            "5 tbs of olive oil",
        ]

        return [ingredient_strings_with_pounds, ingredient_strings_without_pounds], name
    #mL_pattern
    elif measurement == 10:
        name = "mL_pattern"
        ingredient_strings_with_milliliters = [
        "1 milliliter of vanilla extract",
        "2 mLs of lemon juice",
        "3 mL of soy sauce",
        "4 mLs. of vinegar",
        "5 milliliters of olive oil",
        "6_mLs._of vinegar",
        "7_milliliters_of olive oil",
        "8_mL_of water",
        "9_mLs_of orange juice",
        "10_mLs._of vanilla_extract",
        "11_milliliters_of soy_sauce",
        "12_mL_of lemon_juice",
        "13_mLs_of milk",
        "14_mLs._of vinegar",
        ]

        ingredient_strings_without_milliliters = [
            "1 teaspoon of salt",
            "2 tablespoons of honey",
            "3 tbspn of sugar",
            "4 tablespoonsful of flour",
            "5 tbs of mayonnaise",
        ]
        return [ingredient_strings_with_milliliters, ingredient_strings_without_milliliters], name
    #g_pattern
    elif measurement == 11:
        name = "g_pattern"
        ingredient_strings_with_grams = [
        "1 gram of salt",
        "2 gs of sugar",
        "3 g of cinnamon",
        "4 gs. of flour",
        "5 grams of pepper",
        "6_gs._of flour",
        "7_grams_of pepper",
        "8_grams_of sugar",
        "9_gs_of flour",
        "10_g_of salt",
        "11_gs. of chocolate",
        "12_grams of spices",
        "13_gs._of herbs",
        "14_grams_of pepper"
        "15 grams of sugar",
        "16 g of flour",
        "17 gs of salt",
        "18 g.s of chocolate chips",
        "19 gs. of almonds",
        "20 gram of salt",
        "21 gs of sugar",
        "22 g of cinnamon",
        "23 gs. of flour",
        "24 grams of pepper",
        "25_gs._of flour",
        "26_grams_of pepper",
        "27_grams_of_sugar",
        "28_g_of_flour",
        "29_gs_of_salt",
        "30_g.s_of_chocolate_chips",
        "31_gs.of_almonds",
        "32_grams_of_sugar",
        "33_grams of_sugar",
        "34 grams_of_sugar",
        ]

        ingredient_strings_without_grams = [
            "1 teaspoon of salt",
            "2 tablespoons of honey",
            "3 tbspn of vinegar",
            "4 tablespoonsful of sugar",
            "5 tbs of olive oil",
        ]

        return [ingredient_strings_with_grams, ingredient_strings_without_grams], name
    #kg_pattern
    elif measurement == 12:
        name = "kg_pattern"
        ingredient_strings_with_kilograms = [
        "1 kilogram of rice",
        "2 kgs of sugar",
        "3 kg of flour",
        "4 kgs. of chocolate",
        "5 kilograms of pasta",
        "6_kg_of spices",
        "7_kgs_of herbs",
        "8 kilograms of meat",
        "9 kg of vegetables",
        "10 kgs. of seafood",
        "11_kg_of nuts",
        "12_kgs_of beans",
        ]

        ingredient_strings_without_kilograms = [
            "1 teaspoon of salt",
            "2 tablespoons of honey",
            "3 tbspn of vinegar",
            "4 tablespoonsful of sugar",
            "5 tbs of olive oil",
        ]
        return [ingredient_strings_with_kilograms, ingredient_strings_without_kilograms], name
    #l_pattern
    elif measurement == 13:
        name = "l_pattern"
        ingredient_strings_with_liters = [
        "1_liter_of milk",
        "2 ls of water",
        "3 l of apple juice",
        "4 ls. of vinegar",
        "5 liters of olive oil",
        "6_ls._of vinegar",
        "7_liters_of olive oil",
        "8 liters of soda",
        "9 liters of orange juice",
        "10_l_of milk",
        "11_l_of water",
        "12_l_of apple juice",
        "13_l_of vinegar",
        "14_l_of olive oil",
        "15_ls._of vinegar",
        "16_liters_of olive oil",
        "17_l._of water",
        "18_liters_of soda",
        "19_ls._of orange juice",
        "20_liters_of milk",
        ]

        ingredient_strings_without_liters = [
            "1 teaspoon_of salt",
            "2 tablespoons of honey",
            "3 tbspn of sugar",
            "4 tablespoonsful of flour",
            "5 tbs of lemon juice",
        ]

        return [ingredient_strings_with_liters, ingredient_strings_without_liters]
    else:
        return False

def test_measurements(ingredient_strings, test_for_true, measurement):
    # Initialize counters for passed and total tests
    passed_tests = 0
    total_tests = len(ingredient_strings)

    # Iterate through ingredient strings and check for tablespoons
    for ingredient_string in ingredient_strings:
        has_tablespoons = lc.find_measurments(ingredient_string, measurement)
        if test_for_true and has_tablespoons:
            passed_tests += 1
        elif not test_for_true and not has_tablespoons:
            passed_tests += 1

    # Calculate the fraction of passed tests
    pass_fraction = passed_tests / total_tests

    if test_for_true:
        message = "contains"
    else:
        message = "does not contain"

    # Print the summary with the determined message
    print(f"\nSummary: {passed_tests} out of {total_tests} tests {message} given measurements. ({pass_fraction:.2%})")


if test_measurement_finder:
    # Sample ingredient strings
    # Define the list of ingredient strings

    for i in range(1, 13):
        measurement = i
        name = ""
        
        testCase, name = testcases(measurement)
        print("")
        print(name)
        print("="*30)
        
        test_measurements(testCase[0], True, measurement)
        test_measurements(testCase[1], False, measurement)




import re
special_test = True
if special_test:
    pattern_over_head = r"(\d+(?:_\d+)?)\s*[_\s]*(?:[tT](?:ea)?[_\s]*[sS](?:[pP](?:\.(?:s|ful)?)?|\.?\s*p|\.?[sS]|\.?[pP]_[sS])?|t\s*s\.?\s*p|t\s*p\.?s|t\s*[._]?\s*[sS]\s*[._]?\s*[pP]|t\s*[._]?\s*[sS]\s*)\s*(?:of)?\s*"

    #40/44 r"(\d+(?:_\d+)?)\s*[_\s]*(?:[tT](?:ea)?[_\s]*[sS](?:[pP](?:\.(?:s|ful)?)?|\.?\s*p|\.?[sS]|\.?[pP]_[sS])?|t\s*s\.?\s*p|t\s*p\.?s|t\s*[._]?\s*[sS]\s*[._]?\s*[pP])\s*(?:of)?\s*"
    #pattern_over_head = r"(\d+(?:_\d+)?)\s*[_\s]*(?:[tT](?:ea)?[_\s]*[sS](?:[pP](?:\.(?:s|ful)?)?|\.?\s*p|\.?[sS]|\.?[pP]_[sS])?|t\s*s\.?\s*p|t\s*p\.?s)\s*(?:of)?\s*"
    #r"(\d+(?:_\d+)?)\s*(?:tea *spoon|t\s*sp(?:\.|n(?:\.|s)?)?|t\s*bl\s*sp)(?:s)?(?:\.|\s*(?:of)?\s*)" 
    #r"(?:tea *spoon|tsp(?:\.|n(?:\.|s)?)?|tblsp|t_s_p|t_spoon|tspn)(?:s)?(?:\.|\s*(?:of)?\s*)"

    pattern_number_over_head = 2
    match_type_over_head = False

    #match_type_over_head = False 

    # Test function for the tablespoon_pattern regex
    def test_pattern(pattern, pattern_number, match_type):
        # Test cases with different valid formats
        testCase, name = testcases(pattern_number)
        print("")
        print("Special: " + name)
        print("="*30)

        type_P_or_F = 1
        if match_type:
            type_P_or_F = 0
        count = 0

        for input_string in testCase[type_P_or_F]:
            # Find all matches using the simplified regex pattern
            matches = bool(re.search(pattern, input_string, re.IGNORECASE))

            if matches == match_type:
                count += 1
                #print(input_string)
            else:
                print(input_string)
        print("")
        print(count)
        print(len(testCase[type_P_or_F]))

    # Run the test function
    test_pattern(pattern_over_head, pattern_number_over_head, match_type_over_head)
