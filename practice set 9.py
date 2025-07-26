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
'''
'''
i = 2
while i < 21:
    filename = "table_" + str(i) + ".txt"
    f = open(filename, "w")                

    for j in range(11):
        c = i * j
        print(str (c) +" ")                
        f.write(str(c)+" ")

    f.write("\nThis was the table for: " + str(i) + "\n")
    f.close()
    
    i = i + 1
'''
'''
str="i donkey my donkey sitting on a donkey"

f=open("myfile.txt","w")
f.write(str)
f.close()  

f=open("myfile.txt","w")
cy=str.replace("donkey","&&&&")
f.write(cy+" ")
f.close()
'''
l = ["gay", "pig", "dog", "cur"]
f = open("myfile.txt", "w")
f.write(str(l))
f.close()
new_list = []
for word in l:
    if word == "gay":
        new_list.append("&&&&")
    else:
        new_list.append(word)
f = open("myfile.txt", "a") 
f.write("\n" + str(new_list))
f.close()
