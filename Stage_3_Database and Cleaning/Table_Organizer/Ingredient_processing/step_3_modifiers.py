import re



import re
import json

def load_patterns_from_json(filename):
    with open(filename, 'r') as json_file:
        patterns_data = json.load(json_file)
    return patterns_data

def find_modifier(text, patterns_filename):
    caught_values = []
    cleaned_text = text
    found_modifier = False
    modifier_patterns = load_patterns_from_json(patterns_filename)
    
    for pattern_entry in modifier_patterns:
        filter_name = pattern_entry["name"]
        pattern = pattern_entry["pattern"]
        found_modifier, cleaned_text = check_modifier(pattern, cleaned_text)
        if found_modifier:
            caught_values.append(filter_name)
    
    return caught_values, cleaned_text

def filter_check_specified(filter_name, text, patterns_filename):
    modifier_patterns = load_patterns_from_json(patterns_filename)
    pattern = next((entry["pattern"] for entry in modifier_patterns if entry["name"] == filter_name), None)
    if pattern:
        return check_modifier(pattern, text)
    else:
        return False, text

def check_modifier(pattern, text):
    match = re.search(pattern, text, re.IGNORECASE)
    if match:
        found_modifier = True
        cleaned_text = re.sub(pattern, '', text, re.IGNORECASE)
    else:
        found_modifier = False
        cleaned_text = text
    return found_modifier, cleaned_text
    