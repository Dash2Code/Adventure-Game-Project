import time
import random

creatures = ['Dragon', 'Werewolf', 'Troll', 'Demogorgon', 'Ogre', 'Goblin',
             'Chimera', 'Dark fairy']
weapons = ['Sword of Ogoroth', 'Mjölnir', 'Sword of Surtr', 'Excalibur',
           'Foul Axe', 'Lightning Axe', 'Heartstring Bow and Arrow']

random_creature = random.choice(creatures)
random_weapon = random.choice(weapons)


# This function prints messages (with pauses) and is used throughout the game.
def print_pause(message_to_print, seconds_to_delay):
    print(message_to_print)
    time.sleep(seconds_to_delay)


# This function defines the introduction and sets the scene for the game.
# Input parameter is an 'items' list which contains items the user collects.
def intro(items):
    print_pause("You walk into a castle and find yourself in a lightly "
                "dimmed hallway.", 2)
    print_pause("The castle seems haunted ...", 2)
    print_pause("On the left, you see stairs leading up to the tower.", 2)
    print_pause("To your right, there are stairs that lead down to the "
                "dungeon.", 2)
    print_pause("And straight ahead, you see a large wooden door to another "
                "room.", 2)
    print_pause("In your hand you hold your trusty (but not very effective) "
                "dagger.\n", 2)
    items.append('Dagger')


# This function defines what happens when the user is at the door of the tower.
# If the user has the tower key then they get access to the powerful weapon.
# Else if the user has the powerful weapon, they've already already been here.
# Otherwise, the door is locked and the user cannot gain access to the tower.
# Input parameter is an 'items' list which contains items the user collects.
def tower(items):
    place = "tower"
    print_pause("You walk up the winding stairs until you reach a door.", 2)
    if 'Tower Key' in items:
        print_pause("The door appears locked.", 2)
        print_pause("Luckily, the castle owner gave you the key to unlock the "
                    "Tower door!", 2)
        items.remove('Tower Key')
        print_pause("You open the door and see Merlin!", 2)
        print_pause("He eagerly looks up and sees that you have finally "
                    "arrived!", 2)
        print_pause("He says that he has been expecting you all night and "
                    "wasn't sure if you'd show up!", 3)
        print_pause("He finishes up his magic potion and asks for you to take "
                    "out your tiny dagger.", 3)
        print_pause("He pours the magic potion over the tiny dagger and it "
                    f"magically turns it into a powerful {random_weapon}.", 3)
        items.remove('Dagger')
        items.append(random_weapon)
        print_pause(f"Merlin explains that the {random_weapon} is used to "
                    f"defeat the {random_creature}!", 3)
        print_pause("Merlin's last words is let the light shine brightly on "
                    "you.", 2)
    else:
        if random_weapon in items:
            print_pause("The door is opened.", 1)
            print_pause("You've been here before ... Merlin informs you "
                        "there's nothing else he can give you.", 2)
            print_pause("Merlin says you are the chosen one to fight the "
                        f"{random_creature}!", 2)
        else:
            print_pause("The door appears locked.", 2)
            print_pause("Unfortunately, you don't seem to have the key.", 2)
    hallway(items, place)


# This function defines what happens when the user is in the dungeon.
# Depending on what item the user has, a certain scenario is played out.
# Input parameter is an 'items' list which contains items the user collects.
def dungeon(items):
    place = "dungeon"
    print_pause("You walk down the winding stairs and continue to walk the "
                "dungeon path.", 2)
    print_pause("You see a door about a metre ahead of you.", 2)
    print_pause("You approach the door and daringly turn the knob.", 2)
    print_pause(f"Eep! The {random_creature} lives at the bottom of the "
                "castle!", 2)
    print_pause(f"The {random_creature} attacks you!", 2)
    if 'Dagger' in items:
        print_pause("You feel a bit under-prepared for this, what with only "
                    "having a tiny dagger.", 3)
    dungeon_actions(items, place)
    play_again()


