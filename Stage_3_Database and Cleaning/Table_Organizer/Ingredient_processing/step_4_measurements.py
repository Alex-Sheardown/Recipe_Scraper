# Define a regular expression pattern to match tablespoons variations
import json
import re



def load_patterns_from_json(filename):
    with open(filename, 'r') as json_file:
        patterns_data = json.load(json_file)
    if not isinstance(patterns_data, list):
        raise ValueError("Loaded JSON data is not in the expected list format")

    patterns_dict = {}
    for entry in patterns_data:
        name = entry.get("name")
        pattern = entry.get("pattern")
        if not name or not pattern:
            raise ValueError("Invalid entry in JSON data: {}".format(entry))
        if isinstance(pattern, list):
            patterns_dict[name] = pattern
        else:
            patterns_dict[name] = [pattern]
    
    return patterns_dict


def is_element_in_tuple(my_list, filter_name, portion):

    if filter_name != "self_count" or portion == -1:
        return False

    for item in my_list:
        filter_list_name, portion = item
        if filter_name == "self_count":
            if  filter_list_name == "cms" or filter_list_name == "diams":
                return True
            if  filter_list_name == "grams" or filter_list_name == "pots":
                return True
            if  filter_list_name == "kilo_grams" or filter_list_name == "pots":
                return True
            if  filter_list_name == "blocks": 
                return True

    return False


def find_measurement(text, filename):
    
    cauhgt_values = []
    cleaned_text = text
    fiter_type = ""
    filter_redundant = True
    measurement_patterns = load_patterns_from_json(filename)
    while filter_redundant:
        current_modifier = True
        for filter_name, filter in measurement_patterns.items():
                        
            hold = cleaned_text
            found_modifier, cleaned_text, portion = filter_check_specified(filter_name, cleaned_text, measurement_patterns)
            #print("filter",filter_name, "cleaned text", cleaned_text)
            
            if found_modifier and  filter_name != "self_count":
                cauhgt_values.append((filter_name, portion))
                #print("test", cleaned_text, "portion", portion, "unaltered", hold, "filter", filter_name)
                current_modifier = False
            else:
                cleaned_text = hold
        if current_modifier:
            break
    #print(6, cleaned_text)
    #filter_name = 'self_count' : r'\b'

    found_modifier, cleaned_text, portion = filter_check_specified("self_count", cleaned_text, measurement_patterns)
    #print(7, cleaned_text)
    if len(cauhgt_values) == 0 and filter_name == "self_count" and portion > -1:
        cauhgt_values.append((filter_name, portion))
        filter_redundant = False
    elif is_element_in_tuple(cauhgt_values, filter_name, portion) :
        cauhgt_values.append((filter_name, portion))
        filter_redundant = False
    

        
    #cleaned_text = remove_unecessary_data(cleaned_text)

    return cauhgt_values, cleaned_text

def quick_sub_count(text, list):

    count = 9999
    
    index = 0
    new_index = 0

    for p in list:
        cleaned_text = re.sub(p, '', text)
        #print(cleaned_text)
        new_count = len(cleaned_text)
        if count > new_count:
            count = new_count
            new_index = index

        index+=1
    

    return list[new_index]

def filter_check_specified(filter_name, text, measurement_patterns):

    #print("I am here",text)
    text = text.replace('_', ' ')
    text = text.lower()



    filter = measurement_patterns[filter_name]
    

    if filter_name == "table_spoons":
        filter = quick_sub_count(text, filter)
    elif filter_name == "tea_spoons":
        filter = quick_sub_count(text, filter)
    elif filter_name == "fluid_ounces":
        filter = quick_sub_count(text, filter)
    elif filter_name == "gallons":
        filter = quick_sub_count(text, filter)
    elif filter_name == "lbs":
        filter = quick_sub_count(text, filter)    
    elif filter_name == "milli_liters":
        filter = quick_sub_count(text, filter) 
    else:
        filter = filter[0]
    

    #milliliter_breakdown
    #print(filter)

    
    return check_portion(filter, text)

def check_portion(base_pattern, text):
    
    #text = word_to_num(text)
    proportion = -1
    #text = text.replace('_', ' ')
    #text = text.lower()
    has_pattern = False
    altered_text = text

    """
    I will need to add my own list of special cleaning
    """
   
    combined_patterns = [
        #got to fix
        #r'between_(\d+)_and_(\d+)'
        r'(\d+(?:_\d+)?(?:\.\d+)?)\s*(?:-|to|or|and)\s*(\d+(?:_\d+)?(?:\.\d+)?)\s*',
        r'(\d+\.\d+)\s*',
        r'\s*\d+\s*',
        #r'(\d+(?:_\d+)?)\s*',/^\d*\.?\d*$/
        r'a\s*few\s*',
        #r'\b(?:few)\s*',
        r'\b(?:a|an)\s*',
        
        
    ]
    #print(base_pattern)
    pattern = [base_pattern] + combined_patterns
    #print(pattern)

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
        

    return has_pattern, altered_text, float(proportion)