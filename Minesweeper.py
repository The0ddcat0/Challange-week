import random

def coordinates(a):
    if a.isdigit():
        return True
    else:
        print("Invalid input")
mineNmr = 3
cashDollerMoney=0
bigCLICKS=1
bigClickSize=2

while True:
    BIGlist = []
    mines = []
    carCounter = 0
    lineCounter = 0


    x = input("Width: ")
    y = input("Height: ")
    
    i = 0

    while i >= int(mineNmr):
         randMine = f"{random.randint(0,x)}{random.randint()}"
         mines.append(randMine)
         
    if coordinates(x) and coordinates(y):
        x = int(x)
        y = int(y)
        totalSize=x**y
        print("To end the game type: end")
        
        while carCounter**lineCounter <= totalSize:
            if carCounter>=x:
                carCounter=0
                lineCounter= lineCounter+1
            BIGlist.append("0 ")
            carCounter = carCounter+1
        guess = input("guess a coordinate: ")
        numbers = [1, 2, 3]

   
    while guess == "flag":
        print("type guess to guess")

        flag = input("Choose a flag cordinate: ")
        if flag in BIGlist:
              BIGlist[flag] = "F"
        elif flag == "guess":
            break
        

    if guess in mines:
        restart = input("You exploded do wish to play again?\n yes/no")
    elif guess != mines:
         guess = input()
    else:
         guess = input(f"There are {mines} around {guess}")
    lineCounter = 0
    while lineCounter <= int(y):
        print(BIGlist[x*lineCounter-1:x+(x*lineCounter)])
    if guess == "end" or restart == "no":
            break
    if 0 not in BIGlist:
         money = money +((mineNmr**5)//(x**y))