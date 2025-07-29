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