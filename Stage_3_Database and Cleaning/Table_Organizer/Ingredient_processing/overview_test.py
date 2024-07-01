
import re

import os
import sys

from process_ingredient import raw_translated_ingredient





full_process_specific_test = True

if full_process_specific_test:

    #folder = "\Database and Cleaning\Table_Organizer\\test_cases\measurements_cleaning\general_test.csv"
    #ic.overall_test_measurements_enhanced(os.getcwd() + folder)]

    #text = "5 cans of natural tuna"
    #text = "24 oz 5 cans of natural large tuna"
    #text = "1 - 7 large apples"
    #text = "a tablespoon of something"
    #text = "chair"
    #text =  "sliced ​​smoked salmon"
    
    #need fixing
    #remove U+200b
    #text = "5 tbsp sugar"
    #text = "3 tbsp. to s. Amora ketchup"
    #text =  "20ml milk"
    text =  "1kg white spanish melon"
    
    #text =  "10cl of white wine"
    #text =  "1l of chicken stock"

    #text =  "1 c. to c. level(s) of baking powder"
    #text =  "4 tbsp. to s. sweetened condensed milk"
    #text =  "500g_fresh_peas_(_175g_shelled)"
    #text =  "8 tbsp. to c. orange marmalade"
    #text =  "1 c. to c. vanilla extract or liquid vanilla"
    #text = "8 pats of butter"
    #text = "1 tsp sage"
    #text = " an apple"
    #text = "beautiful_pepper_(.amount)"
    #text = "5 beautiful tomatoes to stuff"
    #text = "200g bread flour (I used the Valpiform Bread and Pastry Mix) + a small quantity to knead the dough correctly"
    #text = "1 doy pack poiscassés-courgettes Bjorg"
    #text = " 4 sandwich bread bars"
    #text = "cooking_soy_sauce_"
    #text = "chocolate_(_decoration)_or_coconut"
    #text = "cooking_apple"
    #text = "chocolate_lemon_zest_decorate"
    #text = "1/2 bag of couscous with sweet Tipiak spices (125 gr)"
    #text = "210 g of cream cheese (St Morêt, Philadelphia type, etc.)"
    #text = "3 x 20g caster sugar"
    #4594
    #text = "50 g of cocoa paste (100% cocoa)"
    #text = "chocolate shavings (to make by grating chocolate with a peeler)"
    #text = "a little chocolate (a small handful of pistoles was enough for me)"
    #text = "1/2 l of Carte d’Or® Dark Chocolate Ice Cream"
    #text = "2 tbsp. to s. unrefined cane sugar (complete)"
    #text = "4 tbsp. to s. level of complete/integral sugar"
    #text = "½ l of very cold thick whole crème fraîche (30 or 35%)"
    
    #broken
    #text = "8 chicken drumsticks or 10 or a whole chicken to cut into pieces"
    
    #continued
    #text = "1 liter of custard and a dozen macaroons for decoration"
    #text = "250g blanched or ground almonds"
    #text = "90g butter or margarine"
    #text = "1 jar of Bonne Maman Blueberry and blackcurrant Jam"

    #text = "100 g of chocolate: I used Newtree cherry chocolate which delicately flavors the cupcake and goes wonderfully with a sweet tooth! but you can use the chocolate of your choice!"    
    #6124
    #Awful 
    #text = "1 container of 250 g of Philadelphia cream cheese (if you cannot find this cheese, replace it with mascarpone to which you add a few drops of lemon juice)"
    #text = "1 cup (237 ml) heavy cream (15% country-style or 35% whipping)"
    #1831
    #text = "1 box of 350g Cassegrain button mushrooms with chestnuts, boletes, porcini mushrooms and parsley"
    #giving and 
    #text = "250g pitted cherries (around thirty) + a few for decoration"
    #text = "2 confit duck legs or sleeves (in this case you need at least 6)"
    #text = "6 slices of chorizo ​​or 10 (if it's a little smaller)"
    #text = "5 apples or 7"
    #text = "chicken_or_(or_turkey)_breasts"
    #10154
    #text = "4 candied lemons or 2 lemons in pieces (just add the quarters without the white + a little grated peel)"
    #
    #text = "75 cl of chicken stock (15g of chicken stock and 75 cl of water)"
    #text = "800g chicken breasts, finely sliced ​​diagonally"
    #text = "2 pieces of chicken (1 for each person)"
    #text = "some candied citrus zest and/or diced candied ginger for decoration"
    #text = "1 tsp cake yeast (for me gluten free)"
    #text = "3 packets of m&m's"
    #13464
    result_list = raw_translated_ingredient(text, True, False)
    count = 1
    for result in result_list:
        fmo, fme, text, mod_hash, name, portion, mpis, ignore_this = result
        
        print("modifiers:", fmo,", measurements:", fme,", text:", text, ", hash:", mod_hash,", name:", name, 
               ", portion:", portion, ", multi_part_ingredient_status:", mpis, ", ignore this:", ignore_this)
       
        count+=1
    
