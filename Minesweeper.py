import random
def coordinates(a):
    if a.isdigit():
        return True
    else:
        print("Invalid input")
carCounter=0
lineCounter=0
BIGlist=[]
mines=[]
while True:
    x= input("width: ")
    y=input("height: ")
    
    if coordinates(x) and coordinates(y):

        totalSize=int(x)**int(y)
        print("To end the game type: end")
        x=int(x)
        while carCounter**lineCounter <= totalSize:
            if carCounter>=x:
                carCounter=0
                lineCounter= lineCounter+1
            BIGlist.append("0 ")
            carCounter= carCounter+1
        guess = input("guess a coordinate: ")
        numbers = [1, 2, 3]

   
    while guess == "flag":
         print("type guess to guess")
         if flag == "guess":
              break
         
         flag = input("Choose a flag cordinate: ")
         if flag in BIGlist:
              BIGlist[flag] = "F"
        

    if guess in mines:
        restart = input("You exploded do wish to play again?\n yes/no")
    elif guess != mines:
         guess = input()
    else:
         guess = input(f"There are {mines} around {guess}")
    lineCounter=0
    while lineCounter<=int(y):
        print(BIGlist[x*lineCounter-1:x+(x*lineCounter)])
    if guess == "end" or restart == "no":
            break