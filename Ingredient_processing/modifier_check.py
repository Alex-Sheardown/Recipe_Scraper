import re
import initial_check as ic

modifier_patterns = {
    #General can be added anywhere so not specific enoguh 

    #not need words
    #"of" :r'\s*of\s*',

    "very": r'\s*very\b',
    "not":  r'\s*not\b',#not_too_ # not in ? # check seperatly with list perhaps
    "too":  r'\s*too\b',

    "freeze":r'\s*freeze\b',
    "purchased":r'\s*purchased\b',

    "just": r'\s*just\b', # not pattern should just be the one pattern just ripe 
    "without": r'\s*without\b',
    #"freshly": r'\s*mini\s*\b',
    "nice": r'\s*nice\b',

    "preferably": r'\s*(preferably|preferable)\b',

    #remove not very useful
    #"tooth": r'\s*mini\s*\b',

    #sizes
    "mini": r'\s*mini\b',
    "small": r'\s*small\b',
    "little": r'\s*little\b', #little variation?
    "medium": r'\s*(medium|med)\b',
    "large": r'\s*large\b',
    "plump": r'\s*plump\b',

    #ripe
    "ripe": r'\s*ripe\b',
    "overripe": r'\s*overripe\b',


    #sweet (can be affected by the not, very and tooth)
    "sweet": r'\s*sweet\b', # not pattern
    # quality description generally of when bought
    "natural": r'\s*natural\b', # not pattern
    "quality": r'\s*quality\b', # not pattern
    "new": r'\s*new\b', # not pattern
    "organic": r'\s*organic\b', # not pattern #still_organic_pattern = r'And still organic!'
    "frozen": r'\s*(previously)?\s*frozen\b', # not pattern
    "matured": r'\s*matured\b', # not pattern
    "seeded": r'\s*seeded\b',# not pattern
    "pitted": r'\s*pitted\b',# not pattern
    "shavings": r'\s*shavings\b',# not pattern
    "raw": r'\s*raw\b',
    "soft": r'\s*soft\b',
    "dried": r'\s*dried\b',
    #"freeze_dried": r'\s*(not\s*to)?\s*ripe\b',
    "spicy": r'\s*spicy\b',
    "creamy":  r'\s*creamy\b',
    "fragrant": r'\s*fragrant\b',
    "stale": r'\s*stale\b',
    "strong": r'\s*strong\b',
    "light": r'\s*light\b',
    "heavy": r'\s*heavy\b',
    "crystallized" : r'\s*crystallized\b',


    #the un group not finished
    "untreated" : r'\s*untreated\b',
    "unpeeled" : r'\s*unpeeled\b',
    "unrefined" : r'\s*unrefined\b',

    "degerminated" : r'\s*degerminated\b',
    "defatted" : r'\s*defatted\b',
    "desalinated": r'\s*desalinated\b',
    "deboned": r'\s*deboned\b',

    "rinsed": r'\s*rinsed\b',

    "without_anti_caking_agent": r'\s*without\s*anti\s*caking\s*agent\b',
    
    "skewered": r'\s*skewered\b',#skewers
    "on_the_bone": r'\s*on\s*the\s*bone\b',
    "naturally_salted": r'\s*naturally\s*salted\b',
    "semi_salted": r'\s*semi\s*salted\b',
    "crushed": r'\s*crushed\b',

    #Season sub section
    "season": r'\s*(in)?\s*season(al)?\b', # not pattern many varitions
    """
    in_season_pattern = r'In '#season
    if_in_season_pattern = r'If it\'s in season'
    seasonal_pattern = r'Seasonal'
    """


    "sweet": r'\s*(not\s*to)?\s*ripe\b', # not pattern
    

    "phosphate_free": r'\s*phosphate\s*free\b',
    "molds_with_removable_bases": r'\s*trees?\s*molds?\s*with\s*the?\s*removable?\s*base\b',
    #how bought sub section
    "sold_in_bags": r'\s*sold\s*in\s*bags\b',
    "vacuum_packed": r'\s*vacuum\s*packed\b',

    #basic step for after bought
    "melted": r'\s*melted\b',
    "mashed": r'\s*mashed\b',
    "peeled": r'\s*\speeled\b',
    "steamed": r'\s*steamed\b',
    "diced": r'\s*diced\b',
    "minced": r'\s*minced\b',
    "shredded": r'\s*shredded\b',
    
    "flaked": r'\s*flaked\b',
    "soaked": r'\s*soaked\b',
    "boiled": r'\s*boiled\b',
    "chopped": r'\s*chopped\b',
    "mixed": r'\s*mixed\b',
    "crispy": r'\s*crispy\b',
    "ball": r'\s*balls?\b',

    "finely_cut" : r'\s*finely\s*cut',
    "thinly_sliced" :r'\s*thinly\s*sliced\b',
    "sliced" :r'\s*slice?d?\b',



    "grated": r'\s*grated\b',
    "ground": r'\s*ground\b', #r'\s*freshly\s*ground\s*flavor\b'
    "smoked": r'\bsmoked\b',


    "keep_the_water_inside" : r'\s*keep\s*the\s*water\s*inside\b',
    "in_the_oven_remove" : r'\s*(in)?\s*(the)?\s*oven\s*remove\b',

    
    "well_done": r'\s*well\s*done\b',
    "leftover": r'\s*left\s*over\b',
    "pricked": r'\s*pricked\b',
    "oven_roasted": r'\s*oven\s*roasted\b',
    "homemade": r'\s*home\s*made\b',
    "pan_fried": r'\s*pan\s*fried\b',
    "fir_trees_shape": r'\s*(in)?\s*fir\s*trees?\s*shaped?\b',
    "long_and_quite_thin": r'\s*(that)?\s*(are)?\s*long\s*and\s*quite\s*thin\b',

    #More complicated prep
    "broken_with_rolling_pin": r'\s*broken\s*(into)?\s*(pieces)?\s*with\s*(the)?\s*rolling\s*pin\b',
    #over here got to get specific
    "rolled_with_rolling_pin" : r'\s*rolled\s*with\s*rolling\s*pin\b',
    "rolled_into" : r'\s*rolled\s*into\s*(rectangles|circles)\b',
    
    #"cut_into_sticks" : r'\s*cut\s*into\s*sticks\b',
    "cut"  : r'\s*cut\b',
    "cubes"     :r'\s*cubes?\b',
    "quarters"  :r'\s*quarters?\b',
    "strips"    :r'\s*strips?\b',
    "pieces"    : r'\s*pieces?\b',
    #two\s*sections
    "sections"  :r'\s*sections?\b',
    "slices"    :r'\s*slices?\b',
    "fine_julienne"   :r'\s*fine\s*juliennes?\b',
    "thin_round" :r'\s*thin\s*rounds?\b',
    "wedges"        :r'\s*wedges?\b',
    "chunks"    :r'\s*chunks?\b',
    "even_portions"       :r'\s*(even)?\s*portions?\b',
    "sticks"    :r'\s*sticks?\b',
    #bite-sized
    "bite-sized_pieces"   :r'\s*bite-?\s*sized\s*pieces?\b',
    #5mm


    #Prepared
    "prepare_before_recipe": r'\s*prepared?\s*before\s*recipe\b',
    
    

    #More annoying descriptions
    #barley could be more complicated then I like
    "barely": r'\s*barely\b',
    "edible_flowers": r'\s*(with)?\s*edible\s*flowers\b',
    "beautiful_bunches": r'\s*beautiful\s*bunches\s*(of)?\b',
    

    #sub section overall type describes general grouping 
    
    #"spice_blend": r'\s*spice\s*blend\b',
    #"stalk_of": r'\s*stalk\s*of\b',
    "fixing_agent": r'\s*(with)?\s*fixing\s*agents?\b',
    #"oil": r'\s*oil\b',
    #"icing_sugar": r'\s*icing\s*sugar\b',
    #"powder": r'\s*powder\b',#powered perhaps


    "labeyrie_type": r'\s*labeyrie\s*type\b',
    #"perfume_infusion" : r'\s*Infusion\s*of the same perfume',
    "suzi_wan"  :   r'\s*suzi\s*wan®?\b',
    "briochin"  :   r'\s*briochin\b',
    "dijon"     :   r'\s*dijon\b',
    "chinese"   :   r'\s*chinese\b',

    #basic step cooked sub group 
    "cooked": r'\s*cooked\b',
    "pre_baked": r'\s*pre(-)?\s*baked\b',
    "pre_cooked": r'\s*pre(-)?\s*cooked\b', # precooking without
    "ready_made": r'\s*ready\s*made\b', # precooking without

    #the for and to section
    #to
    "ready_to_roll_out": r'\s*ready\s*to\s*roll\s*out\b',
    "ovals_to_round_strips": r'\s*ovals\s*to\s*round\s*strips\b',
    "to_garnish": r'\s*to\s*garnish\b',
    "to_fry": r'\s*to\s*fry\b', # precooking without

    #for
    "for_color": r'\s*for\s*color\b',
    #"for_me_bought_at_the_same_place": r'\s*for\s*me\s*bought\s*at\s*the\s*same\s*place\b',
    "for_frying_remove": r'\s*for\s*frying\s*(remove)?\b',
    "for_browning": r'\s*for\s*browning\b',
    "for_cooking": r'\s*for\s*cooking\b',

    "for_finishing": r'\s*for\s*finishing\b',
    "for_presentation": r'\s*for\s*presentation\b',
    "for_those_who_like_it": r'\s*for\s*those\s*who\s*like\s*it\b',

    #variations
    "according_to_taste": r'\s*according\s*to\s*taste\b', # precooking without
    "variation" : r'\s*(of)?\s*variation\b',
    "depending" : r'\s*(of)?\s*depending\b',
    "optional"  : r'\s*(of)?\s*optional:?\b',
    "decorations_of_choice": r'\s*(as)?\s*decorations\s*of\s*choice\b',
    "possibly_some": r'\s*possibly\s*(some)?\b',
    "whatever_you_want": r'\s*what\s*ever\s*you\s*want\b',
    "ideally": r'\s*ideally\b',
    "etc": r'\s*etc\b',
    
    #or sub group of variation This group needs more work
    #come back later!
    "or_any_other_milk_powder": r'\s*or\s*any\s*other\b', #"or_any_other_milk_powder"
    "or_more": r'\s*or\s*more\b',
    "or_custard_as_desired": r'\s*or\s*custard\s*as\s*desired\b',

    "or_equivalent":r'\s*or\s*equivalent\b',
    
    #Perferably
    "day_before": r'\s*(from)?\s*(the)?\s*day\s*before\b',
    "if_you_prefer": r'\s*if\s*you\s*prefer\b',
    "preference": r'\s*(if)?\s*(in)?\s*preference\b',

    "absence_of": r'\s*(in)?\s*absence\s*of\b', #something else
    "sensitivity_to_spices": r'\s*(for)?\s*(those)?\s*(with)?\s*sensitivity\s*to\s*spices\b',

    "butter_is_better": r'\s*(but)?\s*butter\s*is\s*better\b', #butter_is_better

    "better_than_broken": r'\s*better\s*than\s*broken\b',
    

    #From might need to do something more complicated
    "from_reims": r'\s*from\s*reims\b',
    "from_asian_grocery_stores": r'\s*from\s*asian\s*grocery\s*strores?\b', #from_asian_grocery_stores
    "from_norway" : r'\s*from\s*norway\b',

    #General non descript info
    #"in_stock" : r'\s*in\s*stock\b',
    "see_recipe_here" : r'\s*see\s*recipe\s*here\b',

    #not tested
    'level' : r'\s*level\b',
    'firm'  : r'\s*firm\b',
    'good'  : r'\s*good\b',

    'norwegian'  : r'\s*norwegian\b',
    'without_the_skin'  : r'\s*without\s*the\s*skin\b',
    'smoked'  : r'\s*smoked \b',
    'salt-preserved'  : r'\s*salt-?\s*preserved\b',
}


#21
"""
confit_pattern = r'Confit'
gloria_pattern = r'Gloria'
canderel_pattern = r'Canderel'


less_than_measure_pattern = r'\s*A little less than a measure \(e\.g\., A little less than a measure of large\)\s*'
nice_chard_leaves_pattern = r'_nice_chard_leaves'

"""

#We should take text and output the text and the column names we can add to

"""
Perhaps we can run a for loop with dict 
"""
def find_modifier(text):
    
    cauhgt_values = []
    cleaned_text = text

    for filter_name, filter in modifier_patterns.items():
        
        found_modifier, cleaned_text = ic.check_modifier(filter, cleaned_text)
    
        if found_modifier:
            cauhgt_values.append(filter_name)

    return cauhgt_values, cleaned_text

def filter_check_specified(filter_name, text):

    print(text)
    filter = modifier_patterns[filter_name]
    return ic.check_modifier(filter, text)

    




    