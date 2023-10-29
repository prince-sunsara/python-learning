'''
SNAK WATER GUN
    > Snake, Water and Gun is a variation of the children's game "rock-paper-scissors" where players use hand gestures to represent a snake, water, or a gun. 
    > The gun beats the snake, the water beats the gun, and the snake beats the water. 
    > Write a python program to create a Snake Water Gun game in Python using if-else statements. 
    > Do not create any fancy GUI. Use proper functions to check for win.
'''
import random

def check(comp, user):
    if(comp == user):
        return 0
    elif(comp == 0 and user == 1):
        return -1
    elif(comp == 1 and user == 2):
        return -1
    elif(comp == 2 and user == 0):
        return -1
    else:
        return 1

comp = random.randint(0, 2)
user = int(input("0 for Snake,1 for Water and 2 for Gun: "))

score = check(comp, user)

print("You: ", user)
print("Comp: ", comp)

if(score == 0):
    print("Match Draw!")
elif(score == 1):
    print("User wins")
else:
    print("Computer wins.")