import random

def coordinates(a):
    if a.isdigit():
        return True
    else:
        print("Invalid input")

print("To end the game type: end")
user = input("Choose the coordinates: ")

numbers = [1, 2, 3]

while True:
    if user == "end":
        break
