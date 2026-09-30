import random

#valid input or not
def coordinates(a):
    if a.isdigit():
        return True
    else:
        print("Invalid coordinate")

#variables
guess = None
carCounter = 0
lineCounter = 0
BIGlist = []
mines = []

#main stuff
while True:
    x= input("Width: ")
    y= input("Height: ")
    
    if coordinates(x) and coordinates(y):

        totalSize = int(x)**int(y)
        print("To end the game type: end")
        x = int(x)
        while carCounter**lineCounter <= totalSize:
            if carCounter >= x:
                carCounter = 0
                lineCounter = lineCounter+1
            BIGlist.append("0 ")
            carCounter = carCounter+1
        guess = input("Guess a coordinate: ")
        numbers = [1, 2, 3]

   
    while guess == "flag":
        print("Type guess to guess")
         
        flag = input("Choose a flag cordinate: ")
        if flag in BIGlist:
            BIGlist[flag] = "F"
        elif flag == "guess":
            break
        guess = input("Guess a coordinate: ")
        

    if guess in mines:
        restart = input("You exploded do wish to play again?\n yes/no")
        restart = restart.lower()
    elif guess != mines:
         guess = input()
    else:
         guess = input(f"There are {mines} around {guess}")
    lineCounter=0
    
    while lineCounter <= int(y):
        print(BIGlist[x*lineCounter-1:x+(x*lineCounter)])
    if guess == "end" or restart == "no":
        break
"""
number of mines increase money after victory money can be used to buy items that increase amount of mines and size of click for more money item that clears 
bosses?!?!?



"""