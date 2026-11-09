import random

def shop():
    global cashDollerMoney
    global mineNmr
    global amountOfBombsPurchased
    global allItems,itemPrice
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
    shop1 = random.randint(0, len(allItems) - 1)
    shop2 = random.randint(0, len(allItems) - 1)
    shop3 = random.randint(0, len(allItems) - 1)
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
        if purchase == "1" and oos1:
            cashDollerMoney = cashDollerMoney - itemPrice[shop1]
            items = items + allItems[shop1]
            oos1
        if purchase == "2" and oos2:
            cashDollerMoney = cashDollerMoney - itemPrice[shop2]
            items=items+allItems[shop2]
        if purchase == "3" and oos3:
            cashDollerMoney = cashDollerMoney - itemPrice[shop3]
            items = items + allItems[shop3]
        if purchase == "4":
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

def organtrade():
    global cashDollerMoney,organs
    if cashDollerMoney<0:
        print("uh oh you defaulted")    
    i=0
    while i < len(organs) and cashDollerMoney<0:
        if cashDollerMoney + list(organs.values())[i] >= 0:
            print(f"the loanshark took {list(organs.keys())[i]}")
            organs.pop(list(organs.keys())[i])
            cashDollerMoney = cashDollerMoney + list(organs.values())[i]
        i+=1

def mortis():
    global deathCounter,cashDollerMoney,pedegry
    if deathCounter <= 0:
        print("you died l bozo")
    if len(pedegry) > 0:
        i = 0
        oldestChild = 0
        oldestChildAge = 0
        while len(pedegry) - 1 >= i:
            if list(pedegry.values())[i] > oldestChildAge:
                oldestChild = list(pedegry.keys())[i]
                oldestChildAge = list(pedegry.values())[i]
        print (f"you are now {oldestChild} you are {oldestChildAge/12} and have all your organs and inhearited {cashDollerMoney} sl$")

def timePassesEverSlowly():
    global pregoLength,pedegry
    for i in pregoLength:
        pregoLength[i] += 1
    for i in pedegry:
        pedegry[i] += 1
        if pedegry[i].values() % 12 == 0:
            print (f"your child {pedegry[i].keys()} turned {pedegry[i].keys()/12} years old today but you missed their birthday because you were sweeping mines.good job, keep going")

def givingbirth():
    global pregoLenght,pedegry
    if 9 in pregoLength.values:
        gender=random.randint(1,11)
        if gender < 5:
            gender = "male"
        elif gender < 10:
            gender = "female"
        else:
            gender = "intersex"
        name = input(f"name your {gender} child")
        pedegry[name] = 0

def gettingYourWifePregnant():
    global wife,pregnant
    if wife > 0 and pregnant != wife :
        i=0
        while i <= wife - pregnant:
            if random.randint(1,5) == 1:
                pregnant += 1
                pregnant[pregnant] = 1

def sellingTheKidsForGamblingDebts():
    global pedegry, cashDollerMoney
    if len(pedegry) > 0:
        sellingTheKids=input("do you wanna sell any kids Y/N")
        if sellingTheKids == "Y":
            for i in pedegry.keys():
                ForGamblingDebts=input(f"do you want to sell {i} Y/N")
                if ForGamblingDebts == "":
                    pedegry.pop(i)
                    cashDollerMoney += babyPrices

def make_mines(mineNmr, x, y):
    mines = []
    i = 0

    while i <= int(mineNmr):
        randMine = (random.randint(1, y) - 1) * x + random.randint(1, x)
        mines.insert(0, randMine)
        i += 1    
    return mines

def guess_validation(a):
    if a == "flag" or a == "end":
        return True
    b = a.split(" ")
    if len(b) == 2:
        if b[0].isdigit() and b[1].isdigit():
            return True
    print("Invalid input")
    return False


babyPrices=20000
amountOfBombsPurchased = 0
items = []
allItems = ["a","b","c","d"]
itemPrice = [1,2,3,4]
mineNmr = 3
cashDollerMoney = 0 
bigCLICKS = 1
bigClickSize = 2

organs = {"a pint of blood":297.46,"a second pint of blood":297.46,"a third pint of blood":297.46,"a forth pint of blood":297.46,"a fifth pint of blood":297.46,"a sixth pint of blood":297.46,"a seventh pint of blood":297.46,"a eighth pint of blood":297.46,"a nineth pint of blood":297.46," your last pint of blood":297.46," your ligaments":4758.62,"your bones":4758.62,"64,516 dm of your skin":7932.33,"most of your skin":7932.33,"the last of your skin":7932.33,"your left cornea":19830.83,"your right cornea":19830.83,"your liver":56195.62,"left kidney":138815.77,"your right kidney":138815.77,"your left lung":272343.33,"your right lung":272343.33,"your heart":562340.87}

def main():
    playing=True
    while playing:
        BIGlist = []
        mines = []
        carCounter = 1
        lineCounter = 1
        mineNmr = 3

        i = 1

#amound of mines
        if True:
            x = input("Width: ")
            y = input("Height: ")
            x = int(x)
            y = int(y)
#           totalSize = x * y
            mines = make_mines(mineNmr, x, y)
            print("To end game type: end")
        
#creates field        
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
                print(BIGlist[x * lineCounter: x + (x * lineCounter)])
                lineCounter += 1  
            #print(BIGlist)
            while True:
                guess = input("Guess a coordinate x y: ")
                if guess_validation(guess):
                    break

#guessing and stuff
            while guess == "flag":
                lineCounter = 0
                while lineCounter <= int(y):    
                    print(BIGlist[x * lineCounter: x + (x * lineCounter)])
                    lineCounter += 1
                while True:
                    flag = input("Choose a flag cordinate x y: ")
                    if guess_validation(flag):
                        break


                if flag == "guess":
                    while True:
                        guess = input("Guess a coordinate x y: ")
                        if guess_validation(guess):
                            break

                if guess_validation(flag):
                    flagX, flagY = flag.split(" ")
                    trueFlag = (int(flagX) - 1) + (int(flagY) - 1) * x
                    if 0 <= trueFlag < len(BIGlist):
                        BIGlist[trueFlag] = "F"
            
            if guess == "end":
                playing = False
                break

            guessX, guessY = guess.split(" ")
            trueGuess = (int(guessX) - 1) + (int(guessY) - 1) * x

            if trueGuess < 0 or trueGuess >= len(BIGlist):
                print("this isnt in the frame")
            else:
                if trueGuess in mines:
                    restart = input("You exploded do wish to play again?\n yes/no \n")
                    if restart == "no":
                        playing = False
                        break

                else:
                    print("you live")
                    BIGlist[trueGuess] = "~"

            if guess == "end":
                playing = False
                break

    if "0" not in BIGlist:
       # cashDollerMoney = cashDollerMoney +((mineNmr**5)//(x**y))
        mineNmr += 1
        shop()
        organtrade()

if __name__ == "__main__":
    main()