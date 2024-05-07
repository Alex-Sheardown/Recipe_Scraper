




import re



def extract_repeated_word_or_original(s):
    # Use regular expression to match repeated words
    match = re.match(r'^\s*(\b\w+\b)\s*\1\s*$', s)

    if match:
        # If a match is found, return the repeated word
        return match.group(1)
    else:
        # If no match is found, return the original string unchanged
        return s

def average_same_numbers(data):
    # Create a dictionary to store cumulative sum and count for each unique word
    word_data = {}
    
    # Process each tuple in the input list
    for word, number in data:
        if word in word_data:
            # Update cumulative sum and count for the existing word
            word_data[word][0] += number
            word_data[word][1] += 1
        else:
            # Add a new entry for the word
            word_data[word] = [number, 1]

    # Calculate the average for each word and create a list of tuples
    averaged_data = [(word, total / count) for word, (total, count) in word_data.items()]

    return averaged_data

def divide_numbers_in_tuples(data, divisor):
    # Divide each number in the tuples by the divisor
    result = [(unit, value / divisor) for unit, value in data]
    return result

def remove_direct_repeats(text):
    # Construct the regular expression pattern to find direct repeats of any word
    pattern = re.compile(r'\b(\w+)\s+\1\b', flags=re.IGNORECASE)
    
    # Remove direct repeats of any word
    cleaned_text = re.sub(pattern, r'\1', text)
    
    return cleaned_text

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
			#print(str)
			
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


def end_clean():
     
    text  = text.replace("-", " ")
    text  = text.replace(" a ", " ")
    text  = text.replace("( )", " ")
    text  = text.replace("( )", " ")
    #experimental ()
    #text  = text.replace("(", " ")
    #text  = text.replace(")", " ")
    
    #quoutes
    text  = text.replace("“", " ")
    text  = text.replace("”", " ")
    text  = text.replace("’", "'")
    text  = text.replace("é", "e")

    
    text  = text.replace("( |", " ")
    text  = text.replace("| )", " ")
    text  = text.replace("(s)", " ")
    text  = text.replace("( s)", " ")
    text  = text.replace("(s )", " ")
    text  = text.replace("( s )", " ")
    text  = text.replace(":", " ")
    
    text = text.rstrip("()")
    text = text.lstrip()
    text = text.rstrip()
    text = text.rstrip(";")
    text = text.lstrip("\\")
    text = text.lstrip("/")
    text = text.rstrip(".")
    text = text.lstrip(".")
    text = text.lstrip(",")
    
    #text = text.lstrip("a ")
    text = text.lstrip()
    text = text.rstrip()
    #interesting 
    #text = text.rstrip("and")
    text = text.rstrip()
    text  = ' '.join(text.split())
    return text