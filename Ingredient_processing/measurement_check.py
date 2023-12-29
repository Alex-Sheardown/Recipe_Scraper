# Define a regular expression pattern to match tablespoons variations
import re
import initial_check as ic

table_spoon_breakdown = [
    r"(?:tbsps?|TBSP\s*S|tbsps?\.)\b",
    r"(?:t ?b ?l ?sp.|tblsp|tbspn|tbsps|tbspns|tblsp|tbspn\.|tbl\s*p|tbl\s*s\.p\s*)\b",
    r"(?:t\s*b\s*l\s*sp\.\s*)\b",
    r"(?:\s*tablespoons?\s*)\b",
    r"(?:\s*tbspoons?\s*)\b",
    r"(?:\s*table\s*spoons?\s*)\b",
    r"(?:\s*table\s*spoonsfuls?)\b",
    r"(?:\s*tablespoons?)\b",
    r"(?:\s*tbs\.p\.oon\.s)\b",
    r"(?:\s*tbs\s*o\s*o\s*n\s*s?)\b",
    r"(?:\s*t\s*b\.l\s*sps?)\b",
    r"(?:\s*tb\s*spns?)\b",
    r"(?:\s*t\s*b\.l\s*sps?)\b",
    r"(?:\s*tb\s*s\s*p\s?\s*s)\b",
    r"(\s*tbs\s*o\so\sn\ss?)\b",

    r"(\s*t\.b\.s\.p\s*s)\b",

    r"(\s*tbsp\s*o\s*ons)\b",
    r"(\s*table\s*spoonss\s*ful)\b",
    r"(\s*t\s*b\s*spoon\s*s)\b"


  
]

tea_spoon_breakdown = [

    r"(?:t\.?s\.?p\.?\s*s?)",
    r"(?:t\.s)",
    r"(?:\btea ?spo?o?n?s?\b)",
    r"(?:|t\.?s\.?p\.?s?)",
    r"(?:tea s\.?p)",
    r"(?:\bt\s?s)",
    r"\s*(?:teaspoon)\b",
    r"\s*(?:tsps)\b",
    r"\s*(?:T.S.P_s)\b",
    r"\s*(?:teaspoons)\b",
    r"\s*t_spoons\b",
    r"\s*(?:t\s*spoons)\b",
    r"\s*(?:tea\s*s\.p\s*s)\b",
    r"\s*(?:tspn)\b",
    r"\s*(?:ts\.p\.oon\.s)\b",
    r"\s*(?:tsp\s*o\s*o\s*n\s*s)\b",
    r"\s*(?:t\.spoon\s*s)\b",
    r"\s*(?:t\.s\.pn)\b",
    r"\s*(?:t\.spoons)\b",
    r"\s*(?:tspn\.)\b",
    r"\s*(?:t\s*spoonsful)\b",
    r"\s*(?:tsp\s*s\s*p\s*s)\b",
    r"\s*(?:t\.spoonsful)\b"

]

gallon_breakdown = [

]

lbs_breakdown = [
    r"(pound|lb)[\s_]*(?:n(?:\.|s)?)?\b",
    r"lbs\b",
    r"lbs\.\b",
    r"pounds\b"
]

fluid_ounce_breakdown = [
    r"(?:fl(?:\.|uid)?[\s_]*oz|fluid[\s_]*ounce)\b",
    r"\s*(?:fluid\s*ounces)\b"
]

gallon_breakdown = [
    r"\b(gallon|gal)[\s_]*(?:n(?:\.|s)?)?\b",
    r"\b(gallons|gals)[\s_]*(?:n(?:\.|s)?)?\b",
    r"\bgals\.\b",
]

milliliter_breakdown = [
    r"\bmilliliter\b",
    r"\bmilliliters\b",
    r"\bml\b",
    r"\bmls\b",
    r"\bmls\.\b"


]

