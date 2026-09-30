import random

def coordinates(a):
    if a.isdigit():
        return True
    else:
        print("Invalid input")
        return False

def guess_flag(a):
    a = a.split(" ")    
    if a.isdigit(a[0]) and a.isdigit(a[1]):
        return True
    else:
        print("big balls by ac/dc")
        return False

        

mineNmr = 3
cashDollerMoney =0 
bigCLICKS = 1
bigClickSize = 2
restart = None
guess = None

while True:
    BIGlist = []
    mines = []
    carCounter = 1
    lineCounter = 1


    x = input("Width: ")
    y = input("Height: ")
    
    i = 0

<<<<<<< HEAD
=======
    while i >= int(mineNmr):
         randMine = f"{random.randint(0,x)} {random.randint(0,y)}"
         mines.append(randMine)
>>>>>>> 6567ea1fb0069c3aade4a3548d4ac27498b5d17c

         
    if coordinates(x) and coordinates(y):
        x = int(x)
        y = int(y)
        totalSize=x**y
        print("To end the game type: end")
       
       
        while lineCounter <=y:
            if carCounter >= x:
                carCounter = 0
                lineCounter = lineCounter + 1
            BIGlist.append("0 ")
            carCounter = carCounter + 1
            #print(carCounter)
        guess = input("guess a coordinate: ")
        guess = input("Guess a coordinate: x y")
    #print(BIGlist)
    #print(mines)
   

    while guess == "flag":
        print("type guess to guess")
        print("Type guess to guess")

        flag = input("Choose a flag cordinate: ")
        if flag in BIGlist:
              BIGlist[flag] = "F"
        elif flag == "guess":
            break
        
    while i >= int(mineNmr):
         randMine = f"{random.randint(0,x)} {random.randint(0,y)}"
         mines.append(randMine) 
    print(mines)
    if guess in mines:
        restart = input("You exploded do wish to play again?\n yes/no")
    elif guess != mines:
    elif guess not in mines:
         guess = input()
    else:
         guess = input(f"There are {mines} around {guess}")


    lineCounter = 0
    while lineCounter <= int(y):
        print(BIGlist[x*lineCounter:x+(x*lineCounter)])
        lineCounter += 1
    if guess == "end" or restart == "no":
            break
        break
    if 0 not in BIGlist:
         cashDollerMoney = cashDollerMoney +((mineNmr**5)//(x**y))
         mineNmr += 1