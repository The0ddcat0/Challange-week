def guess_flag(a):
    a = a.split(" ")    
    if "0" <= a[0] <= "9" and "0" <= a[1] <= "9":
        return True
    else:
        print("big balls by ac/dc")

"""
    if guess in mines:
        restart = input("You exploded do wish to play again?\n yes/no")
    elif guess not in mines:
         guess = input()
    else:
         guess = input(f"There are {mines} around {guess}")
"""
guess = input("Guess a coordinate: ")
minestest = "2 3"

if guess_flag(guess):
    guess = guess.split(" ")
guess_x = guess[0]
guess_y = guess[1]

minestest = minestest.split(" ")

if guess_x in minestest[0] and guess_y in minestest[1]:
    restart = input("You exploded do wish to play again?\n yes/no")
elif guess_x in minestest[0]:
    print("bom nearby the y")
elif guess_y in minestest[1]:
    print("bom nearby the x")
else:
    print("theres no bomb")    

#print(minestest)
#print(f"{guess_x} {guess_y}")