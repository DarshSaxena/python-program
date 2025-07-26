'''
str="yes yes papa"
f=open("poem.txt","w")
f.write(str)
f.close()
f=open("poem.txt")
data=f.read()
if("papa" in data):
    print("true")
else:
    print("nhi hai")
print(data)
f.close()
'''
import random
def game():
    data=random.choice((1,2,3,4,5,6,7,8,9))
    print(data)
    a=int(input("enter any integer"))
    hiscore=0
    if(a>=data):
        hiscore=a
    else:
        hiscore=data
    print(hiscore)
    f=open("myfile.txt","w")
    f.write(str(hiscore))
    f.close()
game()