measurement_patterns = {
    #must be before cups
    'tea_cups':r'\btea\*cups?\b',
    
    #normal
    'table_spoons'  : 1,
    'tea_spoons'    : 2,
    'fluid_ounces'  : 3,#r"(fl(?:\.|uid)?\s*oz|fluid\s*ounce)"
    'ounces'        : r"\b(?:ounce|oz(?:\.|s)?)\b",
    
    'cups'          : r"\b[cC]\s*(ups?)?\.?\b",
    'quarts'        : r"\bqu?a?r?ts?\b",
    'pints'     : r'\b(?:pint|pt)s?\.?(?:\s|$)',
    'gallons'   : 4,
    'lbs'       : 5,
    'milli_liters'  : 6,
    
    'kilo_grams'    : r"\b(kilo\s*grams?|kilos?|kgs?)\b",
    'grams'     : r'\b(grams?|g\.?s?)\b',
    #This one needs to run after table spoon
    'liter' : r'\b(liters?|ls?|l\.s|ls\.)\b',




    #Not tested
    #Should be run after drop glass
    'drops'     : r'\b(drops?)\b',
    'dashes'    : r'\b(dash(?:es)?)\b',
    'dabs'      : r'\b(dabs?)\b',
    'deciliter' : r'\b(dls?|deciliters?)\b',
    'squeezes'  : r'\bsqueezes?\b',
    'cloves'    : r'\bcloves?\b',
    'sprigs'    : r'\bsprigs?\b', #a_few_sprigs
    'handfuls'   : r'\bhandfuls?\b',
    'bunches'     : r'\bbunche?s?\b',
    'pinches'     : r'\bpinche?s?-?\s*',
    'pats'      : r'\bpats?\b',
    'pieces'     : r'\bpieces?\b',

    #25
    #little might need some work :files not made
    #Move over to modifiers
    'little'    : r'\b(little|littles)\b',
    'knobs'      : r'\b(knob|knobs)\b',
    'bits'       : r'\b(bit|bits)\b',

    #Something we are missing
    'centiliters'    : r'\b(cls?|centiliters?)\b',
    'slices' : r'\b(slice|slices)\b',
    'cans'   : r'\b(can|cans)\b',

    #31
    'drop_glasses'    : r'\b(drop glasses|drop glass)\b',
    'jars'           : r'\b(jars?)\b',
    'nests'          : r'\bnests?\b',
    'no.s'            : r'\bno\.?',
    'pots'           : r'\bpots?\b',

    #36
    #'gr'        : r'\b(gr|grams?)\b',
    'servings'   : r'\bservings?\b',
    'stalks'     : r'\bstalks?\b',
    'sticks'     : r'\bsticks?\b',
    #kg' = r' kg(s?) '

    #41
    'logs'       : r'\blogs?\b',
    'legs'       : r'\blegs?\b',
    'kilos'      : r'\b(kilos?|kilograms?)\b',
    'sheets'     : r'\bsheets?\b',
    'strips'    : r'\bstrips?\b',

    #46
    'bricks'  : r'\bbricks?\b',
    'diams'   : r'\b(in)?\s*diameters?\b',
    'heights' : r'\b(in)?\s*height\s*',
    #no type
    'tiles' : r'\btiles?\b',
    #add one
    'somes' : r'\bsome\b',

    #51
    'punnets' : r'\bpunnets?\b',
    'pkgs' : r'\b(pkgs?|packages?|packets?|packs?)\b',
    'qqs' : r'\b(qq|quintals?)\b',
    'times' : r'\btimes?\b',
    #test
    'inchs' : r'\s*-?(inches|inch)\b',

    #56
    'xs' : r'\bx\b',
    'atyts' : r'\b(according to taste| Balance the flavors| according to your taste| according to your taste preferences | Adjust the sweetness of the sauce according to taste| according to taste | adjusting the tanginess according to your taste)\b',
    #remove
    'vls' : r'\bvery\blittle\b',
  

    #61
   
   
    'cms' : r'\s*-?(cm|centimeters?)\b',
   
    'per_persons' : r'\bper\s*persons?\b',
    'heaping_spoonfuls' : r'\s*heaping\s*spoonfuls?\b',
    #'weights' : r'\s*weighting\s*',
    #not tested
    'bags'  : r'\bbags?\b',
    'boxes'  : r'\bboxe?s?\b',
    'heaped'  : r'\bheaped\b',

    #needs to be last
    'self_count' : r'\b'

}

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

    return False




def find_modifier_complete(text):
    
    cauhgt_values = []
    cleaned_text = text

    fiter_type = ""

    filter_redundant = True

    while filter_redundant:
        current_modifier = True
        for filter_name, filter in measurement_patterns.items():
                        
            hold = cleaned_text
            found_modifier, cleaned_text, portion = filter_check_specified(filter_name, cleaned_text)
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
    found_modifier, cleaned_text, portion = filter_check_specified("self_count", cleaned_text)
    #print(7, cleaned_text)
    if len(cauhgt_values) == 0 and filter_name == "self_count" and portion > -1:
        cauhgt_values.append((filter_name, portion))
        filter_redundant = False
    elif is_element_in_tuple(cauhgt_values, filter_name, portion) :
        cauhgt_values.append((filter_name, portion))
        filter_redundant = False
        

    cleaned_text = ic.remove_unecessary_data(cleaned_text)
    return cauhgt_values, cleaned_text

