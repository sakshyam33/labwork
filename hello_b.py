print(4*(6+5))
print(4*6+5)
print(4+6*5)
print((5>4) and (3==5))
print(not(5>4))
print((5>4) or (3==5))
print(not((5>4) or (3==5)))
print((True and True)and(True==False))
print((not True)or(not False))
import math
n=input("enter the number")
m=math.sqrt(n)
print("the squareroot is ",m)
print("the square is",math.pow(2,n))
result=3*1.5+4
print(type(result))
x=30
y=20
print((x),"+",(y),"=",(x+y))
import math
n = float(input("Enter the number: "))
m = math.sqrt(n)
print("The square root is", m)
print("2 raised to the power of", n, "is", math.pow(2, n))
a=["Red","Green","white","black","blue"]
print(a[0],a[-1])
x=4
y=3
z=(x+y)*(x+y)
print((x,'+',y,'^2'),"=",z)
name=input("enter your name")
print("GOOD MORNING \n","Mr",name)
r=int(input("enter the radius"))
import math
v=(4/3)* math.pi *(r**3)
print("the volume of the sphere is",v)
for i in range(12):
    if(i%2==0):
        print(i)
n=int(input("enter the number"))
m=int(input("enter the number"))
z=m+n
if(z>=15 and z<=20):
    print('20')
else:
        print("the sum is",z)
        a=123
b=12.3
c=1+2j
d="abc"
print(type(a))
print(type(b))
print(type(c))
print(type(d))
a=int(input("enter the number"))
b=int(input("enter the number"))
c=(a)/(b)
d=a//b
print(c)
print(d)
print("""twinkle twinkle little star,
            How i wonder what you are!
                Up above the world so high
                like a diamond in the sky
        twinkle twinkle little star,
            How i wonder what you are""")
# Example variables
var1 = "Hello"
var2 = 123
var3 = 45.67

# Check if var1 is a string
if isinstance(var1, str):
    print("var1 is a string")

# Check if var2 is an integer
if isinstance(var2, int):
    print("var2 is an integer")

# Check if var3 is a float
if isinstance(var3, float):
    print("var3 is a float")
var1 = [1, 2, 3]

var2 = (1, 2, 3)
var3 = {1, 2, 3}

# Check if var1 is a list
if isinstance(var1, list):
    print("var1 is a list")

# Check if var2 is a tuple
if isinstance(var2, tuple):
    print("var2 is a tuple")

# Check if var3 is a set
if isinstance(var3, set):
    print("var3 is a set")
no=input("enter thr no of roses")
no=int(no)
print("the number of roses are",no)
print(type(no))
n= int(input("Enter the number of strings to concatenate: "))
# Get the strings and concatenate them using join
strings = [input(f"Enter string {i+1}: ") for i in range(n)]
concatenated_string = ''.join(strings)
# Print the concatenated string
print("Concatenated String:", concatenated_string)"""
# Example variables
