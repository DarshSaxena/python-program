'''
a=int(input("enter a number"))
b=int(input("enter a number"))
c=int(input("enter a number"))
d=int(input("enter a number"))

if (a>b and a>c and a>d):
    print(a)
    

elif (b>a and b>c and b>d):
    print(b)


elif (c>a and c>b and c>d):
    print(c)
    
elif (d>b and d>c and d>a):
    print(d) 
    
else:
    print("all r same")    
'''
'''
sub1=int(input("enter marks in hindi : "))   
sub2=int(input("enter marks in history: "))
sub3=int(input("enter marks in maths :")) 
avg= ((sub1+sub2+sub3)/3)
print(avg)
if(sub1>=33 and sub2>=33 and sub3>=33 and avg>=40):
    print("YOU HAVE PASSED THE EXAM BY ")
  
else:
    print("YOU FAILED ANY WAY")
'''
'''
f1="Make a lot of money"
f2="buy now"
f3="Subscribe this"
f4="click this"
a=input("enter the message you recived :")

if(f1 in a or f2 in a or f3 in a or f4 in a):
    print("you spammer")
else:
    print("hello baby")
 '''
'''
a=(input("enter the username in numerics"))        
if(len(a)>=10):
    print("please stick to the number said")
else:
    print("good")
'''
''' 
a=["darsh","aman","shreyash","vaishnavi","devansh","taraksh"]
b=input("enter the name u want to check")
if(b in a):
    print("yes")
else:
    print("no")   
'''
'''
hindi=int(input("enter marks in hindi :"))
english=int(input("enter marks in english :"))
percent=(hindi+english)/2 
print(percent)

if(100>percent>90):
    print("excellent")
    
elif(90>percent>80):
    print("A+") 
    
elif(80>percent>70):
    print("B")
elif(70>percent>60):
    print("c")
elif(60>percent>50):
    print("D")
else:
    print("F")
'''
a=input("enter the post")

if("darsh" in a.lower()):
    print("yess")
else:
    print("noo")
  