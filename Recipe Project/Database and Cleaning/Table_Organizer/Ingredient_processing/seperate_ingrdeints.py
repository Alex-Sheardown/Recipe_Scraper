import re

def split_on_or_not_surrounded_by_numbers(ingredient_string):
    # Split on "or" not surrounded by numbers
    parts = re.split(r'(?<!\d)(_|\(|/)or_?\s*(?!\d)', ingredient_string, flags=re.IGNORECASE)
    parts = [part.strip() for part in parts if part.strip()]
    return parts

def split_on_and_not_surrounded_by_numbers(ingredient_string):
    # Split on "or" not surrounded by numbers
    parts = re.split(r'(?<!\d)(_|\()_and_?\s*(?!\d)', ingredient_string, flags=re.IGNORECASE)
    parts = [part.strip() for part in parts if part.strip()]
    return parts

def split_on_comma_not_surrounded_by_numbers(ingredient_string):
    # Split on "or" not surrounded by numbers
    parts = re.split(r'(?<!\d),_?\s*(?!\d)', ingredient_string, flags=re.IGNORECASE)
    parts = [part.strip() for part in parts if part.strip()]
    return parts
# Python3 program to remove invalid parenthesis 

# Method checks if character is parenthesis(open 
# or closed) 
def isParenthesis(c):
	return ((c == '(') or (c == ')')) 

# method returns true if contains valid 
# parenthesis 
def isValidString(str):
	cnt = 0
	for i in range(len(str)):
		if (str[i] == '('):
			cnt += 1
		elif (str[i] == ')'):
			cnt -= 1
		if (cnt < 0):
			return False
	return (cnt == 0)
	
# method to remove invalid parenthesis 
def removeInvalidParenthesis(str):
	if (len(str) == 0):
		return ""
		
	# visit set to ignore already visited 
	visit = set()
	
	# queue to maintain BFS
	q = []
	temp = 0
	level = 0
	
	# pushing given as starting node into queue
	q.append(str)
	visit.add(str)
	while(len(q)):
		str = q[0]
		q.pop(0)
		if (isValidString(str)):
			print(str)
			
			# If answer is found, make level true 
			# so that valid of only that level 
			# are processed. 
			level = True
		if (level):
			continue
		for i in range(len(str)):
			if (not isParenthesis(str[i])):
				continue
				
			# Removing parenthesis from str and 
			# pushing into queue,if not visited already 
			temp = str[0:i] + str[i + 1:] 
			if temp not in visit:
				q.append(temp)
				visit.add(temp)
	return str

def remove_number_after_or(text):
    # Define the regular expression pattern to find " or <number>"
    pattern = re.compile(r'\s+or\s+(\d+)')
    
    # Find the pattern in the text
    match = pattern.search(text)
    
    if match:
        # Get the captured number
        captured_number = match.group(1)
        
        # Remove the pattern from the text
        cleaned_text = pattern.sub('', text)
        
        return cleaned_text.strip(), int(captured_number)
    else:
        return text.strip(), None

"""
# Example usage:
text = "8 chicken drumsticks or 10 or a whole chicken to cut into pieces"
cleaned_text, captured_number = remove_number_after_or(text)
print("Cleaned text:", cleaned_text)
print("Captured number:", captured_number)
"""
# This code is contributed by SHUBHAMSINGH10


# Example usage:
"""
ingredient_string = "8 chicken drumsticks or 10 or a whole chicken to cut into pieces"
parts = split_on_or_not_surrounded_by_numbers(ingredient_string)
print(parts)
"""