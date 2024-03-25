import re
import initial_check as ic

modifier_patterns = {
    #General can be added anywhere so not specific enoguh 

    #not need words
    #"of" :r'\s*of\s*',

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
    "light": r'\blight\b',
    "heavy": r'\s*heavy\b',
    "crystallized" : r'\s*crystallized\b',


    #the un group not finished
    "untreated" : r'\s*untreated\b',
    "unpeeled" : r'\s*unpeeled\b',
    "unrefined" : r'\s*unrefined\b',

    "degerminated" : r'\s*deger(minated|med)\b',
    "defatted" : r'\s*defatted\b',
    "desalinated": r'\s*desalinated\b',
    "deboned": r'\s*deboned\b',

    "rinsed": r'\s*rinsed\b',
    
    
    "skewered": r'\s*skewered\b',#skewers
    "on_the_bone": r'\s*on\s*the\s*bone\b',
    "naturally_salted": r'\s*naturally\s*salted\b',
    "semi_salted": r'\s*semi\s*salted\b',
    'demi_salted' : r'\s*demi-?\s*salted',
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
    "finely" : r'\s*finely\b',

    "finely_cut" : r'\s*finely\s*cut',

    #"slices"    :r'\s*slices?\b',
    "thinly_sliced" :r'\s*thinly\s*sliced\b',
    "sliced" :r'\s*sliced\b',

    "thick" : r'\s*thick\b',
    "thin" : r'\s*thin\b',

    "grated": r'\s*grated\b',
    "ground": r'\s*ground\b', #r'\s*freshly\s*ground\s*flavor\b'
    "smoked": r'\bsmoked\b',


    "keep_the_water_inside" : r'\s*keep\s*the\s*water\s*inside\b',
    "in_the_oven_remove" : r'\s*(in)?\s*(the)?\s*oven\s*remove\b',

    
    "well_done": r'\s*well\s*done\b',
    "leftover": r'\s*left\s*over\b',
    "pricked": r'\s*pricked\b',
    "oven_roasted": r'\s*oven\s*roasted\b',
    "roasted" : r'\s*roasted',
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
    "cubes"     :r'\s*(in)?\s*cubes?\b',
    "quarters"  :r'\s*quarters?\b',
    "strips"    :r'\s*(in)?\s*strips?\b',
    "pieces"    : r'\s*in\s*pieces?\b',
    #two\s*sections
    "sections"  :r'\s*sections?\b',
    
    "fine_julienne"   :r'\s*fine\s*juliennes?\b',
    "thin_round" :r'\s*thin\s*rounds?\b',
    "wedges"        :r'\s*wedges?\b',
    "chunks"    :r'\s*chunks?\b',
    "even_portions"       :r'\s*(even)?\s*portions?\b',
    "sticks"    :r'\s*sticks?\b',
    #bite-sized
    "bite-sized_pieces"   :r'\s*bite-?\s*sized\s*pieces?\b',
    #half
    #5mm


    #Prepared
    "butcher" : r"prepared\s*by\s*(the)?\s*butcher",
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
    "cooking": r'\s*(for)?\s*cook(ing)?\b',

    "for_finishing": r'\s*for\s*finishing\b',
    "for_presentation": r'\s*for\s*presentation\b',
    "for_those_who_like_it": r'\s*for\s*those\s*who\s*like\s*it\b',

    #variations
    "to_taste": r'\s*(according)?\s*(to)?\s*(taste)?\s*(your)?\s*(desires?)\s*', # precooking without
    "variation" : r'\s*(of)?\s*variation\b',
    "depending" : r'\s*(of)?\s*depending\b',
    "optional"  : r'\s*(of)?\s*optional:?\b',
    "decoration": r'\s*(as)?\s*decorat(e|ions?|ive)(\s*(of)?\s*choice)?(elements?)\s*',
    
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
    
    'smoked'  : r'\s*smoked \b',
    'salt-preserved'  : r'\s*salt-?\s*preserved\b',
    'at_room_temperature' : r'\s*at_?\s*room_?\s*temperature\b',
    'authentic' : r'\s*authentic\b',

    'in_half_lengthwise' : r'\s*in\s*half\s*lengthwise\b',
    'around' : r'\s*\(?around\)?\b',
    'aged' : r'\s*aged\b',
    'amora' : r'(\s*croq\'vert)?\s*amora\b',
    'beautiful' : r'\s*beautiful\b',
    'lots_black_spots' : r'\s*lots\s*black\s*spots\b',
    'blanched' : r'\s*blanched\b',
    'finely' : r'\s*finely\b',
    'beaten' : r'\s*beaten\b',
    "beautiful" : r"\s*beautiful\b",
    "basic_elements" : r"\s*basic\s*elements\b",
    #beaten_salted_and_peppered_egg_(_milk_or_liquid_cream)
    'boiling' : r"\s*boiling\b",
    #"bitter" : r"\s*bitter\b",
    'pureed' : r"\s*pureed\b",
    "from_garden" : r"\s*from\s*garden\b",
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

    
    "from_garden" : r"\s*from\s*(the)?\s*garden\b",
    "ripe_but_firm" : r"\s*ripe\s*but\s*firm\b",
    "bonne_maman" : r"\s*bonne\s*maman\b",
    "cored" : r"\s*cored\b",
    "roughly" : r"\s*roughly\b",
    #"suit_your_taste" : r"\s*suit\s*your\s*taste\b*",
    "cleaned" : r"\s*cleaned\b",
    "coarse" : r"\s*coarse\b",

    "country-style" : r"\s*country-style\b",
    "country" : r"\s*country\b",

    "philadelphia_type" : r"\s*philadelphia\s*type\s*",
    "drained" : r"\s*drained\b",
    "crumbled" : r"\s*crumbled\b",
    "spread" : r"\s*spread\b",

    "philadelphia": r"\s*philadelphia\b",
    "st-Morêt" : r"\s*st-?\s*morêt\b",  
    "kiri" : r"\s*kiri\b",
    #temps not included lol
    "cold" : r"\s*(very)?\s*cold\b",

    "catalan" : r"\s*catalan\b",
    "maizena" : r"\s*maizena\b",
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

    "around" : r"\s*around\b",
    "decoration" : r"\s*decoration\b",
    "blackcurrant" : r"\s*blackcurrant\b",
    "whipping" : r"\s*whipping",
    "st sever" : r"\s*st\s*sever",
    "cooking" : r"\s*cooking\b",
    "cathedral city" : r"\s*cathedral\s*city\s*",
    "mature" : r"\s*mature",
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
    'better_than_milk' : r'\s*better\s*than\s*milk',
    'zest' : r'\s*zest',
    'each' : r'\s*each\b',
    'bjorg' : r'\s*bjorg',
    'mild' : r'\s*mild',
    'sharp' : r'\s*sharp',
    'freshly_squeezed' : r'\s*freshly\s*squeezed\b',
    'danette' : r'\s*danette',
    'charlotte_red_label' : r'\s*charlotte\s*red\s*label',
    'p_erigord' : r'p\s*érigord',
    'glazed' : r'\s*glazed',
    'puree' : r'\s*puree',
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
    "semi_salted" : r"\s*semi\s*salted",
    "salted" : r"\s*salted!?",
    "cubed" : r"\s*cubed",
    "i_didn't_have_any" : r'\s*i\s*didn\'t\s*have\s*any',
    "in_shoulder" : r'\s*in\s*(the)?\s*shoulder',
    "corsican_canestrelli" : r'\s*corsican\s*canestrelli',
    "clarified" : r'\s*clarified',
    "cornicabra" : r'\s*cornicabra',
    "from_spain" : r'\s*from\s*spain',
    "candia" : r'\s*candia\s*baby',
    "from_your_poultry_store" : r'\s*(from)?\s*(your)?\s*poultry\s*store',
    "cleaned" : r'\s*cleaned',
    "cassegrain" : r'\s*cassegrain',
    "crumbs" : r'\s*crumbs?\b',
    "colored" : r'\s*colored',
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
    'flavor' : r'\s*flavor',
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
    'south_west' : r'\s*south\s*west'

    #'deger' : r'\s*deger\b'
  


    
 

 

    
    #"croq'vert" : r'\s*croq\'vert\s*'



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
    found_modifier = False

    for filter_name, filter in modifier_patterns.items():
        #print(filter_name)
        found_modifier, cleaned_text = ic.check_modifier(filter, cleaned_text)
    
        if found_modifier:
            cauhgt_values.append(filter_name)

    return cauhgt_values, cleaned_text

def filter_check_specified(filter_name, text):

    print(text)
    filter = modifier_patterns[filter_name]
    return ic.check_modifier(filter, text)

    




    