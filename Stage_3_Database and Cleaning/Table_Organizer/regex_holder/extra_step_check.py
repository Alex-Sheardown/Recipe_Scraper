import json

useless = False
modifier =False
measurements =True

def useless_patterns_to_json(patterns, filename):
    json_data = [{"pattern": pattern} for pattern in patterns]
    with open(filename, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)

def modifier_patterns_to_json(patterns_dict, filename):
    json_data = [{"name": name, "pattern": pattern} for name, pattern in patterns_dict.items()]
    with open(filename, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)

def measurements_to_json(patterns, filename):
    json_data = [{"name": name, "pattern": pattern if isinstance(pattern, str) else pattern} for name, pattern in patterns.items()]
    with open(filename, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)
            
    with open(filename, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)

if useless:
    

    # Example usage:

    combined_patterns = [

            r"\s*dish\(es\)",
            r"\s*decorative\s*elements",
            r"\s*according",
            r"\s*desires",
            r"it's\s*good\s*when\s*it's\s*beautiful",
            r"it\'s\s*",
            r"\s*when",
            r"\s*for\s*me",
            r"\s*for\s*the\s*soup\b",
            r'\s*on\s*top\s*of\s*the\s*lasagna\b',
            r'\s*on\s*top\s*of\s*the\b',
            r'\s*on\s*top\s*of\b',
            r'\s*on\s*top\b',

            r'\s*for\s*the\s*energy\s*bars?\b',
            r'\s*for\s*the\s*energy\b',
            r'\s*for\s*the\b',
            r"\s*for\s*top\b",

            r'\s*main\s*course\b',
            r'\s*make\s*omelette\b',
            r'\s*in\s*granola\b', 
            
            r'\s*make\s*the\s*omelette\b'
            
            
            r'\s*to\s*make\s*the\s*meatballs\b', 
            r'\s*to\s*make\s*the\b', 
            r'\s*to\s*make\b',  

            
            r'\s*to\s*the\s*sautéed\s*mushrooms\b',  
            r'\s*to\s*the\s*sautéed\b',
            r'\s*to\s*the\b', 

            r'\s*combine\b', 

            r'\s*can\s*enhance\s*the\s*flavor\s*of\s*the\s*soup\b',
            r'\s*for\s*the\s*soup\b',
            
            
            #r'\bthe\s*meatballs\s*',

            r'\s*in\s*the\s*granola\s*for\s*extra\s*crunch\b',
            r'\s*in\s*the\s*granola\s*for\s*extra\b',
            r'\s*in\s*the\s*granola\s*for\b',

            r'\s*extra\s*crunch\b',
            r'\s*for\s*a\s*generous\s*serving\b',
            r'\s*on\s*the\s*pizza\b',

            r"\s*long\s*piece\b",

            r"\s*to\s*sweeten\s*the\s*tea\s*",

            #r'\s*decorate\s*cake\s*with\b',
            #r'\s*decorate\s*cake\s*',
            r"decorate\s*the\s*cake\s*with\s*",
            r'\s*decorate\b'

            r'\bassembling\b',
            r'\s*for\s*assembling\s*tacos\b',
            r'\s*top\s*with\b',

            r"\s*you'll\s*need\b",
            r"\bdessert\b",


            r"\s*measure\s*out\b",
            
            r"\s*you'll\s*bneed\b",
            r'\s*with\s*a\b',
            r"\s*shape\s*bread\s*into\b",
            r"\s*bread\s*into\b",
            

        
            r'\barrange\b',
        
        
            r'\s*can\s*enhance\s*',
            #r'\bsandwich\b',
            r'\badded\b',
            
            
            r'\bplatter\b',
            r'\barrange\b',
            r'\bplatter\b',
            
            
            r'\bsweeten\b',
            
            r'\bthem\b',
            r'\bcarefully\b',
            r'\binclude\b',
            
            
        
            r'\b(bowl)\s*of\b',
            r'\bused\b',
            r'\bshe\b',
            r'\bhe\b',
            r'\badd\b',
            r'\bfor\b',
            r'\bthe\b',
            r'\bto\s*(stuff|cook)\b',
            #r'\bhot\b',
            r'\bpan\b',

            
            r'\bon\b',
            r'\bhis\b',
            r'\btea\b',
            r'\buse\b',
            r'\blay\b',
            r"\bwith\b",
            r"\bcreate\b",
            r"\blayer\b",
            r"\bform\b",
            r"\bstack\b",
            r"\babout\b",
            #extra space
            
            


            #experimental
            r"\binto\b",
            r"\bshape\b",
            r"\bthick\b",

            
            r'\s*weighting\b',
            r"\bweighing\b",
            
            r"\s*from\s*mandy,\s*done\\b",
            r"\s*,\s*done\b",
            r"\s*portioned\s*in\b",
            

            r"\s*,?_?\s*approximately_?\b",
            r"\bœ\b",

            r"^\s*and\b",
            r"\s*approx.\b",
            r'\b(\s*and\s*)\s*$',
            r"\b(\s*or\s*)\s*$",

            r"^\s*at\b",
            r"^\s*by\b"
            r"\s*(\(\s*taste\s*\)|taste)\b",
            
            #butter_,_
            
            r"\s*\.?amount\b",
            r"\s*roux\b",
            #r"\s*i\bvalpiform\bbread\band\bpastry\bmix\)\bquantity\bknead\bdough\bcorrectly\b",
            
            r"\babout\b",
            
            r"\bof\b",
            r"ingredients?",
            r"from",
            r"and\s*other\s*decorations?",
            r"don’?'?t\s*forget\s*",
            r"see\s*tip",
            r"cooking",
            r"amount\s*your\s*liking!",
            r"oriental\s*grocery\s*stores",
            
            r"\s*st\s*morêt",
            r",\s*,\s*.",

            r"by\s*grating\s*chocolate\s*peeler\s*",



            r"\s*supermarket\b",
            r"\s*be\s*aware\b",
            r",?however,?" ,
            r"\s*that\s*moquec\s*is\s*eaten\s*very\b",
            r"\s*childhood\b",
            r"®",
            
            r"\s*in\s*supermarkets\s*or\s*barry\s*in\s*specialist\s*stores",
            r"sold\s*in\s*supermarkets",

            r"\s*between\b",
    
            #r"\s*container",
            r"\s*if\s*you\s*cannot\s*find\s*this\s*cheese,?",
            r'\s*etc\b',

            r'\bextra?\b.*$',
            r'\bextra\b',

            r"\s*\(\s*or",
            r"\(\s*fat",
            r"\s*made\s*above",
            r"\s*it\s*all\s*depends\s*quantity",
            r"\s*ready\s*to\s*",
            #"\s*a?\s*(few)?\s*(for)?\s*",
            r"\s*few",
            r"\s*cooked\s*at\s*home\s*or\s*in\s*a\s*can\s*",
            r"\s*to\s*your",
            r"\s*in\s*this\s*case\s*you\s*need\s*",
            r"\s*in\s*asia?n?\s*grocery\s*stores\s*",
            r"\s*strength\s*coloring\s*",
            r"\s*brand",
            r'\s*made\s*this\s*summer',
            r'\s*put\s*in\s*',
            r'\s*size',
            r'\s*diagonally',
            r'\s*but\s*as',
            r'\s*you\s*have',
            r'\s*dark/',
            r'\s*they\s*are',
            r'\s*and\s*very',
            r'\s*whatever\s*you\s*have\s*will\s*do',
            r'\s*store',
            r'\s*siphon',
            r'\s*and\s*keep\s*theasurement',
            r'\s*which\s*will\s*reveal\s*all\s*its\s*',
            r'\s*otherwise',
            r'\s*failing\s*that',
            r'\s*bring\s*second\s*in\s*case',
            r'\s*desired\s*consistency',
            r'\s*size',
            r'\s*total',
            r'\s*left',
            r'\s*quick',
            
            

            

            r"\s*\.\s*\.\s*\.\s*",
            #r"\s*.\s*.\s*.",

            r"\(\s*\,*\s*\.*\)",

            
        ]
    useless_patterns_to_json(combined_patterns, "useless_patterns.json")

