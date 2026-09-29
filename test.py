import random

def coordinates(a):
    a = a.split(":")
    if a.isdigit(a[0]) and a.isdigit(a[1]):
        return True
    else:
        print("Invalid coordinate")

print("To end the game type: end")
guess = input("Choose the coordinates or flag: x:y")

numbers = [1, 2, 3]

while True:
    if guess == "end" or restart == "no":
            break
        
    while guess == "flag":
         print("type guess to guess")
         if flag == "guess":
              break
         
         flag = input("Choose a flag cordinate: ")
         if flag in grid:
              grid[flag] = "F"
        

    if guess in mines:
        restart = input("You exploded do wish to play again?\n yes/no")
    elif guess != mines:
         guess = input()
    else:
         guess = input(f"There are {mines} around {guess}")
