import random

# Get the hero's name as input.
hero = input("Please enter your hero's name: ")
health = 10
trolls = 0
damage = 3
coins = 0

# Start a loop that continues while the hero's health is greater than 0.
while health > 0:
    # Generate a random event (a number between 1 and 10).
    event = random.randint(1, 10)

    # Check different events based on the randomly generated number.
    if event == 1:
        print(hero, "falls off a cliff and takes", health, "damage points.\n")
        health = 0  # Set health to 0 when the hero falls off a cliff.

    # A simple use of 'and' to tell if a number is between two other numbers (2 to 8).
    elif 2 <= event <= 8:
        trolls += 1
        health -= damage
        coins += 1
        print(hero, "swings and defeats an evil troll, but takes", damage, "damage points.\n")

    # Check if the event is 9 and some conditions are met (coins and trolls).
    elif event == 9 and (coins > 10 or trolls > 20):
        print(hero, "finds an Inn and pays for a room, healing", health, "health points.\n")
        if health > 11:
            health = 10  # Ensure health doesn't go above the maximum value (10).

    # Check if the event is 9.
    elif event == 9:
        print(hero, "finds an Inn and can't pay for a room, healing no health points.\n")

    # Check if the event is 10 and whether the hero has enough coins.
    elif event == 10:
        print(hero, "finds a wizard who offers a reward for those worthy!")
        if coins > 10:
            print("The wizard finds you Worthy!")
            coins -= 10
            damage -= 1
        else:
            print("The wizard finds you not Worthy!")

    else:
        print(hero, "messes with probability and explodes")

# The game loop ends when the hero's health is 0 or less.

"""
# calculating number of trolls defeated without loops
trolls = int(health/damage + 1)
print(hero, "fought valiantly and defeated", 
        trolls, "trolls.")
print("But alas, your hero is no more.") 
"""


"""
#first one
while health > 0:

    trolls += 1
    health -= damage
    
    print (hero, " swings and defeats an evil troll," 
    "but takes", damage, "damage points.\n")
    
print(hero, "fought valiantly and defeated", 
        trolls, "trolls.")
print("But alas, your hero is no more.") 
"""