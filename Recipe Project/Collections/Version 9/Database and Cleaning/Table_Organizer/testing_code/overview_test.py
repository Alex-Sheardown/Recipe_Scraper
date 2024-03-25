
import re

def find_first_number(input_string):
    # Regular expression pattern to match the first number in a string
    pattern = r'\d+'
    
    # Search for the pattern in the input string
    match = re.search(pattern, input_string)
    
    if match:
        # Extract and return the first number found
        return match.group()
    else:
        # No number found in the string
        return None
