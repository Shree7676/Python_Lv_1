"""
Sahil got to know about modules in python. He wants to use the random module to make virtual dice in python.
Write a program to help Sahil with the same.
"""
# Creating a virtual dice

import random
dice = 1,2,3,4,5,6
roll = random.choice(dice)
print("Roll :" , roll)

"""
Arvind is working on a project where he needs a module to find the area of different shapes for him. 
To help Arvind in his project, create a module getArea() that can 
find the area of different shapes like square, rectangle, circle, and triangle. 
Using the above module create a separate py file to calculate the area of a football field of length 105m and width 65m
"""
# Module to get the area of different shapes
# getArea.py

# function to find the area of square

def square(side):
    area = side**2
    return area

# function to find the area of a rectangle

def rectangle(length , breath):
    area = length*breath
    return area

# function to find the area of a circle

def circle(radius):
    pi = 3.14
    area = pi*radius**2
    return area

# function to find the area of a triangle

def triangle(height , base):
    area = height * base * 0.5
    return area



"""
Nidhi wants to make her custom random module with the name myRandom(). She wants to make the following functions:
○	evenChoice() --> Selects a random even number from a given list.
○	oddChoice() --> Selects a random odd number from a given list.
○	primeChoice() --> Selects a prime number from a given list.
Create a similar module to help Nidhi.
"""
# Custom random module
# myRandom.py

import random

# function to select random even number from a given list

def evenChoice(lst):
    evens = []
    for i in lst :
        if i%2 == 0 :
            evens.append(i)

    value = random.choice(evens)

    return value

# function to select a random odd number from a given list

def oddChoice(lst):
    odds = []
    for i in lst :
        if i%2 != 0 :
            odds.append(i)

    value = random.choice(odds)

    return value

# function to check for prime numbers

def isPrime(num):
    for i in range(2,num//2):
        if num%i == 0 :
            return False
    return True

# function to select a random prime number from a given list

def primeChoice(lst):
    primes = []
    for i in lst :
        if isPrime(i):
            primes.append(i)

    value = random.choice(primes)

    return value

