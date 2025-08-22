#  Write a Python program to create a calculator using functions.

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def multi(a,b):
    return a*b

def divi(a,b):
    return a/b

print("Calculator")
num1=float(input("Enter first num::"))
num2=float(input("Enter second num::"))

print("chosse operator:: + - * /")
op=input("chosse operator::")

if op=='+':
    print("Result",add(num1,num2))
elif op=='-':
    print("Result",sub(num1,num2))
elif op=='*':
    print("Result",multi(num1,num2))

elif op=='/':
    if num2==0:
           print("Cannot divide by zero!")
    else:
        print("Result:", divi(num1, num2))
else:
    print("Invalid operator")