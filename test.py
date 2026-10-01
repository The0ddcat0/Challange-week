import random

mineNmr = 3
cashDollerMoney =0 
bigCLICKS = 1
bigClickSize = 2
restart = None
guess = None


oos1= True
oos2= True
oos3= True


amountOfBombsPurchased=0
items=[]
allItems=["a","b","c","d"]
itemPrice=[1,2,3,4]
def shop():
    done="N"
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
    shop1=random.randint(0,len(allItems)-1)
    shop2=random.randint(0,len(allItems)-1)
    shop3=random.randint(0,len(allItems)-1)
    print ('to purchase type the number infront of the item')
    print (f"1  {allItems[shop1]}  sl$ {itemPrice[shop1]}")
    print (f"2  {allItems[shop2]}  sl$ {itemPrice[shop2]}")
    print (f"3  {allItems[shop3]}  sl$ {itemPrice[shop3]}")
    print ("4  buy more mines 50$")
    oos1=True
    oos2=True
    oos3=True
    while done!="Y "or done!="y":
        purchase= input()
        if purchase==1 and oos1:
            cashDollerMoney=cashDollerMoney-itemPrice[shop1]
            items=items+allItems[shop1]
            oos1
        if purchase==2 and oos2:
            cashDollerMoney=cashDollerMoney-itemPrice[shop2]
            items=items+allItems[shop2]
        if purchase==3and oos3:
            cashDollerMoney=cashDollerMoney-itemPrice[shop3]
            items=items+allItems[shop3]
        if purchase==4:
            mineNmr=mineNmr+1
            amountOfBombsPurchased=amountOfBombsPurchased+1
        done = input("are you done shoping: Y or N")
shop()
        


