from step_1_general_cleaning import clean_ingredient, edge_cases, process_measurement, remove_unnecessary_data
from step_2_seperation import seperate_ingredients
from step_3_modifiers import find_modifier
from step_4_measurements import find_measurement
from step_5_touch_ups import average_same_numbers, divide_numbers_in_tuples, extract_repeated_word_or_original, remove_direct_repeats, remove_number_after_or, removeInvalidParenthesis
from step_6_conversion import create_hash


def stage_print(text, show_data, test_name):
    global stage_count
    if show_data:
        print("Stage ", str(stage_count), ":    ", text, ": ", test_name)
        stage_count = stage_count + 1

stage_count = 0
def raw_translated_ingredient(text, show_data, test_status):
    #print("I made it")
    
    patterns_filename = "G:\Code\Recipe Project\Stage_3_Database and Cleaning\Table_Organizer\\regex_holder\\"
    text, error = clean_ingredient(text)
    stage_print(text,show_data,"clean_ingredient")
    
    text = edge_cases(text)
    stage_print(text,show_data,"edge_cases")

    #This fixes abreviations of measurements
    text = process_measurement(text)
    stage_print(text,show_data,"process_measurement")

    text = remove_unnecessary_data(text, patterns_filename + "useless.json", test_status)
    stage_print(text,show_data,"remove_unnecessary_data")

    result_list = []
    text_list, multi_part_ingredient_status = seperate_ingredients(text, show_data)

    #stage_print(text,show_data)
            
    if show_data:
        print("---------")


    last_meausurement = ""
    summary_modifier, text = find_modifier(text, patterns_filename + "modifier_patterns.json", test_status)
    empty_text = False
    found_measurements_list_total = []
    for text in text_list:
        found_modifier, text = find_modifier(text, patterns_filename + "modifier_patterns.json", test_status)
        stage_print(text,show_data, "find_modifier")
        found_measurements, cleaned_text = find_measurement(text, patterns_filename + "measurement_patterns.json", test_status)
        cleaned_text = extract_repeated_word_or_original(cleaned_text)
        print(len(found_measurements))
        if len(found_measurements) != 0:
            found_measurements_list_total += [found_measurements]
        if len(cleaned_text) < 3:
            empty_text = True
            continue 
    with_split = False
    data = str(found_measurements_list_total) + " " + str(len(found_measurements_list_total))
    stage_print(data, show_data, "Count of measurement list")
    if len(found_measurements_list_total)== 1 and multi_part_ingredient_status == "with":
        stage_print("with split found",show_data, "")
        with_split = True

    
    for text in text_list:
        stage_count = 5
        ignore_this = False

        found_modifier, text = find_modifier(text, patterns_filename + "modifier_patterns.json", test_status)
        stage_print(text,show_data, "find_modifier in list")
        
        found_measurements, cleaned_text = find_measurement(text, patterns_filename + "measurement_patterns.json", test_status)
        stage_print(found_measurements,show_data, "find_measurement in list")
        stage_print(cleaned_text,show_data, "find_measurement in list")


        
        cleaned_text = extract_repeated_word_or_original(cleaned_text)
        stage_print(cleaned_text,show_data, "extract_repeated_word_or_original")
        cleaned_text = removeInvalidParenthesis(cleaned_text)
        stage_print(cleaned_text,show_data,"removeInvalidParenthesis")

        cleaned_text, captured_number = remove_number_after_or(cleaned_text)
        if captured_number != None:
            found_measurements.append(("self_count",captured_number))
        stage_print(cleaned_text,show_data,"remove_number_after_or")
        stage_print(found_measurements,show_data,"Self count add")

        #removes direct repeats
        hold = remove_direct_repeats(cleaned_text)
        while hold != cleaned_text:
            cleaned_text = hold
            hold = remove_direct_repeats(hold)

        stage_print(cleaned_text,show_data,"remove_direct_repeats")

        if len(cleaned_text) < 3:
            continue 

        #Hash creator
        hex_hash = create_hash(found_modifier, summary_modifier,empty_text)

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
    stage_count = 0
    return result_list

