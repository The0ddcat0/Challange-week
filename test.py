import random

def coordinates(a):
    if a.isdigit():
        return True
    else:
        print("Invalid input")

print("To end the game type: end")
guess = input("Choose the coordinates or flag: ")

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
