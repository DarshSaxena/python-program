'''
class programmer:
    salary=12345454
    age=45
    dept="socs"
def getinfo(self):
    print("salary="+str(self.salary),"age="+str(self.age),"department="+str(self.dept))
darsh=programmer()
darsh.name="DARSH"
print(darsh.name)
getinfo(darsh)
'''
'''
import math

choice=input("enter your choice c for square,cc for cube and ccc for square root:")
print(choice)
class calculator:
    def square(self,a):
     return a*a
     
    def cube(self,a):
     return a*a*a
    def squareroot(self,a):
     return math.sqrt(a)
darsh=calculator()
a=float(input("enter the number"))
if(choice=="c"):
    print(darsh.square(a))
elif(choice=="cc"):
    print(darsh.cube(a))
elif(choice=="ccc"):
    print(darsh.squareroot(a))
else:
    print("invalid choice")
'''
'''
import math

print("please enter your choice")
choice=input("enter your choice c for square,cc for cube and ccc for square root:")
print(choice)
class calculator:
    def square(self,a):
     return a*a

    def cube(self,a):
     return a*a*a
    @staticmethod 
    def squareroot(a):
     return math.sqrt(a)
darsh=calculator()
a=float(input("enter the number"))
if(choice=="c"):
    print(darsh.square(a))
elif(choice=="cc"):
    print(darsh.cube(a))
elif(choice=="ccc"):
    print(calculator.squareroot(a))c
else:
    print("invalid choice")
'''
'''
wish=input("if you want to book ticket press 1"+" "+"if you want any info press 2 :")
class train:
    print("welcome to Darsh Railways")
    def bookticket(self):
        print("hi welcome to ticket booking:")
        a=input("enter you boarding station:")
        b=input("enter you destination station:")
        c=input("please enter the tier you want to travel:")
        if(c=="sleeper"):
            print("your fare is"+str("500"))
        elif(c=="3ac"):
            print("your fare is"+str("1000"))
        elif(c=="2ac"):
            print("your fare is"+"1500")
        elif(c=="1ac"):
            print("your fare is "+"2500")
        else:
            print("hut gareeb")
        return "thank you"
    def getinfo(self):
        d=int(input("enter your train number:"))
        if(len(str(d))):
            print("your train is delayed by 5hrs")
        else:
            print("please enter a valid train number")
        name=input("enter your name:")
        age=input("enter your age:")
        gender=input("enter your gender:")
        choice=input("please tell what you want to know:")
        if(choice=="name"):
         print(name)
        elif(choice=="age"):
            print(age)
        elif(choice=="gender"):
            print(gender)
        elif(choice=="all"):
            print(str(name)+str("")+str(gender)+str("")+str(age))
        else:
            print("gian ho aap")
        return "Happy Journey"
darsh=train()
if(wish=="1"):
    print(darsh.bookticket())
else:
 print(darsh.getinfo())
'''
class something:
    print("kuch nhi yaar chal rha h")
    def someone(seloffeb):
        print("no one")
        return "ooi maa"
obj=something()
obj.someone()
               
        