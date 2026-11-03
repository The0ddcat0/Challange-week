import random
def shop():
    global cashDollerMoney, mineNmr, amountOfBombsPurchased, items, shopSize
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
    amountUniqueItems = random.randint(0,shopSize)
    shopStock = {}
    i=0

    while i<amountUniqueItems:
        tempRandom = random.randint(0,len(items["unicum"]))
        shopStock[i] = items["unicum"](list(items["unicum"])[tempRandom])
        items["unicum"].pop(list [items["unicum"]] [tempRandom])
        i+=1
    while i + amountUniqueItems<=shopSize:
        tempRandom = random.randint(0,len(items["nonunicum"]))
        shopStock[i] = items["nonunicum"][(list(items["nonunicum"].keys()))][tempRandom]
        i += 1
    print (shopStock)






    """print ('to purchase type the number infront of the item')
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
            oos1=False
        if purchase == "2" and oos2:
            cashDollerMoney = cashDollerMoney - itemPrice[shop2]
            items=items+allItems[shop2]
        if purchase == "3" and oos3:
            cashDollerMoney = cashDollerMoney - itemPrice[shop3]
            items = items + allItems[shop3]
        if purchase == "4":
            cashDollerMoney = cashDollerMoney - 50
            mineNmr = mineNmr + 1
            amountOfBombsPurchased = amountOfBombsPurchased + 1
        done = input("are you done shoping: Y or N")"""
mineNmr=3
amountOfBombsPurchased=0
items={"unicum":{"a":1,"b":2},"nonunicum":{"Na":1,"Nb":2}}
while True:
    cashDollerMoney=input()
    cashDollerMoney=int(cashDollerMoney)
    shopSize=input( )
    shopSize=int(shopSize)-1
    shop()