import requests

import random

#pick pkmn needs to be happning in the background first, to pull a no for the pkmn

def pick_pkmn (): #auto picking pkmn
    #generate random number btwn 1-151
    pkmn_id = int(random.random()*151)+1
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pkmn_id}/")
    pkmn = response.json()
    # pull from no pkmn API
    top_trumps = {'name': pkmn['name'], 'id': pkmn['id'], 'height': pkmn['height'], 'weight': pkmn['weight'],
                  'xp': pkmn['base_experience'], }

    return (top_trumps)


print('Welcome to the world of Pokemon\n')

my_pkmn = pick_pkmn()
print(f"You chose {my_pkmn['name']}".title())  ##i want this to be better formatted ie pkmn name in title case

#using XP instead of ID as im a nerd

#limit the user input to avoid mess ups
allowed_stats = ['height', 'weight', 'xp']
stat = input('Which stat will you pick? Height, Weight, or XP? \n').lower()
while stat not in allowed_stats:
    stat = input('Which stat will you pick? Height, Weight, or XP? \n').lower()

#classic rival
gary_oak = pick_pkmn()

my_team = my_pkmn[stat]
garys_team = gary_oak[stat]


print(f"\nYour rival chose {gary_oak['name']}".title())

if my_team > garys_team:
    print("Congrats Champ - you win".title())
elif garys_team > my_team:
    print("Your team got wiped out!".title())
else:
    print("Draw!")

print('\nPress run to play again'.title())

##can i loop it for multiple rounds??
