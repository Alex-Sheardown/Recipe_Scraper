# Define a regular expression pattern to match tablespoons variations
import re
import initial_check as ic


portion_pattern = ""
tablespoon_pattern = r"(?:t ?b ?l ?sp.|tbsp|tablespoon|TBSP|tbspoons|tblsp|tbspn|tbsp\.|tbsps|tbspns|tbspoons|tblsp|tbspn\.|table\s*spoons|table\s*spoonsful|tablespoons|tbs\.p\.oon\.s|tbs\s*o\s*o\s*n\s*s|t\s*b\.l\s*sp|t\s*b\s*spo\s*o\s*n\s*s|tb\s*spn|t\s*b\s*l\s*sp\.|tb\s*s\s*p\s\s*s|tbl\s*p|t\s*b\s*l\s*sp\.\s*|tbl\s*s\.p\s*)"
teaspoon_pattern = r"(?:\btea ?spo?o?n?s?\b|t\.?s\.?p\.?s?|t\.s|tea s\.?p|\bt\s?s)" #r"\s*(?:teaspoon|tsps|T.S.P_s|tsps|\s*|t.s.p|teaspoons|t_spoons|t.s|t.spoon_s|t.spoonsful)\s*"
oz_pattern = r"(?:ounce|oz(?:\.|s)?)"
fl_oz_pattern = r"(?:fl(?:\.|uid)?[\s_]*oz|fluid[\s_]*ounce)"#r"(fl(?:\.|uid)?\s*oz|fluid\s*ounce)"
cup_pattern = r"\b[cC]\s*(ups?)?\.?\b"
qt_pattern = r"\bqu?a?r?ts?\b"
pint_pattern = r'\b(?:pint|pt)s?\.?(?:\s|$)'
gallon_pattern = r"(gallon|gal)[\s_]*(?:n(?:\.|s)?)?"
lb_pattern = r"(pound|lb|lbs|lb\.s|lbs\.)[\s_]*(?:n(?:\.|s)?)?"
mL_pattern = r"(milliliter|mL|mLs)[\s_]*(?:n(?:\.|s)?)?"
g_pattern = r'\b(grams?|g\.?s?)\b'
kg_pattern = r"\b(kilograms?|kg\.?s?\.?)\b"
#This one needs to run after table spoon
l_pattern = r'\b(liters?|ls?|l\.s|ls\.)\b'




#Not tested
#Should be run after drop glass
drops_pattern = r'\b(drops?)\b'
dash_pattern = r'\b(dash(?:es)?)\b'
dab_pattern = r'\b(dabs?)\b'
dl_pattern = r'\b(dls?)\b'
squeeze_pattern = r'\bsqueezes?\b'
clove_pattern = r'\bcloves?\b'
sprigs_pattern = r'\bsprigs?\b' #a_few_sprigs
handful_pattern = r'\bhandfuls?\b'
bunch_pattern = r'\bbunche?s?\b'
pinch_pattern = r'\bpinche?s?\b'
pats_pattern = r'\bpats?\b'
piece_pattern = r'\bpieces?\b'

#25
#little might need some work :files not made
#Move over to modifiers
little_pattern = r'\b(little|littles)\b'
knob_pattern = r'\b(knob|knobs)\b'
bit_pattern = r'\b(bit|bits)\b'

#Something we are missing
cl_pattern = r'\bcLs?\b'
slice_pattern = r'\b(slice|slices)\b'
can_pattern = r'\b(can|cans)\b'

#31
drop_glass_pattern = r'(drop glass|drop glasses)'
jar_pattern = r'(jar|jars)'
nest_pattern = r'\b(nests?\sof)\b'
no_pattern = r' no. '
pot_pattern = r'\b(pots?\sof)\b'

#36
gr_pattern = r'\s(gr|grams?)\s'
serving_pattern = r'serving(s?)'
stalk_pattern = r'stalk(s?)'
stick_pattern = r'stick(s?)'
#kg_pattern = r' kg(s?) '

#41
log_pattern = r'\slogs?\s'
leg_pattern = r'leg(s?)'
kilo_pattern = r'(kilos?|kilograms?)'
sheet_pattern = r'sheet(s?)'
strips_pattern = r'strip(s?)'

#46
brick_pattern = r'bricks?'
diam_pattern = r'diameters?'
height_pattern = r'heights?'
#no type
tile_pattern = r'tile(s?)'
#add one
some_pattern = r' some '

