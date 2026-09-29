import random
def coordinates(a):
    if a.isdigit():
        return True
    else:
        print("Invalid input")
carCounter=0
lineCounter=0
BIGlist=[]
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
        user = input("guess a coordinate: ")
        numbers = [1, 2, 3]
        print(BIGlist[x*lineCounter-1:x+(x*lineCounter)])
        break