from player import *


# Creating players
player_one = Player('Pat', 'samurai')
player_two = Player('Ethan', 'wizard')
player_three = Player('Odion', 'ninja')

# printing player one data
print(player_one)
print(player_one.warrior)

# player one attacks
player_one.warrior.attack(player_three)