#51
punnet_pattern = r'punnet(s?)'
pkg_pattern = r'\s?(pkgs?|packages?|packs?)\s?'
qq_pattern = r'qq'
time_pattern = r'time(s?)'
#test
inch_pattern = r'\s?-?(inches|inch)\s?'

#56
x_pattern = r' x '
atyt_pattern = r'(according to taste| Balance the flavors| according to your taste| according to your taste preferences | Adjust the sweetness of the sauce according to taste| according to taste | adjusting the tanginess according to your taste)'
#remove
vl_pattern = r' very little '
per_person_pattern = r' per person '
heap_pattern = r' heaping spoonful'

#61
#remove
weigh_pattern = r' weighing '
cm_pattern = r'\s(cm|centimeters?)\s'
#remove
medium_pattern = r'medium'

#add this one in !
#portions_of_pattern = r'Portions of,'

# Define a function to check for tablespoons in an ingredient string
def find_measurments( measurement, ingredient_string):

    #ingredient_string = ingredient_string.replace('_', ' ')
    if measurement == 0:
        pattern = tablespoon_pattern
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 1:
        pattern = teaspoon_pattern
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 2:
        pattern = oz_pattern
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 3:
        pattern = fl_oz_pattern
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 4:
        pattern = cup_pattern
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 5:
        pattern = qt_pattern
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 6:
        pattern = pint_pattern
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 7:
        pattern = gallon_pattern
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 8:
        pattern = lb_pattern
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 9:
        pattern = mL_pattern
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 10:
        pattern = g_pattern
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 11:
        pattern = kg_pattern
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 12:
        pattern = l_pattern
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 13:
        pattern = drops_pattern
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 14:
        pattern = dash_pattern
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 15:
        pattern = dab_pattern
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 16:
        pattern = dl_pattern
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 17:
        pattern = squeeze_pattern
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 18:
        pattern = clove_pattern
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 19:
        pattern = sprigs_pattern
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 20:
        pattern = handful_pattern
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 21:
        pattern = bunch_pattern
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 22:
        pattern = pinch_pattern
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 23:
        pattern = pats_pattern
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 24:
        pattern = piece_pattern
        return ic.check_portion(pattern, ingredient_string)

    elif measurement == 26:
        pattern = knob_pattern
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 27:
        pattern = bit_pattern
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 28:
        pattern = cl_pattern
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 29:
        pattern = slice_pattern
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 30:
        pattern = can_pattern
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 31:
        pattern = drop_glass_pattern
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 32:
        pattern = jar_pattern
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 33:
        pattern = nest_pattern
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 34:
        pattern = no_pattern
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 35:
        pattern = pot_pattern
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 36:
        pattern = gr_pattern
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 37:
        pattern = serving_pattern
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 38:
        pattern = stalk_pattern
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 39:
        pattern = stick_pattern
        return ic.check_portion(pattern, ingredient_string)
    
    elif measurement == 41:
        pattern = log_pattern
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 42:
        pattern = leg_pattern
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 43:
        pattern = kilo_pattern
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 44:
        pattern = sheet_pattern
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 45:
        pattern = strips_pattern
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 46:
        pattern = brick_pattern
        return ic.check_portion(pattern, ingredient_string)
    
    elif measurement == 48:
        pattern = height_pattern
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 49:
        pattern = tile_pattern
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 50:
        pattern = some_pattern
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 51:
        pattern = punnet_pattern
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 52:
        pattern = pkg_pattern
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 53:
        pattern = qq_pattern
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 54:
        pattern = time_pattern
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 55:
        pattern = inch_pattern
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 56:
        pattern = x_pattern
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 57:
        pattern = atyt_pattern
        return ic.check_portion(pattern, ingredient_string)
   
    elif measurement == 59:
        pattern = per_person_pattern
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 60:
        pattern = heap_pattern
        return ic.check_portion(pattern, ingredient_string)
    
    elif measurement == 62:
        pattern = cm_pattern
        return ic.check_portion(pattern, ingredient_string)
    
    else:
        return False, "", -1
    

    """
    elif measurement == 25:
        pattern = little_pattern
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 40:
        pattern = kg_pattern
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 47:
        pattern = diam_pattern
        return ic.check_portion(pattern, ingredient_string)
     elif measurement == 58:
        pattern = vl_pattern
        return ic.check_portion(pattern, ingredient_string)
    elif measurement == 61:
        pattern = weigh_pattern
        return ic.check_portion(pattern, ingredient_string)
    """
    