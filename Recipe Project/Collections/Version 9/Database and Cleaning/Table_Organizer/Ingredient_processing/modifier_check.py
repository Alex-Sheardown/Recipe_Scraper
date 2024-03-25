import re
import initial_check as ic

modifier_patterns = {
    #General can be added anywhere so not specific enoguh 
    """
    if these two are together then we can suggest a minumum level of whatever
    there order should not change much of whats happening 

    not going to use overipe cause its to specific to ripe
    """
    #not need words
    "of" :r'\s*of\s*',

    "very": r'\s*very\s*',
    "not":  r'\s*not\s*',#not_too_ # not in ? # check seperatly with list perhaps
    "too":  r'\s*too\s*',

    "freeze":r'\s*freeze\s*',
    "purchased":r'\s*purchased\s*',

    "just": r'\s*just\s*', # not pattern should just be the one pattern just ripe 
    "without": r'\s*without\s*',
    #"freshly": r'\s*mini\s*\s*',
    "nice": r'\s*nice\s*',

    "preferably": r'\s*(preferably|preferable)\s*',

    #remove not very useful
    #"tooth": r'\s*mini\s*\s*',

    #sizes
    "mini": r'\s*mini\s*',
    "small": r'\s*small\s*',
    "little": r'\s*little\s*', #little variation?
    "medium": r'\s*(medium|med)\s*',
    "large": r'\s*large\s*',
    "plump": r'\s*plump\s*',

    #ripe
    "ripe": r'\s*ripe\s*',
    "overripe": r'\s*overripe\s*',


    #sweet (can be affected by the not, very and tooth)
    "sweet": r'\s*sweet\s*', # not pattern
    # quality description generally of when bought
    "natural": r'\s*natural\s*', # not pattern
    "quality": r'\s*quality\s*', # not pattern
    "new": r'\s*new\s*', # not pattern
    "organic": r'\s*organic\s*', # not pattern #still_organic_pattern = r'And still organic!'
    "frozen": r'\s*(previously)?\s*frozen\s*', # not pattern
    "matured": r'\s*matured\s*', # not pattern
    "seeded": r'\s*seeded\s*',# not pattern
    "pitted": r'\s*pitted\s*',# not pattern
    "shavings": r'\s*shavings\s*',# not pattern
    "raw": r'\s*raw\s*',
    "soft": r'\s*soft\s*',
    "dried": r'\s*dried\s*',
    #"freeze_dried": r'\s*(not\s*to)?\s*ripe\s*',
    "spicy": r'\s*spicy\s*',
    "creamy":  r'\s*creamy\s*',
    "fragrant": r'\s*fragrant\s*',
    "stale": r'\s*stale\s*',
    "strong": r'\s*strong\s*',
    "light": r'\s*light\s*',
    "heavy": r'\s*heavy\s*',
    "crystallized" : r'\s*crystallized\s*',


    #the un group not finished
    "untreated" : r'\s*untreated\s*',
    "unpeeled" : r'\s*unpeeled\s*',
    "unrefined" : r'\s*unrefined\s*',

    "degerminated" : r'\s*degerminated\s*',
    "defatted" : r'\s*defatted\s*',
    "desalinated": r'\s*desalinated\s*',
    "deboned": r'\s*deboned\s*',

    "rinsed": r'\s*rinsed\s*',

    "without_anti_caking_agent": r'\s*without\s*anti\s*caking\s*agent\s*',
    
    "skewered": r'\s*skewered\s*',#skewers
    "on_the_bone": r'\s*on\s*the\s*bone\s*',
    "naturally_salted": r'\s*naturally\s*salted\s*',
    "semi_salted": r'\s*semi\s*salted\s*',
    "crushed": r'\s*crushed\s*',

    #Season sub section
    "season": r'\s*(in)?\s*season(al)?\s*', # not pattern many varitions
    """
    in_season_pattern = r'In '#season
    if_in_season_pattern = r'If it\'s in season'
    seasonal_pattern = r'Seasonal'
    """


    "sweet": r'\s*(not\s*to)?\s*ripe\s*', # not pattern
    

    "phosphate_free": r'\s*phosphate\s*free\s*',
    "molds_with_removable_bases": r'\s*trees?\s*molds?\s*with\s*the?\s*removable?\s*base\s*',
    #how bought sub section
    "sold_in_bags": r'\s*sold\s*in\s*bags\s*',
    "vacuum_packed": r'\s*vacuum\s*packed\s*',

    #basic step for after bought
    "melted": r'\s*melted\s*',
    "mashed": r'\s*mashed\s*',
    "peeled": r'\s*\speeled\s*',
    "steamed": r'\s*steamed\s*',
    "diced": r'\s*diced\s*',
    "minced": r'\s*minced\s*',
    "shredded": r'\s*shredded\s*',
    
    "flaked": r'\s*flaked\s*',
    "soaked": r'\s*soaked\s*',
    "boiled": r'\s*boiled\s*',
    "chopped": r'\s*chopped\s*',
    "mixed": r'\s*mixed\s*',
    "crispy": r'\s*crispy\s*',
    "ball": r'\s*balls?\s*',

    "finely_cut" : r'\s*finely\s*cut',
    "thinly_sliced" :r'\s*thinly\s*sliced\s*',

    "grated": r'\s*grated\s*',
    "ground": r'\s*ground\s*', #r'\s*freshly\s*ground\s*flavor\s*'
    "smoked": r'\s*smoked\s*',


    "keep_the_water_inside" : r'\s*keep\s*the\s*water\s*inside\s*',
    "in_the_oven_remove" : r'\s*(in)?\s*(the)?\s*oven\s*remove\s*',

    
    "well_done": r'\s*well\s*done\s*',
    "leftover": r'\s*left\s*over\s*',
    "pricked": r'\s*pricked\s*',
    "oven_roasted": r'\s*oven\s*roasted\s*',
    "homemade": r'\s*home\s*made\s*',
    "pan_fried": r'\s*pan\s*fried\s*',
    "fir_trees_shape": r'\s*(in)?\s*fir\s*trees?\s*shaped?\s*',
    "long_and_quite_thin": r'\s*(that)?\s*(are)?\s*long\s*and\s*quite\s*thin\s*',

    #More complicated prep
    "broken_with_rolling_pin": r'\s*broken\s*(into)?\s*(pieces)?\s*with\s*(the)?\s*rolling\s*pin\s*',
    #over here got to get specific
    "rolled_with_rolling_pin" : r'\s*rolled\s*with\s*rolling\s*pin\s*',
    "rolled_into" : r'\s*rolled\s*into\s*(rectangles|circles)\s*',
    
    #"cut_into_sticks" : r'\s*cut\s*into\s*sticks\s*',
    "cut_into"  : r'\s*cut\s*into\s*',
    "cubes"     :r'\s*cubes?\s*',
    "quarters"  :r'\s*quarters?\s*',
    "strips"    :r'\s*strips?\s*',
    "pieces"    : r'\s*pieces?\s*',
    #two\s*sections
    "sections"  :r'\s*sections?\s*',
    "slices"    :r'\s*slices?\s*',
    "fine_julienne"   :r'\s*fine\s*juliennes?\s*',
    "thin_round" :r'\s*thin\s*rounds?\s*',
    "wedges"        :r'\s*wedges?\s*',
    "chunks"    :r'\s*chunks?\s*',
    "even_portions"       :r'\s*(even)?\s*portions?\s*',
    #bite-sized
    "bite-sized_pieces"   :r'\s*bite-?\s*sized\s*pieces?\s*',
    #5mm


    #Prepared
    "prepare_before_recipe": r'\s*prepared?\s*before\s*recipe\s*',
    
    

    #More annoying descriptions
    #barley could be more complicated then I like
    "barely": r'\s*barely\s*',
    "edible_flowers": r'\s*(with)?\s*edible\s*flowers\s*',
    "beautiful_bunches": r'\s*beautiful\s*bunches\s*(of)?\s*',
    

    #sub section overall type describes general grouping 
    
    #"spice_blend": r'\s*spice\s*blend\s*',
    #"stalk_of": r'\s*stalk\s*of\s*',
    "fixing_agent": r'\s*(with)?\s*fixing\s*agents?\s*',
    #"oil": r'\s*oil\s*',
    #"icing_sugar": r'\s*icing\s*sugar\s*',
    #"powder": r'\s*powder\s*',#powered perhaps


    "labeyrie_type": r'\s*labeyrie\s*type\s*',
    #"perfume_infusion" : r'\s*Infusion\s*of the same perfume',
    "suzi_wan"  :   r'\s*suzi\s*wan®?\s*',
    "briochin"  :   r'\s*briochin\s*',
    "dijon"     :   r'\s*dijon\s*',
    "chinese"   :   r'\s*chinese\s*',

    #basic step cooked sub group 
    "cooked": r'\s*cooked\s*',
    "pre_baked": r'\s*pre(-)?\s*baked\s*',
    "pre_cooked": r'\s*pre(-)?\s*cooked\s*', # precooking without
    "ready_made": r'\s*ready\s*made\s*', # precooking without

    #the for and to section
    #to
    "ready_to_roll_out": r'\s*ready\s*to\s*roll\s*out\s*',
    "ovals_to_round_strips": r'\s*ovals\s*to\s*round\s*strips\s*',
    "to_garnish": r'\s*to\s*garnish\s*',
    "to_fry": r'\s*to\s*fry\s*', # precooking without

    #for
    "for_color": r'\s*for\s*color\s*',
    #"for_me_bought_at_the_same_place": r'\s*for\s*me\s*bought\s*at\s*the\s*same\s*place\s*',
    "for_frying_remove": r'\s*for\s*frying\s*(remove)?\s*',
    "for_browning": r'\s*for\s*browning\s*',
    "for_cooking": r'\s*for\s*cooking\s*',

    "for_finishing": r'\s*for\s*finishing\s*',
    "for_presentation": r'\s*for\s*presentation\s*',
    "for_those_who_like_it": r'\s*for\s*those\s*who\s*like\s*it\s*',

    #variations
    "according_to_taste": r'\s*according\s*to\s*taste\s*', # precooking without
    "variation" : r'\s*(of)?\s*variation\s*',
    "depending" : r'\s*(of)?\s*depending\s*',
    "optional"  : r'\s*(of)?\s*optional\s*',
    "decorations_of_choice": r'\s*(as)?\s*decorations\s*of\s*choice\s*',
    "possibly_some": r'\s*possibly\s*(some)?\s*',
    "whatever_you_want": r'\s*what\s*ever\s*you\s*want\s*',
    "ideally": r'\s*ideally\s*',
    "etc": r'\s*etc\s*',
    
    #or sub group of variation This group needs more work
    #come back later!
    "or_any_other_milk_powder": r'\s*or\s*any\s*other\s*', #"or_any_other_milk_powder"
    "or_more": r'\s*or\s*more\s*',
    "or_custard_as_desired": r'\s*or\s*custard\s*as\s*desired\s*',

    "or_equivalent":r'\s*or\s*equivalent\s*',
    
    #Perferably
    "day_before": r'\s*(from)?\s*(the)?\s*day\s*before\s*',
    "if_you_prefer": r'\s*if\s*you\s*prefer\s*',
    "preference": r'\s*(if)?\s*(in)?\s*preference\s*',

    "absence_of": r'\s*(in)?\s*absence\s*of\s*', #something else
    "sensitivity_to_spices": r'\s*(for)?\s*(those)?\s*(with)?\s*sensitivity\s*to\s*spices\s*',

    "butter_is_better": r'\s*(but)?\s*butter\s*is\s*better\s*', #butter_is_better

    "better_than_broken": r'\s*better\s*than\s*broken\s*',
    

    #From might need to do something more complicated
    "from_reims": r'\s*from\s*reims\s*',
    "from_asian_grocery_stores": r'\s*from\s*asian\s*grocery\s*strores?\s*', #from_asian_grocery_stores
    "from_norway" : r'\s*from\s*norway\s*',

    #General non descript info
    #"in_stock" : r'\s*in\s*stock\s*',
    "see_recipe_here" : r'\s*see\s*recipe\s*here\s*'
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

    for column, filter in modifier_patterns.items():
        
        found_modifier, cleaned_text = ic.check_modifier(filter, cleaned_text)
    
        if found_modifier:
            cauhgt_values.append(column)

def filter_check_specified(filter_name, text):

    filter = modifier_patterns[filter_name]
    return ic.check_modifier(filter, text)

    




    