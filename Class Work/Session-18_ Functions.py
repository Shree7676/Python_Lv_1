"""
Chirag, Yugank, and Chris decide to create a python program together.
But they are not able to understand how they are going to divide the whole program among them.
Also, they are confused with the combination process of the program as well.
We can divide a big program into smaller parts known as functions.
To explain the same thing to three students, write a python program and create different functions
to add, subtract, and multiply two numbers.
# Creating different functions for addition subtraction and multiplication
"""
# function to add two numbers

def add(x,y):
    sum = x + y
    return sum

# function for subtraction

def subtract(x,y):
    diff = x - y
    return diff

# function to multiply two numbers

def multiply(x,y):
    product = x * y
    return product

# Main Program

first = int(input("Enter first number:"))
second = int(input("Enter second number:"))

print("Addition :" , add(first,second))
print("Subtraction :" , subtract(first,second))
print("Multiplication :" , multiply(first , second))

"""
Sahil is wondering whether we can use the same concept of functions in creating simple and 
compound interest calculators. He is trying to create it but is unable to return the answers from the functions. 
Help him in doing the same.
"""
# Calculating simple and compound interest using functions

# Function to calculate simple interest

def simpleInterest(p,r,t):
    si = p * r/100 * t
    return si

# Function to calculate compound interest

def compoundInterest(p,r,t):
    ci = p*(1+r/100)**t - p
    return ci

# Main Program

# Taking necessary inputs

p = int(input("Enter principal amount :"))
r = int(input("Enter rate of interest :"))
t = int(input("Enter time duration in yrs :"))

simple_interest = simpleInterest(p,r,t)
compound_interest = compoundInterest(p,r,t)

print("Simple interest return :" ,simple_interest)
print("Compound interest return :" ,compound_interest)


"""
Nidhi is writing a long program. She needs a function that can check whether a given number 
is a perfect square or not. To help Nidhi, write a program in python and create a function 
that checks whether the given number is a perfect square or not.
"""# Program to check whether the given number is a perfect square or not

def isPerfectSquare(num):
    root = num ** 0.5
    intRoot = int(root)

    if root == intRoot :
        return True

    return False

# Main Program

number = int(input("Enter the number :"))

if isPerfectSquare(number):
    print("The given number is perfect square")

else :
    print("The given number is not a perfect square")

