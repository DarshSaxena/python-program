'''
def factorial(n):
    if(n==0):
        return 1
    return n*factorial(n-1)

n=int(input("enter any number: "))
a= factorial(n)
print(a)
'''
'''
def greatest():
    a=int(input("enter any number: "))
    b=int(input("enter any number: "))
    c=int(input("enter any number: "))
    if(a>b and b>c and a>c):
      return a
    if(b>a and a>c and b>c):
        return b
    if(c>a and c>b):
        return c
    
a=greatest()
print(a)
'''
'''
def temp():
    a=float(input("enter temp in clecuis"))
    b=(a*1.8)+32
    return b
c=temp()
print(c)
 '''
''' 
def recurse(n):
    if(n==0):
        return 0
    return n+recurse(n-1)

n=int(input("enter any number"))
b=recurse(n)
print(b)
'''
'''
def conversion():
    a=float(input("enter length in cm: "))
    b=a/2.54
    return b
c=conversion()
print(c)
'''
def multiply(n):                            
    for i in range(1, 11):               
        print(f"{n} x {i} = {n*i}")      

multiply(5)                                                                                                                                         
   
    