if modifier:


    modifier_patterns = {
        #General can be added anywhere so not specific enoguh 

        #not need words
        #"of" :r'\s*of\s*',
        "fine_and_amora" : r"\s*fine\s*and\s*amora",
        "a_little_grated_peel" : r"\s*a\s*little\s*grated\s*peel",
        
        "not":  r'\bnot\b',#not_too_ # not in ? # check seperatly with list perhaps
        "too":  r'\s*too\b',

        "freeze":r'\s*freeze\b',
        "purchased":r'\s*purchased\b',

        "just": r'\s*just\b', # not pattern should just be the one pattern just ripe 
        "without_the_white": r'\s*without\s*the\s*white',
        'without_the_skin'  : r'\s*without\s*(the)?\s*skin\b',
        "without_anti_caking_agent": r'\s*without\s*anti\s*caking\s*agent\b',
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
        "medium": r'\b(medium|med)\b',
        "large": r'\s*large\b',
        "plump": r'\s*plump\b',

        #ripe
        "ripe": r'\s*ripe\b',
        "overripe": r'\s*overripe\b',


        "only_the_leaves" :r"\s*only\s*the\s*leaves\s*are\s*used",

        #sweet (can be affected by the not, very and tooth)
        "sweet": r'\s*sweet\b', # not pattern
        # quality description generally of when bought
        "natural": r'\s*natural\b', # not pattern
        "quality": r'\s*quality\b', # not pattern
        "new": r'\s*new\b', # not pattern
        "organic": r'\s*organic\b', # not pattern #still_organic_pattern = r'And still organic!'
        "frozen": r'\s*(previously)?\s*frozen\b', # not pattern
        "matured": r'\s*matured?\b', # not pattern
        "seeded": r'\s*seeded\b',# not pattern
        "pitted": r'\s*pitted\b',# not pattern
        "shavings": r'\s*shavings\b',# not pattern
        "raw": r'\s*raw\b',

        "soft": r'\s*(slightly)?\s*soft\b',
        "dried": r'\s*dried\b',
        #"freeze_dried": r'\s*(not\s*to)?\s*ripe\b',
        "spicy": r'\s*spicy\b',
        "creamy":  r'\s*creamy\b',
        "fragrant": r'\s*fragrant\b',
        "stale": r'\s*stale\b',
        "strong": r'\s*strong\b',
        "light": r'\blight\b',
        "heavy": r'\s*heavy\b',
        "crystallized" : r'\s*crystallized\b',


        #the un group not finished
        "untreated" : r'\s*untreated\b',
        "unpeeled" : r'\s*unpeeled\b',

        'lightly_sweetened' : r'\s*lightly\s*sweetened',
        "lightly_refined" : r'\s*(lightly)?\s*refined',
        "unrefined" : r'\s*unrefined\b',

        "degerminated" : r'\s*deger(minated|med)\b',
        "defatted" : r'\s*defatted\b',
        "desalinated": r'\s*desalinated\b',
        "deboned": r'\s*deboned\b',

        "rinsed": r'\s*rinsed\b',
        
        
        "skewered": r'\s*skewered\b',#skewers
        "on_the_bone": r'\s*on\s*the\s*bone\b',
        'naturally' : r'\s*naturally',
        
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
        'milk_free' : r'\s*milk\s*free',
        "molds_with_removable_bases": r'\s*trees?\s*molds?\s*with\s*the?\s*removable?\s*base\b',
        #how bought sub section
        "sold_in_bags": r'\s*sold\s*in\s*bags\b',
        "vacuum_packed": r'\s*vacuum\s*packed\b',

        #basic step for after bought
        "melted": r'\s*melted\b',
        "mashed": r'\s*mashed\b',
        "peeled": r'\s*peeled\b',
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
        "fine" : r'\s*finel?y?\b',

        "finely_cut" : r'\s*finely\s*cut',

        #"slices"    :r'\s*slices?\b',
        "thinly_sliced" :r'\s*thinly\s*sliced\b',
        "sliced" :r'\s*sliced\b',

        "thick" : r'\s*thick\b',
        "thin" : r'\s*thin\b',

        "grated": r'\s*grated\b',
        "ground": r'\s*ground\b', 
        "smoked": r'\bsmoked\b',


        "keep_the_water_inside" : r'\s*keep\s*the\s*water\s*inside\b',
        "in_the_oven_remove" : r'\s*(in)?\s*(the)?\s*oven\s*remove\b',

        
        "well_done": r'\s*well\s*done\b',
        "leftover": r'\s*left\s*over\b',
        "pricked": r'\s*pricked\b',
        "oven_roasted": r'\s*oven\s*roasted\b',
        "roasted" : r'\s*roasted',
        "homemade": r'\s*home\s*made\b',
        "fried": r'\s*(pan)?\s*fried\b',
        "fir_trees_shape": r'\s*(in)?\s*fir\s*trees?\s*shaped?\b',
        "long_and_quite_thin": r'\s*(that)?\s*(are)?\s*long\s*and\s*quite\s*thin\b',

        #More complicated prep
        "broken_with_rolling_pin": r'\s*broken\s*(into)?\s*(pieces)?\s*with\s*(the)?\s*rolling\s*pin\b',
        
        "ready_to_roll_out": r'\s*ready\s*to\s*roll\s*out\b',
        "rolled_with_rolling_pin" : r'\s*rolled\s*with\s*rolling\s*pin\b',
        "rolled_into" : r'\s*rolled\s*into\s*(rectangles|circles)\b',
        'rolled': r'\s*rolled',
        'rolls': r'\s*rolls?',
        #over here got to get specific
        
        

        
        #"cut_into_sticks" : r'\s*cut\s*into\s*sticks\b',
        "cut"  : r'\s*cut\b',
        "cubes"     :r'\s*(in)?\s*cubes?\b',
        "quarters"  :r'\s*quarters?\b',
        "strips"    :r'\s*(in)?\s*strips?\b',
        "pieces"    : r'\s*in\s*pieces?\b',
        #two\s*sections
        "sections"  :r'\s*sections?\b',
        
        "julienne"   :r'\s*(fine)?\s*juliennes?d?\b',

        "wedges"        :r'\s*wedges?\b',
        "chunks"    :r'\s*chunks?\b',
        "even_portions"       :r'\s*(even)?\s*portions?\b',
        "sticks"    :r'\s*sticks?\b',
        #bite-sized
        "bite-sized_pieces"   :r'\s*bite-?\s*sized\s*pieces?\b',
        #half
        #5mm

        #salted
        "naturally_salted": r'\s*naturally\s*salted\b',
        "semi_salted" : r"\s*semi\s*salted",
        'demi_salted' : r'\s*demi-?\s*salted',
        'desalted' : r'\s*desalted',
        "salted" : r"\s*salted!?",
        
        
        

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
        "ready_cook" : r'\s*ready\s*cook',
        "cooked": r'\s*cooked\b',
        "pre_baked": r'\s*pre(-)?\s*baked\b',
        "pre_cooked": r'\s*pre(-)?\s*cooked\b', # precooking without
        "ready_made": r'\s*ready\s*made\b', # precooking without

        #the for and to section
        #to
        
        "ovals_to_round_strips": r'\s*ovals\s*to\s*round\s*strips\b',
        "to_garnish": r'\s*(to\s*)?garnish\b',
        "to_fry": r'\s*to\s*fry\b', # precooking without

        #for
        "for_color": r'\s*for\s*color\b',
        #"for_me_bought_at_the_same_place": r'\s*for\s*me\s*bought\s*at\s*the\s*same\s*place\b',
        "for_frying_remove": r'\s*for\s*frying\s*(remove)?\b',
        "for_browning": r'\s*for\s*browning\b',
        "cooking": r'\s*(for)?\s*cook(ing)?\b',

        "for_finishing": r'\s*for\s*finishing\b',
        "for_presentation": r'\s*for\s*presentation\b',
        "like": r'\s*(if)\s*(you)\s*(for)?\s*(those)?\s*(who)?\s*like\s*(it)?',
        
    
        #variations
        "to_taste": r'\s*(according)?\s*(to)?\s*(taste)?\s*(your)?\s*(desires?)?\s*(choice)?', # precooking without
        "variation" : r'\s*(of)?\s*variation\b',
        "depending" : r'\s*(of)?\s*depending\b',
        "optional"  : r'\s*(of)?\s*optional:?\b',
        "decoration": r'\s*(few)?\s*(as)?\s*decorat(e|ions?|ive)(\s*(of)?\s*choice)?(elements?)\s*',
        
        "possibly_some": r'\s*possibly\s*(some)?\b',
        "whatever_you_want": r'\s*what\s*ever\s*you\s*want\b',
        "ideally": r'\s*ideally\b',
        #"etc": r'\s*etc\b',
        
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
        'better_than_milk' : r'\s*better\s*than\s*milk',
        'better' : r'\s*(is)?\s*better\s*',
        

        #From might need to do something more complicated
        "reims": r'\s*(from)?\s*reims\b',
        "from_asian_grocery_stores": r'\s*(from)?\s*asian\s*grocery\s*strores?\b', #from_asian_grocery_stores
        "from_norway" : r'\s*(from)?\s*norway\b',

        #General non descript info
        #"in_stock" : r'\s*in\s*stock\b',
        "see_recipe_here" : r'\s*see\s*recipe\s*here\b',

        #not tested
        'level' : r'\s*level\b',
        'firm'  : r'\s*firm\b',
        'good'  : r'\s*good\b',

        'norwegian'  : r'\s*norwegian\b',
        
        'smoked'  : r'\s*smoked \b',
        'salt-preserved'  : r'\s*salt-?\s*preserved\b',
        'at_room_temperature' : r'\s*at_?\s*room_?\s*temperature\b',
        'authentic' : r'\s*authentic\b',

        'in_half_lengthwise' : r'\s*in\s*half\s*lengthwise\b',
        'around' : r'\s*around\b',
        'aged' : r'\s*aged\b',
        'amora' : r'(\s*croq\'vert)?\s*amora\b',
        'beautiful' : r'\s*beautiful\b',
        'lots_black_spots' : r'\s*lots\s*black\s*spots\b',
        'blanched' : r'\s*blanched\b',
        'finely' : r'\s*finely\b',
        'beaten' : r'\s*(lightly)?\s*beaten\b',
        "beautiful" : r"\s*beautiful\b",
        "basic_elements" : r"\s*basic\s*elements\b",
        #beaten_salted_and_peppered_egg_(_milk_or_liquid_cream)
        'boiling' : r"\s*boiling\b",
        #"bitter" : r"\s*bitter\b",
        'puree' : r"\s*puree(d|s)?\b",
        "garden" : r"\s*(from)?\s*garden\b",
        "beaten" : r"\s*beaten\b",
        "boxed" : r"\s*boxed\b",
        "bomb" : r"\s*bomb\b",
        "powder" : r"\s*poweder\b",
        "broken" : r"\s*broken\b",
        "for_the_plate" : r"\s*for\s*the\s*plate\b",
        "american_style" : r"\s*american\s*style\s*",
        "boneless" : r"\s*boneless\b",
        "fresh" : r"\s*fresh\b",
        "burgundy" : r"\s*burgundy\b",
        "butcher_style" : r"\s*butcher\s*style\b",
        "to_taste" : r"\s*(to)?\s*taste\b",
        "soissons" : r"\s*soissons\b",
        'himalayan' : r'\s*himalayan',
        'passed_through_sieve' : r'\s*passed\s*through\s*sieve',

        
        "from_garden" : r"\s*from\s*(the)?\s*garden\b",
        "ripe_but_firm" : r"\s*ripe\s*but\s*firm\b",
        "bonne_maman" : r"\s*bonne\s*maman\b",
        "cored" : r"\s*cored\b",
        "roughly" : r"\s*rough(ly)?\b",
        "smooth" : r'\s*smooth',
        #"suit_your_taste" : r"\s*suit\s*your\s*taste\b*",
        "cleaned" : r"\s*cleaned\b",
        "lean" : r"\blean\b",
        "coarse" : r"\s*coarse\b",

        "country-style" : r"\s*country-style\b",
        "country" : r"\s*country\b",

        
        "drained" : r"\s*drained\s*(well)?",
        "crumbled" : r"\s*crumbled\b",
        "spread" : r"\s*spread\b",

        "philadelphia": r"\s*philadelphia\b",
        "st-Morêt" : r"\s*st-?\s*morêt\b",  
        "kiri" : r"\s*kiri\b",
        #temps not included lol
        "cold" : r"\s*(very)?\s*cold\b",

        "catalan" : r"\s*catalan\b",
        "maizena" : r"\s*ma(ï|i)zena®?\b",
        "crumbled" : r"\s*crumbled\b",
        "vanhouten": r"\s*van\s*houten\b",
        "cobourg": r"\s*cobourg\b",
        "carte_d_or" : r"\s*carte\s*d(’|')\s*or\b",
        "pistoles" :r"\s*pistoles",
        "was_enough_me" : r"\s*was\s*enough\s*(for)?\s*me",
        "carte_d'or" : r"\s*carte_d(’|')or®?",

        "complete" : r"complete",
        "integral" : r"integral",
        "danone" : r"danone",

        "the leaves" : r"(the)?\s*leaves",
        "van_houten" : r"van\s*houten",

        "with_their_stems" : r"with\s*their\s*stems",

        "whole" : r"\s*whole\b",
        "clovis" : r"\s*clovis\b",
        "caramelized" : r"\s*caramelized\b",
        "imperial_powder" : r"\s*imperial\s*powder",
        "van houghten" : r"\s*van\s*houghten",


        "blackcurrant" : r"\s*blackcurrant\b",
        "whipping" : r"\s*whipping",
        "st sever" : r"\s*st\s*sever",
        "cooking" : r"\s*cooking\b",
        "cathedral city" : r"\s*cathedral\s*city\s*",
        #"mature" : r"\s*mature",
        "crunchy" : r"\s*crunchy",
        "verrines" : r"\s*verrines",
        "compagnons du goût" : r"\s*compagnons\s*du\s*goût\b",
        "slection" : r"\s*selection\b",
        "besan_or_gram" : r"\s*?\(besan\s*(or\s*gram\))?",
        "crumbled" : r"\s*crumbled\b",
        "caramelized" : r"\s*caramelized\b",
        "at_least" : r"\s*at\s*least\b",
        'confit' : r"\s*confit\b",
        "if_you_want": r"\s*if\s*you\s*want\b",
        'colorful' : r"\s*colorful\b",
        "classic" : r"\s*classic\b",
        "inverted" : r"\s*inverted\b",
        "vermicelli" : r"\s*vermicelli\b",
        "cliforette" : r"\s*cliforette\b",
        "flaming" : r"\s*flaming\b",
        "chuao" : r"\s*chuao\b",
        "valrhon" : r"\s*valrhon",
        "pure" : r"\s*pure\s*(origin)?\b",
        "marmande" : r'\s*(from)?\s*marmande\b',
        "asterix" : r'\s*asterix\b',
        "goth" : r'\s*goths?',
        "albert_menès" : r'\s*albert\s*menès',
        "canned": r'\s*canned\b',
        'la_napolea' : r'\s*la\s*napolea',
        "crumbled" : r'\s*crumbled',
        "sprouts" : r'\s*sprouts?',
        "with_its_tops" : r'\s*with\s*its\s*tops',
        "carapelli_vivace_bicarbonate" : r'\s*carapelli\s*vivace\s*bicarbonate\s*',
        'concentrated' : r'\s*concentrated\s*',
        'candied' : r'\s*candied',
        'your_choice' : r'\s*your\s*choice',
        'alter_africa' : r'\s*alter\s*africa',
        'from_store' : r'\s*from\s*store',
        
        'zest' : r'\s*zest',
        'each' : r'\s*each\b',
        'bjorg' : r'\s*bjorg',
        'mild' : r'\s*mild',
        'sharp' : r'\s*sharp',
        'squeezed' : r'\s*(freshly)?\s*squeezed\b',
        'danette' : r'\s*danette',
        'charlotte_red_label' : r'\s*(charlotte)?\s*red\s*label',
        'glazed' : r'\s*glazed',
        'guinettes' : r'\s*guinettes',
        'halves' : r'\s*halves',
        'charlotte' : r'\s*charlotte\s*(type)?',
        "failing_that" : r'\s*failing\s*that',
        "from_melfor" : r"\s*(from)?\s*melfor",
        "market" :r"\s*market\b",
        "sauceline" : r"\s*sauceline",
        "if_smaller" : r"\s*if\s*(it\'s)?\s*a\s*smaller",
        "leftovers" : r"\s*leftovers?",
        'cognac' : r"\s*cognac",
        'fried_in_butter' : r"\s*fried\s*in\s*butter",
        "coarsely" : r"\s*coarsel?y?", 
        "crumbled" : r"\s*crumbled",
        "me_gluten_free" : r"\s*me\s*gluten\s*free",
        "containing_livers" : r"\s*(still)?\s*(containing)?\s*their\s*livers?",
        
        "cubed" : r"\s*cubed",
        "i_didn't_have_any" : r'\s*i\s*didn\'t\s*have\s*any',
        "in_shoulder" : r'\s*in\s*(the)?\s*shoulder',
        "corsican_canestrelli" : r'\s*corsican\s*canestrelli',
        "clarified" : r'\s*clarified',
        "cornicabra" : r'\s*cornicabra',
        "from_spain" : r'\s*from\s*spain',
        "candia" : r'\s*candia\s*baby',
        "from_your_poultry_store" : r'\s*(from)?\s*(your)?\s*poultry\s*store',
    
        "cassegrain" : r'\s*cassegrain',
        "crumbs" : r'\s*crumbs?\b',
        "colored" : r'\s*(multi)?\s*colored',
        "carambar" : r'\s*carambar®?',
        "with_the_peel" : r'\s*with\s*the\s*peel',
        "diluted_in_glass_water" : r'\s*diluted\s*in\s*glass\s*water',
        "canadian" : r"\s*canadian",
        'casa_azzurra':  r"\s*casa\s*azzurra",
        "ciflorettes" : r"\s*ciflorettes",
        "made_from_milk" : r"\s*made\s*from\s*milk",
        "julienned" : r"\s*julienned",
        "carambar" : r"\s*carambar",
        "industrial" : r'\s*industrial',
        "chuka_wakame" : r'\s*chuka\s*wakame',
        "pays_de_caux" : r'\s*pays\s*de\s*caux',
        "calvados" : r'\s*calvados',
        "caraïbos" : r'\s*caraïbos',
        'liquefied' : r'\s*liquefied',
        "semi_liquid" : r'\s*semi\s*liquid',
        "liquid" : r'\s*liquid',
        "crunchy" : r'\s*crunchy',
        "la_napolea_brand" : r'\s*la\s*napolea\s*brand',
        "cacao_barry" : r'\s*cacao\s*barry',
        "dark_gold" : r'\s*dark\s*gold',
        "black_gold" : r'\s*black\s*gold',
        "chatawak" : r'\s*chatawak',
        "nestl_e" : r'\s*nestl_(é|e)',
        "in_water" : r'\s*in\s*water',
        'france' : r'\s*france',
        'toasted' : r'\s*toasted',
        'vacuum_packed' : r'\s*vacuum\s*-?packed',
        'deveined' : r'\s*deveined',
        'dehydrated' : r'\s*dehydrated',
        'hydrated' : r'\s*hydrated',
        'dry' : r'\s*dry\b',
        'yon_la_goêle' : r'\s*in\s*yon\s*la\s*go(ê|e)le\s*',
        'confit' : r'\s*confit',
        'thin' : r'\s*thin',
        'dolloped' : r'\s*dolloped',
        'doused' : r'\s*doused',
        'dose' : r'\s*dose',
        'disc' : r'\s*disc',
        'valrhona' : r'\s*valrhona',
        'barry_cocoa' : r'\s*barry\s*cocoa',
        'chantecler' : r'\s*chantecler',
        'tangy' : r'\s*tangy',
        'flavor' : r'\s*(rich\s*in)?\s*flavor(ed)?',
        'dar_egal' : r'\s*dar\s*(é|e)gal',
        'doused_amora' : r'\s*(doused)?\s*amora',
        'reserve' : r'\s*reserve',
        'per': r'\bper\b\s*(cream)?',
        'domed' : r'\s*domed',
        'dakatine' : r'\s*dakatine',
        'dressing' : r'\s*dressing',
        'at min.' : r'\s*at\s*min\.?',
        'reduction' : r'\s*reduction',
        'recovered_cooking_juice' : r'\s*recovered\s*(cooking)?\s*juice',
        'durum' : r'\s*durum',
        'guinness' : r'\s*guinness',
        'cold_pressed' : r'\s*cold\s*pressed',
        'dolfin' : r'\s*dolfin',

        'more_than' : r'\s*more\s*than',
        'south_west' : r'\s*south\s*west',
        'terrine' : r'\s*terrine',
        'derinded' : r'\s*de\s*rinded',
        'dakatine' : r'\s*dakatine',
        'alsace' : r'\s*alsace\s*(type)?',
        
        'ghana' : r'\s*ghana',
        'r_égal_et_sens' : r'\s*r\s*(é|e)gal\s*et\s*sens',
        'denervated' : r'\s*denervated',
        'danette' : r'\s*danette',
        'stirred' : r'\s*stirred',
        'ducros' : r'\s*ducros',
        'couverture' : r'\s*couverture',
        "white_and_yolk_separated" : r'\s*(white|yolk)s?\s*and\s*(white|yolk)s?\s*separated',
        "brushing" : r'\s*brushing',
        "gilding" : r'\s*gilding',
        "separated" : r'\s*separated?',
        "beaten" : r'\s*(lightly)?\s*beaten',
        'ebly' : r'\s*ebly®?',
        'elle_&_vire' : r'\s*elle\s*(&|and)\s*vire',
        'ethiquable' : r'\s*ethiquable',
        'powder_work_surface' : r'\s*powder\s*work\s*surface',
        'madagascar' : r'\s*madagascar',
        'edible' : r'\s*edible',
        'entredeuxmers' : r'\s*entredeuxmers',
        'etorki®' : r'\s*etorki®?',
        'preparation' : r'\s*preparation',
        'mets_aventures' : r'\s*mets\s*aventures',
        'easy' : r'\s*easy\b',
        'extremely' : r'\s*extremely',
        'exotic' : r'\s*exotic\s*(fruits)?',
        'empty' : r'\s*empty',
        'golden' : r'\s*golden',
        'whipped_until_stiff' : r'\s*whipped\s*until\s*stiff',
        'elongated' : r'\s*elongated',
        'long' : r'\blong\b',
        'wide' : r'\bwide\b',


        'local' : r'\s*local',
        'fatty' : r'\s*fatty',
        'douceur_de_saint_agur' : r'(\s*douceur)?\s*de\s*saint\s*agur',
        'st_moret_clod' : r'\s*(st|saint)\s*m(o|ô)ret\s*(clod)?',
        'still_in_pod' : r'\s*still\s*in\s*pod',
        'shelled' : r'\s*shelled',
        'ferment' : r'\s*ferment(ed)?',
        'fjord' : r'\s*fjord',
        'free_range' : r'\s*free\s*range',
        'florets' : r'\s*florets',
        'chavroux' : r'\s*chavroux',
        'saint_maure' : r'\s*saint\s*maure',
        'fluid' : r'\s*fluid',
        'fruity' : r'\s*fruity',
        'spread' : r'\s*spread',
        'filtered' : r'\s*filtered',
        'floury' : r'\s*floury',
        'incorporated' : r'\s*incorporated',
        'fleury_michon' : r'\s*fleury\s*michon',
        'petit_billy' : r'\s*petit\s*billy',
        'fairly' : r'\s*fairly',
        'sifted' : r'\s*sifted',
        'pasteurized' : r'\s*pasteurized',
        'florida' : r'\s*florida',
        'defrosted' : r'\s*defrosted',
        'flat' : r'\s*flat',
        'filleted' : r'\s*fillete?d?',
        'cutlets' : r'\s*cutlets?',
        'fleshed' : r'\s*fleshed',

        'green' : r'\s*green',
        'golden' : r'\s*golden',
        'gray' : r'\s*gray',
        'grilled' : r'\s*grilled',
        'red' : r'\bred\b',
        'gluten_free' : r'\s*gluten\s*free',
        'generous' : r'\s*generous',
        'softened' : r'\s*softened',
        'superfine' : r'\s*super\s*fine',
        'grain_fed' : r'\s*grain\s*fed',
        'mixture' : r'\s*mixture(\s*your\s*choice)?',
        'scaled' : r'\s*scaled',
        'glacial' : r'\s*glacial',
        'lengthwise' : r'\s*length\s*wise',
        'grain' : r'\s*grain',
        'gu_érande' : r'\s*gu\s*(é|e)rande',
        'fermage' : r'\s*fermage',
        'clarified' : r'\s*clarified',
        'bitter' : r'\s*bitter',
        'gutted' : r'\s*gutted',
        'gâtinais' : r'\s*gâtinais',
        'chardonnay' : r'\s*chardonnay',
        'coteaux_du_layon' : r'\s*coteaux\s*du\s*layon',
        'washed' : r'\s*washed',
        'half' : r'\s*half',
        'in_tube' : r'\s*in\s*tube',
        'sure_valley' : r'\s*sure\s*valley',
        'lot_et_garonne' : r'\s*lot\s*et\s*garonne',
        'hollow' : r'\s*hollow',
        'herbamare' : r'\s*herbamare',
        'hawaiian' : r'\s*hawaiian',
        'lomagne' : r'\s*lomagne',
        'hungarian' : r'\s*hungarian',
        'preserved_in_oil' : r'\s*preserved\s*in\s*oil',
        'round' : r'\s*round(s|ed)?',
        'juicy' : r'\s*juicy',
        'juice' : r'\s*juice',
        'julienned' : r'\s*julienned',
        'japanese' : r'\s*japanese',
        'jura' : r'\s*jura\s*(grape)?\s*(variety)?',
        'jerusalem' : r'\s*jerusalem',
        'jean_martin' : r'\s*jean\s*martin',
        'jean_routhiau' : r'\s*jean\s*routhiau',
        'jerez' : r'\s*jerez',
        'jean_herve' : r'\s*jean\s*herve',
        'jupiler' : r'\s*jupiler',
        'jeanlain' : r'\s*jeanlain',
        'jules_destrooper' : r'\s*jules\s*destrooper',
        'ker_cad_élac' :  r'\s*ker\s*cad\s*(é|e)lac©?',
        'kambly' : r'\s*kambly',
        'kritsen' : r'\s*kritsen',
        'knorr' : r'\s*knorr',
        'kiri' : r'\s*kiri',
        'kombu' : r'\s*kombu',
        'kaffir' : r'\s*kaffir', 
        'knacki' : r'\s*knacki',
        'kahlua' : r'\s*kahlua',
        'kinder' : r'\s*kinder®?',
        'kellog' : r'\s*kellogg\'s',
        'kayser' : r'\s*kayser',
        'kirsch' : r'\s*kirsch',
        'kamut' : r'\s*kamut',
        'knorr' : r'\s*knorr',
        'lukewarm' : r'\s*lukewarm',
        'lindt' : r'\s*lindt',
        'loaded' : r'\s*loaded',
        'lesieur' : r'\s*lesieur',
        'bitterness' : r'\s*bitterness',
        'reconstituted' : r'\s*reconstituted',
        'label_rouge_charlotte' : r'\s*label\s*rouge\s*charlotte',
        'laughing' : r'\s*laughing',
        'apices_planet' : r'\s*apices\s*planet',
        'low_fat' : r'\s*low\s*fat',
        'from_garden' : r'\s*(from)?\s*garden\s*(or)?\s*(store)?',
        'life_water' : r'\s*life\s*water',
        'landes' : r'\s*landes',
        'liège' : r'\s*li(è|e)ge',
        'lactose_free' : r'\s*(lactose|milk)\s*free',
        'lanquetot' : r'\s*lanquetot',
        'quartered' : r'\s*quartered',
        'lomagne' : r'\s*lomagne',
        'white' : r'\s*white',
        'mirabelle' : r'\s*mirabelle',
        'mc_vities' : r'\s*mc\s*vities',
        'marinated' : r'\s*marinated',
        'milled' : r'\s*milled',
        'madiran' : r'\s*madiran',
        
        'maltese' : r'\s*maltese',
        'scamorza' : r'\s*scamorza',
        'maggi' : r'\s*maggi',
        'aroma_flavor' : r'\s*aroma\s*flavor',
        'muscadet' : r'\s*muscadet',
        'morteau' : r'\s*morteau',
        'maldon' : r'\s*maldon',
        'melting' : r'\s*melting',
        'morello' : r'\s*morello',
        'mascobado' : r'\s*mascobado',
        'moselle' : r'\s*moselle',
        'molded'  : r'\s*molded',
        'malibu' : r'\s*malibu',
        'myrtle' : r'\s*myrtle',
        'madeira' : r'\s*madeira',
        'my_andros' : r'\s*my\s*andros',
        'margate' : r'\s*margate',
        'morgate' : r'\s*morgate',
        'muesli' : r'\s*muesli',

        'magnificat' : r'\s*magnificat',
        'mont_élimar' : r'\s*mont\s*(é|e)limar',
        'miscellaneous' : r'\s*miscellaneous',
        'measure' : r'\s*measure',
        'macerated' : r'\s*macerated',
        ''
        'old_nick' : r'\s*old\s*nick',
        'old_el_paso' : r'\s*old\s*el\s*paso',
        'old' : r'\bold\b\s*(fashioned|style)?\s*(brown\s*agricultural)?',
        'duxelles' : r'\s*duxelles',
        'maille' : r'\s*maille',
        'martini®' : r'\s*martini®?',
        'madras' : r'\s*madras',
        'maitre_coq' : r'\s*ma(î|i)tre\s*coq',
        'mont_blanc' : r'\s*mont\s*blanc',
        'montb_eliard' : r'\s*montb\s*(é|e)liard',
        'regular' : r'\s*regular',
        'mikados' : r'\s*mikados',
        'meaux' : r'\s*meaux',
        'melun' : r'\s*melun',
        'milly' : r'\s*milly',
        'miniature': r'\s*miniature',
        'rmandy': r'\s*rmandy',
        'markal': r'\s*markal',

        'medjool': r'\s*medjool',
        'mejhoul': r'\s*mejhoul',
        'if_needed': r'\s*if\s*needed',
        'melfort': r'\s*melfort',
        'milk_fed': r'\s*milk_fed',
        'natali': r'\s*natali',
        'nampla': r'\s*nampla',
        'nicaraguan': r'\s*nicaraguan',
        'ethiquable': r'\s*ethiquable',
        'negrita': r'\s*n\s*(e|é)grita',
        'napoleon_bigarreau': r'\s*napoleon\s*bigarreau',
        'neutral': r'\s*neutral',
        'nutritional': r'\s*nutritional',
        'nat_and_vie': r'\s*nat\s*(&|and)\s*vie',
        'oriental': r'\s*oriental',
        'ossau_valley': r'\s*ossau\s*valley',
        'over': r'\s*over\b',
        'studded': r'\s*studded',

        'arcachon': r'\s*arcachon',
        'roscoff': r'\s*roscoff\s*(style)?',
        'pink': r'\s*pink',
        'powdered': r'\s*powdered',
        'plain': r'\s*plain',
        'puffed': r'\s*puffed',
        'pralinoise': r'\s*pralinoise',
        'praline': r'\s*praline',
        'in_syrup': r'\s*in\s*syrup',
        'prince_de_bretagne': r'\s*prince\s*de\s*bretagne',
        'p_érigord': r'\s*p\s*(é|e)rigord',

        'purslane': r'\s*purslane',
        'parma': r'\s*parma',
        'paris': r'\s*paris',
        'preserved': r'\s*preserved',
        'pm': r'\s*pm\b',
        'pre_hulled': r'\s*pre\s*hulled',
        'palm_dende': r'\s*palm\s*dend(ê|e)',
        
        'princess_amandine_dor_éoc': r'\s*princess\s*amandine\s*(dor\s*éoc)?',
        'up_to': r'\s*up\s*to',
        'irish': r'\s*irish\s*(product)?',
        
        'pickled': r'\s*pickled',
        
        'comt_é': r'\s*comt\s*(é|e)',
        'purple': r'\s*purple',
        'spreadable': r'\s*spreadable',
        'poached': r'\s*poached',
        'pressed': r'\s*pressed',
        'pyrenees_suckling': r'\s*pyrenees\s*(suckling)?',
        'giovanni_ferrari': r'\s*giovanni\s*ferrari',
        'portuguese': r'\s*portuguese',
        
        'parme': r'\s*parme(\'s)?\b',
        
        #Prepared
        "butcher" : r"prepared\s*by\s*(the)?\s*butcher",
        "prepare_before_recipe": r'\s*prepared?\s*before\s*recipe\b',
        'previously_prepared': r'\s*previously\s*prepared',
        "prepared" : r'\s*prepared',


        'pata_negra': r'\s*pata\s*negra',
        'parma': r'\s*parma',
        'thawed': r'\s*thawed',

        'panzani': r'\s*panzani',
        'poulain': r'\s*poulain',
        'bintje': r'\s*bintje',
        'pulverized': r'\s*pulverized',
        'pulco': r'\s*pulco',
        'unsweetened': r'\s*unsweetened',
        'sweetened' : r'\s*sweetened',
        'peppered': r'\s*peppered',
        'victoria': r'\s*victoria',
        'pe_tsai': r'\s*pe\s*tsai',
        'praline': r'\s*praline',
        'phare_deckmühl': r'\s*phare\s*d(’|\')eckm(ü|u)hl',
        'processed': r'\s*processed',
        'qs': r'\s*qs',
        'quai_sud': r'\s*quai\s*sud',
        'rocher': r'\s*(ferrero)?\s*rocher',

        'r_egilait': r'\s*r\s*égilait',
        'roquefort': r'\s*roquefort?',
        'riso_gallo': r'\s*riso\s*gallo',
        'reine_claude': r'\s*reine\s*claude',
        'rectangular': r'\s*rectangular',
        
        #'ros_e': r'\s*ros\s*(é|e)',
        
        
        'reduced': r'\s*reduced',
        'roquefort': r'\s*roquefort',
        'rian': r'\s*rian',
        'richesmonts': r'\s*richesmonts',
        'rigate': r'\s*rigate',
        'russian': r'\s*russian',
        'special': r'\s*special',
        'accompaniment': r'\s*accompaniment',
        'refrigerated': r'\s*refrigerated0V',
        'rivesaltes': r'\s*rivesaltes?',
        'lengthwise': r'\s*lengthwise',
        'overnight': r'\s*overnight',
        'remaining': r'\s*remaining',
        'regent\'s_parks': r'\s*regent\'s\s*parks',
        
        'if_possible': r'\s*if\s*possible',
        'rustica_marque_repere': r'\s*rustica\s*(marque)?\s*(rep(è|e)re)?',
        'greek': r'\s*greek',
        'that_you_will_have': r'\s*that\s*you\s*will\s*have',
        'soaking': r'\s*soaking',
        'soluble': r'\s*soluble',
        'nescaf_e': r'\s*nescaf\s*(é|e)',
        'st_mamet': r'\s*st\s*mamet',
        'full_fat': r'\s*full\s*fat',
        'semi_skim': r'\s*semi\s*skim',
        'ariak_e': r'\s*ariak\s*(é|e)',
        'strasbourg': r'\s*strasbourg',
        'knackis': r'\s*knackis',
        'puffed': r'\s*puffed',
        'puffed': r'\s*puffed',
        'puffed': r'\s*puffed',
        'puffed': r'\s*puffed',
        'puffed': r'\s*puffed',
        'puffed': r'\s*puffed',
        'puffed': r'\s*puffed',

        'powdered': r'\s*powdered',

    }
    modifier_patterns_to_json(modifier_patterns, "modifier_patterns.json")


