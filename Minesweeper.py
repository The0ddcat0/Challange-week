import random

def shop():
    print("""
    (`-').-> (`-').->            _  (`-') 
    ( OO)_   (OO )__      .->    \-.(OO ) 
    (_)--\_) ,--. ,'-'(`-')----.  _.'    \ 
    /    _ / |  | |  |( OO).-.  '(_...--'' 
    \_..`--. |  `-'  |( _) | |  ||  |_.' | 
    .-._)   \|  .-.  | \|  |)|  ||  .___.' 
    \       /|  | |  |  '  '-'  '|  |      
    `-----' `--' `--'   `-----' `--'      
        """)
    shop1 = random.randint(0,len(allItems)-1)
    shop2 = random.randint(0,len(allItems)-1)
    shop3 = random.randint(0,len(allItems)-1)
    print ('to purchase type the number infront of the item')
    print (f"1  {allItems[shop1]}  sl$ {itemPrice[shop1]}")
    print (f"2  {allItems[shop2]}  sl$ {itemPrice[shop2]}")
    print (f"3  {allItems[shop3]}  sl$ {itemPrice[shop3]}")
    print ("4  buy more mines 50$")
    oos1 = True
    oos2 = True
    oos3 = True
    while done!="Y "or done!="y":
        purchase= input()
        if purchase == 1 and oos1:
            cashDollerMoney = cashDollerMoney - itemPrice[shop1]
            items = items + allItems[shop1]
            oos1
        if purchase == 2 and oos2:
            cashDollerMoney = cashDollerMoney - itemPrice[shop2]
            items=items+allItems[shop2]
        if purchase == 3and oos3:
            cashDollerMoney = cashDollerMoney - itemPrice[shop3]
            items = items + allItems[shop3]
        if purchase == 4:
            mineNmr = mineNmr + 1
            amountOfBombsPurchased = amountOfBombsPurchased + 1
        done = input("are you done shoping: Y or N")

def coordinates(a):
    if a.isdigit():
        return True
    else:
        print("Invalid input")
        return False
    
def guess_flag(a):
    a = a.split(" ")    
    if "0" <= a[0] <= "9" and "0" <= a[1] <= "9":
        return True
    else:
        print("big balls by ac/dc")
        return False

        
amountOfBombsPurchased=0
items = []
allItems = ["a","b","c","d"]
itemPrice = [1,2,3,4]
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

    while i >= int(mineNmr):
         randMine = f"{random.randint(0,x)} {random.randint(0,y)}"
         mines.append(randMine)

         
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
        guess = input("Guess a coordinate x y: ")
    #print(BIGlist)
    #print(mines)
   

    while guess == "flag":
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

#dis mijn guess bs dus als het niet werkt stuur msg    
    if guess_flag(guess):
        guess = guess.split(" ")

    guess_x = guess[0]
    guess_y = guess[1]
    mines = mines.split(" ")

    if guess_x in mines[0] and guess_y in mines[1]:
        restart = input("You exploded do wish to play again?\n yes/no")
    elif guess_x in mines[0]:
        print("bom on the y-axis")
    elif guess_y in mines[1]:
        print("bom on the x-axis")
    else:
        print("theres no bomb")  

#    if guess in mines:
#        restart = input("You exploded do wish to play again?\n yes/no")
#    elif guess not in mines:
#         guess = input()
#    else:
#         guess = input(f"There are {mines} around {guess}")

    lineCounter = 0
    while lineCounter <= int(y):
        print(BIGlist[x*lineCounter:x+(x*lineCounter)])
        lineCounter += 1
    if guess == "end" or restart == "no":
        break
    if 0 not in BIGlist:
         cashDollerMoney = cashDollerMoney +((mineNmr**5)//(x**y))
         mineNmr += 1
         shop()