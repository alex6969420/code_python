#import statement
from random import randrange

#input
difficulty = int(input("Enter the DC: "))

#processing & output
player_roll = randrange(1,21)
print(f"the player has rolled {player_roll} on their D20")
if player_roll >= difficulty:
    print(f"Player was successful as {player_roll} >=  {difficulty}.")
else:
    print(f"Player was not successful as {player_roll} < {difficulty}")