#going to need advance method for findign based off largest removal
def find_modifier(text):
    
    cauhgt_values = []
    cleaned_text = text

    fiter_type = ""


    for filter_name, filter in measurement_patterns.items():
        
        found_modifier, cleaned_text, portion = filter_check_specified(filter_name, cleaned_text)
    
        if found_modifier:
            fiter_type = filter_name
            break



    return fiter_type
       
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

def filter_check_specified(filter_name, text):

    #print("I am here",text)
    text = text.replace('_', ' ')
    text = text.lower()



    filter = measurement_patterns[filter_name]

    if filter == 1:
        filter = quick_sub_count(text, table_spoon_breakdown)
    elif filter == 2:
        filter = quick_sub_count(text, tea_spoon_breakdown)
    elif filter == 3:
        filter = quick_sub_count(text, fluid_ounce_breakdown)
    elif filter == 4:
        filter = quick_sub_count(text, gallon_breakdown)
    elif filter == 5:
        filter = quick_sub_count(text, lbs_breakdown)    
    elif filter == 6:
        filter = quick_sub_count(text, milliliter_breakdown) 
    

    #milliliter_breakdown
    #print(filter)

    
    return ic.check_portion(filter, text)

  




    



#add this one in !
#portions_of' = r'Portions of,'
"""
# Define a function to check for tablespoons in an ingredient string
def find_measurments( measurement, ingredient_string):

    #ingredient_string = ingredient_string.replace('_', ' ')
    if measurement == 0:
        pattern = tablespoon'
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 1:
        pattern = teaspoon'
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 2:
        pattern = oz'
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 3:
        pattern = fl_oz'
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 4:
        pattern = cup'
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 5:
        pattern = qt'
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 6:
        pattern = pint'
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 7:
        pattern = gallon'
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 8:
        pattern = lb'
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 9:
        pattern = mL'
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 10:
        pattern = g'
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 11:
        pattern = kg'
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 12:
        pattern = l'
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 13:
        pattern = drops'
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 14:
        pattern = dash'
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 15:
        pattern = dab'
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 16:
        pattern = dl'
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 17:
        pattern = squeeze'
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 18:
        pattern = clove'
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 19:
        pattern = sprigs'
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 20:
        pattern = handful'
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 21:
        pattern = bunch'
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 22:
        pattern = pinch'
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 23:
        pattern = pats'
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 24:
        pattern = piece'
        return ic.check_portion(pattern, ingredient_string)

    elif measurement == 26:
        pattern = knob'
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 27:
        pattern = bit'
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 28:
        pattern = cl'
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 29:
        pattern = slice'
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 30:
        pattern = can'
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 31:
        pattern = drop_glass'
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 32:
        pattern = jar'
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 33:
        pattern = nest'
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 34:
        pattern = no'
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 35:
        pattern = pot'
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 36:
        pattern = gr'
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 37:
        pattern = serving'
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 38:
        pattern = stalk'
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 39:
        pattern = stick'
        return ic.check_portion(pattern, ingredient_string)
    
    elif measurement == 41:
        pattern = log'
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 42:
        pattern = leg'
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 43:
        pattern = kilo'
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 44:
        pattern = sheet'
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 45:
        pattern = strips'
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 46:
        pattern = brick'
        return ic.check_portion(pattern, ingredient_string)
    
    elif measurement == 48:
        pattern = height'
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 49:
        pattern = tile'
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 50:
        pattern = some'
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 51:
        pattern = punnet'
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 52:
        pattern = pkg'
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 53:
        pattern = qq'
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 54:
        pattern = time'
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 55:
        pattern = inch'
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 56:
        pattern = x'
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 57:
        pattern = atyt'
        return ic.check_portion(pattern, ingredient_string)
   
    elif measurement == 59:
        pattern = per_person'
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 60:
        pattern = heap'
        return ic.check_portion(pattern, ingredient_string)
    
    elif measurement == 62:
        pattern = cm'
        return ic.check_portion(pattern, ingredient_string)
    
    else:
        return False, "", -1
    

    """