# This function defines the various scenarios when the user is in the dungeon.
# If the user chooses to fight and has the powerful weapon, they can defeat the
# creature. Else if the user chooses to fight and has the dagger, they lose.
# If the user chooses to runaway, they have a second chance to play the game
# without restarting.
# Otherwise, if the users picks an option other than 1 or 2, they will be asked
# again to pick 1 or 2.
# Input parameter is an 'items' list which contains items the user collects.
def dungeon_actions(items, place):
    response = input("Would you like to (1) Fight (2) Run away?\n")
    if response == '1':
        if random_weapon in items:
            print_pause(f"As the {random_creature} moves to attack, you "
                        f"unsheath your new {random_weapon}.", 2)
            print_pause(f"The {random_weapon} with all its magical powers is "
                        "in your hand as you brace yourself for the "
                        "attack.", 3)
            print_pause(f"You take a few strikes using your {random_weapon} "
                        f"and weaken the {random_creature}.", 3)
            print_pause(f"The {random_creature} falls to the ground.", 2)
            print_pause("You are victorious!", 2)
        elif 'Dagger' in items:
            print_pause("You do your best with what you have...", 2)
            print_pause("but your dagger is no match for the "
                        f"{random_creature}.", 2)
            print_pause("You have been defeated!", 2)
    elif response == '2':
        hallway(items, place)
    else:
        dungeon_actions(items, place)


# This function defines the scenarios when the user is in the room.
# If the user has the tower key, they will be informed they were already here.
# Else if the user has the powerful weapon, they will be asked to save the day.
# Otherwise, the user will be handed a key to the tower.
# Input parameter is an 'items' list which contains items the user collects.
def room(items):
    place = "room"
    print_pause("You walk straight towards the large wooden door.", 2)
    print_pause("You open the door ... and see a frightened person inside.", 2)
    if 'Tower Key' in items:
        print_pause("You've been here before, and the castle owners pleads "
                    "with you to get help quickly!", 3)
    elif random_weapon in items:
        print_pause("You've been here before, and the castle owners is "
                    "pleased you've sort help from Merlin!", 2)
        print_pause(f"He says for you to hurry as there's not much time "
                    "at hand!", 3)
    else:
        print_pause("He tells you that he is the castle owner, too "
                    "frightened to roam the castle after sundown.", 3)
        print_pause("He informs you that the rumours are true! "
                    f"The {random_creature} is lurking the castle and has "
                    "scared away most people!", 3)
        print_pause("The castle owner hands you a key to the castle "
                    "tower.", 2)
        items.append('Tower Key')
        print_pause("He informs you that Merlin has returned and is now "
                    "waiting for you in the Tower!", 2)
    hallway(items, place)


# This function is used to determine the next action depending on the user
# location.
# Input parameter is an 'items' list which contains items the user collects.
def hallway(items, place):
    if place == 'dungeon':
        print_pause("You run back upstairs to the castle hallway. "
                    "Luckily, you don't seem to have been followed.\n", 2)
    elif place == 'room':
        print_pause("You run back out to the hallway.\n", 2)
    elif place == 'tower':
        print_pause("You run back downstairs to the castle hallway.\n", 2)
    adventure_game(items)


# This function requests input to determine where the user would like to go.
# Input parameter is an 'items' list which contains items the user collects.
def adventure_game(items):
    print_pause("Enter 1 to take the stairs up to the tower.", 1)
    print_pause("Enter 2 to take the stairs down to the dungeon.", 1)
    print_pause("Enter 3 to walk to the room on the same floor.", 1)
    print_pause("What would you like to do?", 0)
    response = input("(Please enter 1, 2 or 3 only)\n")
    if response == '1':
        tower(items)
    elif response == '2':
        dungeon(items)
    elif response == '3':
        room(items)
    else:
        adventure_game(items)


# This function requests input to determine where the user would like to play
# the game again.
def play_again():
    response = input("Would you like to play again? (y/n)\n")
    if response == 'y':
        print_pause("Excellent! Restarting the game ...", 2)
        play_adventure_game()
    elif response == 'n':
        print_pause("Thanks for playing! See you next time!", 2)
    else:
        play_again()


# This function defines the items list, calls the intro and adventure game
# functions.
def play_adventure_game():
    items = []
    intro(items)
    adventure_game(items)


play_adventure_game()
