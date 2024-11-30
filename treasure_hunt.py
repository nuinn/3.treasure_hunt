print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction = input("You come to a cross roads. Would you like to go left L or right R? ")
if direction == 'L':
  water = input("You come to river. Will you 'swim' or 'wait' for a boat? ")
  if water == "wait":
    door = input('A boat comes and takes you to an island. There is a long wall with three doors: "red", "yellow" or "blue". Which do you choose? ')
    if door == 'yellow':
      print('There\'s the treaure! Oooh, so pretty!! Congratulations, you win!')
    elif door == 'red':
      print('A fireball burns you alive. Game over')
    elif door == 'blue':
      print('A bear swipes at you and beheads you. Game over obviously.')
    else:
      print('That was not an option. You die! Game over.')
  else:
    print('The current overwhelms you and your are swept towards an enormous waterfall. You fall for a long time before hitting some rocks. Game over.')
else:
  print('You see a flash of orange and white, before being overcome by a vicious beast. Game over.')
