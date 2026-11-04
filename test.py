import random
wife = 0
pregnant = 0
pregoLength = {}
pedegry={}
babyPrices=20000
def gettingYourWifePregnant():
    
    if wife > 0 and pregnant != wife :
        i=0
        while i <= wife - pregnant:
            if random.randint(1,5)==1:
                pregnant+=1
                pregnant[pregnant]=1

def givingbirth():
    if 9 in pregoLength.values:
        gender=random.randint(1,11)
        if gender<5:
            gender="male"
        elif gender<10:
            gender="female"
        else:
            gender = "intersex"
        name =input(f"name your {gender} child")
        pedegry[name]=0

def timePassesEverSlowly():
    for i in pregoLength:
        pregoLength[i]+=1
    for i in pedegry:
        pedegry[i]+=1
        if pedegry[i].values()%12==0:
            print (f"your child {pedegry[i].keys()}turned {pedegry[i].keys()/12} years old today but you missed their birthday because you were sweeping mines.good job, keep going")
def mortis():
    global deathCounter,cashDollerMoney,pedegry
    if deathCounter<=0:
        print ("you died l bozo")
    if len(pedegry)>0:
        i=0
        oldestChild=0
        oldestChildAge=0
        while len (pedegry)-1>=i:
            if list(pedegry.values())[i]>oldestChildAge:
                oldestChild=list(pedegry.keys())[i]
                oldestChildAge=list(pedegry.values())[i]
        print (f"you are now {oldestChild} you are {oldestChildAge/12}and have all your organs and inhearited {cashDollerMoney} sl$")

def sellingTheKidsForGamblingDebts():
    global pedegry, cashDollerMoney
    if len(pedegry)>0:
        sellingTheKids=input("do you wanna sell any kids Y/N")
        if sellingTheKids=="Y":
            for i in pedegry.keys():
                ForGamblingDebts=input(f"do you want to sell {i} Y/N")
                if ForGamblingDebts=="":
                    pedegry.pop(i)
                    cashDollerMoney+=babyPrices
            