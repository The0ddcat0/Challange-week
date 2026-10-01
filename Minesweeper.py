import random

def shop():
    global cashDollerMoney
    done = "n"
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
    print(f" you have {cashDollerMoney} silly linguini dollars")
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
    while done == "N" or done == "n":
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
            cashDollerMoney = cashDollerMoney - 100
            mineNmr = mineNmr + 1
            amountOfBombsPurchased = amountOfBombsPurchased + 1
        done = input("are you done shoping: Y or N")

def coordinates(a):
    if a.isdigit():
        return True
    else:
        print("Invalid input")
        return False
        
amountOfBombsPurchased = 0
items = []
allItems = ["a","b","c","d"]
itemPrice = [1,2,3,4]
mineNmr = 3
cashDollerMoney =0 
bigCLICKS = 1
bigClickSize = 2
restart = ""
guess = ""
organs= ["a pint of blood","a pint of blood","a pint of blood","a pint of blood","a pint of blood","a pint of blood","a pint of blood","a pint of blood","a pint of blood","a pint of blood","ligaments","bones","64,516 dm of skin","64,516 dm of skin","64,516 dm of skin","cornea","cornea","liver","kidney","kidney","lung","lung","heart"]
organPrice=[297.46,297.46,297.46,297.46,297.46,297.46,297.46,297.46,297.46,297.46,4758,62,6611.25,7932.33,7932.33,7932.33,19830.83,19830.83,56195.62,138815.77,138815.77,272343.33,272343.33,562340.87]

while True:
    BIGlist = []
    mines = []
    carCounter = 1
    lineCounter = 1


    x = input("Width: ")
    y = input("Height: ")
    
    i = 1


    if coordinates(x) and coordinates(y):
        x = int(x)
        y = int(y)
        totalSize = x**y
        print("To end the game type: end")
        while i <= int(mineNmr):
             randMine = (random.randint(1,y)-1)**x+random.randint(1,x)
             mines.insert(0,randMine)
             i += 1
             print(mines)
             print (i)        
       
        while lineCounter <= y:
            if carCounter >= x:
                carCounter = 0
                lineCounter = lineCounter + 1
            BIGlist.append("0")
            carCounter = carCounter + 1
            #print(carCounter)
    while "0" in BIGlist:
        lineCounter = 0
        while lineCounter <= int(y):
            print(BIGlist[x*lineCounter:x+(x*lineCounter)])
            lineCounter += 1  
        #print(BIGlist)
        guess = input("Guess a coordinate x y: ")    
        while guess == "flag":
            lineCounter = 0
            while lineCounter <= int(y):    
                print(BIGlist[x*lineCounter:x+(x*lineCounter)])
                lineCounter += 1              
            flag = input("Choose a flag cordinate x y: ")
            if flag == "guess":
                guess = input("Guess a coordinate x y: ")   
            else:
                flagX,flagY = flag.split(" ")       
                trueFlag = int(flagX) + (int(flagY)-1) ** x
                flag = int(flagX) -1+ (int(flagY)-1)  ** x
                BIGlist[flag] = "F"
             
        guessX,guessY = guess.split(" ")
        trueGuess = int(guessX) + (int(guessY)-1) ** x
        if trueGuess in mines:
            restart = input("You exploded do wish to play again?\n yes/no")

        else:
            print("you live")
            BIGlist[trueGuess] = "~"

        if guess == "end" or restart == "no":
            break
    if "0" not in BIGlist:
       # cashDollerMoney = cashDollerMoney +((mineNmr**5)//(x**y))
        mineNmr += 1
        shop()
        while cashDollerMoney <0:
            print("uh oh you defaulted")
            i=0
            count=0
            if cashDollerMoney+organPrice[i] >= 0:
                print (f"the loan shark took your {organs[i]} for {organPrice[i]}")
                cashDollerMoney=cashDollerMoney+organPrice[i]
                organs[i]="hole"
                organPrice[i]=0
            if i > len(organs) and cashDollerMoney<0:
                if organPrice[count]>0:
                    print (f"the loan shark took your {organs[count]} for {organPrice[count]}")
                    cashDollerMoney=cashDollerMoney+organPrice[count]
                    organs[count]="hole"
                    organPrice[count]=0
            
            i=i+1