






import re


def split_on_or_not_surrounded_by_numbers(ingredient_string):
    # Split on "or" not surrounded by numbers
    parts = re.split(r'(?<!\d)(\s*|_|\(|/)or_?\s*(?!\d)', ingredient_string, flags=re.IGNORECASE)
    parts = [part.strip() for part in parts if part.strip()]
    return parts

def split_on_and_not_surrounded_by_numbers(ingredient_string):
    # Split on "or" not surrounded by numbers
    parts = re.split(r'(?<!\d)(\s*|_|\(|/)_(and|add)_?\s*(?!\d)', ingredient_string, flags=re.IGNORECASE)
    parts = [part.strip() for part in parts if part.strip()]
    return parts

def split_on_comma_not_surrounded_by_numbers(ingredient_string):
    # Split on "or" not surrounded by numbers
    parts = re.split(r'(?<!\d),_?\s*(?!\d)', ingredient_string, flags=re.IGNORECASE)
    parts = [part.strip() for part in parts if part.strip()]
    return parts


def seperate_ingredients(text, show_data):
      
    old_status = "NA"
    multi_part_ingredient_status = "comma"
    text_list = split_on_comma_not_surrounded_by_numbers(text)
    if show_data:
        print("comma    :", text_list)
    if len(text_list) == 1:
        #print("check 3")
        multi_part_ingredient_status = "NA"
    else:
        old_status = "comma"

    

    text_list_a = []
    multi_part_ingredient_status = "or"
    for tl in text_list:
        text_list_a+=split_on_or_not_surrounded_by_numbers(tl)

    if len(text_list_a) == len(text_list):
        multi_part_ingredient_status = old_status
    else:
        old_status = "or"

    if show_data:
        print("or       :", text_list_a)

    
    text_list_b = []
    multi_part_ingredient_status = "and"
    for tl in text_list_a:
        text_list_b+=split_on_and_not_surrounded_by_numbers(tl)

    if len(text_list_a) == len(text_list_b):
        multi_part_ingredient_status = old_status
    else:
        old_status = "and"
    if show_data:
        print("and      :", text_list_b)

    if "with" in text:
        multi_part_ingredient_status = "with"

    return text_list_b, multi_part_ingredient_status