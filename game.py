from player import Player
from location import World

def get_valid_input(prompt, valid_options):
    """Get valid input from user, retrying if invalid."""
    while True:
        user_input = input(prompt).lower().strip()
        if user_input in valid_options:
            return user_input
        else:
            print(f"Invalid input. Please try again. Valid options: {', '.join(valid_options)}")

def race_print(race):
        if race == 'whit':
            print('easy choice')
            health = 100
            print('Health =', health)
        elif race == 'blat':
            print('You chose a life of hardship')
            health = 1
            print('Health =', health)
        elif race == 'asi':
            print('This race has low visibility, your health is lower')
            health = 75
            print('Health =', health)
        elif race == 'mex':
            print('SIRENS')
            print('Sigh, you have been caught by ICE, GAME OVER')
            health = 0
            print('Health =', health)
        else: #makes it bullet proof
            print("Invalid race")

print('Hello, welcome to the game')

name = input('What is your name?')
print('Hi', name)

print('Race options: whit, blat, asi, mex')
race = get_valid_input('Select a race: ', ['whit', 'blat', 'asi', 'mex'])
race_print(race)
if race == 'mex':
    print('GAME OVER')
    exit()#game over

current_location = 'panda express'#where the player starts
location = World[current_location]

print(f'You are in {location["name"]}')
print(location["description"])#description of the location
print('Unlocked items:')
print(location["items"])#starting item

input('To leave Panda Express, press Enter')
current_location = 'ghetto'
location = World[current_location]
print(f'You are in {location["name"]}')
print(location["description"])
print('Unlocked items:')
print(location["items"])
gun_choice = get_valid_input('Do you want to shoot the gun at the homeless? (y/n) ', ['y', 'n'])
if gun_choice == 'y':
    print('You shot the gun at the homeless')
    print('The homeless is dead')
    print('You are now a murderer')
    print('Have fun in prison, killer')

elif gun_choice == 'n':
    print('You do not shoot the gun at the homeless')
    print('The homless take your things')
    print('You are now poor, was being nice worth it?')
    print('GAME OVER')
    exit() #game over

current_location = 'prision'
location = World[current_location]
print(f'You are in {location["name"]}')
print(location["description"])
print('find the key to the warden\'s office, to leave the prision')

print('You notice a bar of soap in your cell')
print('You can pick up the bar of soap, but you notice a rather large man on the top bunk')
print(location["hazards"])
soap_choice = get_valid_input('do you want to pick up the bar of soap? (y/n) ', ['y', 'n'])

if soap_choice == 'y':
    print('You pick up the bar of soap')
    print('You use the bar of soap to clean yourself')
    print('You feel refreshed')
    print('You notice a key on the floor')
    print('You pick up the key')
    print('You use the key to open the door')
elif soap_choice == 'n':
    print('You do not pick up the bar of soap')
    print('You do not clean yourself')
    print('You do not notice a key on the floor')
    print('You do not pick up the key')
    print('You do not use the key to open the door')
    print('You do not enter the portal')
    print('GAME OVER')
    exit() #game over

current_location = 'wardens office'
location = World[current_location]
print(f'You are in {location["name"]}')
print(location["description"])
print('You notice a guard in the hallway')
print('You can either:')
print('1. Give the guard the bar of soap')
print('2. Try to unlock the locked door to a portal')
choice = get_valid_input('Do you want to give the guard the bar of soap? (y/n) ', ['y', 'n'])
if choice == 'y':
    print('You give the guard the bar of soap')
    print('The guard is friends with big fella on top bunk, and knows him personally')
elif choice == 'n':
    print('You try to unlock the locked door to a portal')
    print('the door is unlocked, and you enter the portal')


    current_location = 'garden'
    location = World[current_location]
    print(f'You are in {location["name"]}')
    print(location["description"])
    print('Unlocked items:')
    print(location["items"])
    print('You made it to the garden')
    print('You notice a large panda eating a cheesey gordita crunch')
    print('Ask the panda for the cheesey gordita crunch')
    panda_choice = get_valid_input('Do you want to ask the panda for the cheesey gordita crunch? (y/n) ', ['y', 'n'])
    
    if panda_choice == 'y':
        print('The panda gives you the cheesey gordita crunch')
        print('You eat the cheesey gordita crunch')
        print('You feel refreshed')
        print('Congrats, enjoy your cheesey gordita crunch')
        exit() #game over

    elif panda_choice == 'n':
        print('You do not ask the panda for the cheesey gordita crunch')
        print('You do not eat the cheesey gordita crunch')
        print('You do not feel refreshed')
        print('GAME OVER')
        exit() #game over

   
   




