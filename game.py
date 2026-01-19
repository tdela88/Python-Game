from player import Player

def race_print(self, race):
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
race = input('Select a race: ')
race_print(race)

# if race == 'whit':
#     print('easy choice')
#     health = 100
#     print('Health =', health)
# elif race == 'blat':
#     print('You chose a life of hardship')
#     health = 1
#     print('Health =', health)
# elif race == 'asi':
#     print('This race has low visibility, your health is lower')
#     health = 75
#     print('Health =', health)
# elif race == 'mex':
#     print('SIRENS')
#     print('Sigh, you have been caught by ICE, GAME OVER')
#     health = 0
#     print('Health =', health)







