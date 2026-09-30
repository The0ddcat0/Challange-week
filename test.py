import random
mineNmr = 3
cashDollerMoney =0 
bigCLICKS = 1
bigClickSize = 2
restart = None
guess = None


items=[]
allItems=[1,1,1,1]
itemPrice=[1,1,1,1]
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
    shop1=random.randint(0,len(allItems)-1)
    shop2=random.randint(0,len(allItems)-1)
    shop3=random.randint(0,len(allItems)-1)
    print ('to purchase type the number infront of the item')
    print (f"1  {allItems[shop1]}  sl$ {itemPrice[shop1]}")
    print (f"2  {allItems[shop2]}  sl$ {itemPrice[shop2]}")
    print (f"3  {allItems[shop3]}  sl$ {itemPrice[shop3]}")
    print ("4  buy more mines 50$")
    purchase= input()
    if purchase==1
shop()




"""
number of mines increase money after victory money can be used to buy items that increase amount of mines and size of click for more money item that clears 
bosses?!?!?



"""