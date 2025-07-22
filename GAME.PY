import random

a=random.choice(("snake","water","gun"))
b=input("enter your choice :")
print("you choose:"+b)
print("the computer choose:"+a)
if(b==a):
    print("its a tie")
else:
    if(b=="snake" and a=="water"):
        print("you won")
    elif(b=="snake" and a=="gun"):
        print("you lose")
    elif(b=="water" and a=="gun"):
        print("you won")
    elif(b=="water" and a=="snake"):
        print("you lose")
    elif(b=="gun" and a=="water"):
        print("you lose")
    elif(b=="gun" and a=="snake"):
        print("you won")
    else:
        print("game over")
