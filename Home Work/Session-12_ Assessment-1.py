
"""Homework questions

Ayman is confused between odd, even, prime, and composite numbers.
To help him write a python program that takes a number as input from
the users and prints the following properties about the number.
For example :
------------------
12
Even
Composite
------------------
13
Odd
Prime
------------------
"""
# Program to check whether the number is :
# Prime or Composite and
# Odd or Even

number = int(input("Enter the number :"))

# Odd or Even

if number%2 == 0 :
    print("Even")
else :
    print("Odd")

# Prime or Composite

flag = 1
for i in range(2, number//2):
    if number%i == 0 :
        flag = 0
        break

if flag == 1 :
    print("Prime")
else:
    print("Composite")