if measurements:
    measurement_patterns = {
        #must be before cups
        'tea_cups':r'\btea\*cups?\b',
        "coffee_cup" : r'\s*coffee\s*cup',
        
        #normal
        'table_spoons'  : [
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
            r"(\s*t\s*b\s*spoon\s*s)\b"],

        'tea_spoons'    : [
            r"(?:t\.?s\.?p\.?\s*s?)\b",
            r"(?:t\.s)\b",
            r"(?:\btea ?spo?o?n?s?\b)",
            r"(?:|t\.?s\.?p\.?s?)\b",
            r"(?:tea s\.?p)\b",
            r"(?:\bt\s?s)\b",
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
            r"\s*(?:t\.spoonsful)\b"],

        
        'fluid_ounces'  :  [
            r"(?:fl(?:\.|uid)?[\s_]*oz|fluid[\s_]*ounce)\b",
            r"\s*(?:fluid\s*ounces)\b"],
        
        'ounces'        : r"\b(?:ounce|oz(?:\.|s)?)\b",
        'cups'          : r"\b[cC]\s*(ups?)?\.?\b",
        'quarts'        : r"\bqu?a?r?ts?\b",
        'pints'     : r'\b(?:pint|pt)s?\.?(?:\s|$)',
        'gallons'   : [
            r"\b(gallon|gal)[\s_]*(?:n(?:\.|s)?)?\b",
            r"\b(gallons|gals)[\s_]*(?:n(?:\.|s)?)?\b",
            r"\bgals\.\b"],
        
        'lbs'       :  [
            r"(pound|lb)[\s_]*(?:n(?:\.|s)?)?\b",
            r"lbs\b",
            r"lbs\.\b",
            r"pounds\b"],
            
        'milli_liters'  : [
            r"\bmilliliter\b",
            r"\bmilliliters\b",
            r"\bml\b",
            r"\bmls\b",
            r"\bmls\.\b"],
        
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
        'glass'            : r'\bglass(es)?',
        'jars'           : r'\b(jars?)\b',
        'nests'          : r'\bnests?\b',
        'no.s'            : r'\bno(\.?\b|°)\s*',
        'pots'           : r'\bpots?\b',

        #36
        #'gr'        : r'\b(gr|grams?)\b',
        'servings'   : r'\bservings?\b',
        'stalks'     : r'\bstalks?\b',
        'sticks'     : r'\bsticks?\b',
        #kg' = r' kg(s?) '

        #41
        'logs'       : r'\blogs?\b',
        #'legs'       : r'\blegs?\b',
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
        'pkgs' : r'\b(doy)?\s*(pkgs?|packages?|packets?|packs?)\b',
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
    
        'per_persons' : r'\s*(for\s*(each\s*)?person|per\s*persons?)\s*',
        'heaping_spoonfuls' : r'\s*heaping\s*spoonfuls?\b',
        #'weights' : r'\s*weighting\s*',
        #not tested
        'bags'  : r'\bbags?\b',
        'boxes'  : r'\bboxe?s?\b',
        'heaped'  : r'\bheaped\b',
        'bowl' : r'\s*bowl\s*of\b',
        'base' : r'\s*base\s*of\b',
        'block' : r'\s*block\s*of\b',
        'bottle' : r'\s*bottles?\b',
        'branches' : r'\s*branche?s?\b',
        'tablets' : r'\s*tablets?\b',
        'carton' : r'\s*carton\b',
        'puree' : r'\s*puree\b',

        'grain': r'\s*gr\b',
        #experimental
        'percent_fat': r'\s*percent\s*fat',
        'percent': r'\s*percent',
        'piece' : r'\s*piece\b',
        'container' : r'\s*container\b',
        "case" : r'\s*case\b',
        "carmine" : r'\s*carmine\b',
        "cork" : r'\s*cork\b',
        "capsule" : r'\s*capsule\b',
        "drizzle" : r'\s*drizzle\b',
        'dose' : r'\s*dose\b',
        'slices' : r'\s*slices?\b',
        'blocks' : r'\s*blocks',
        'doses' : r'\s*doses',

        'dices' : r'\s*dices',
        'hint' : r'\s*hint',
        'head' : r'\s*heads?\b',
        'knife_tip' : r'\s*knife\s*tip',
        'ladle' : r'\s*ladle(ful)?',
        'measure' : r'\s*measure',
        'plate' : r'\s*plate',
        'turns_mill' : r'\s*turns\s*(mill)?',
        'quantity' : r'\s*quantity',
        'sachet' : r'\s*sachet',
        
        
        #needs to be last
        'self_count' : r'\b',
        

    }
    measurements_to_json(measurement_patterns, "measurement_patterns")


    


