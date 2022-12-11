"""Abel is in first grade and he is confused with the positive and negative numbers. 
He doesn’t know when a number is positive and when a number is negative. His teacher 
has given him a few numbers and told him to write positive negative in front of those numbers as homework. 
He is confused. To help Abel write a program in python that can take a number as 
input and can print positive, negative, or 0 according to the number.
"""

"""Abel understood positive and negative numbers and now he wants to understand odd and even numbers. 
His teacher has given him some numbers to check whether they are odd or even. 
To help Abel write a program in python to check whether a given number is odd or even.
"""

"""
Rahul is measuring the ph level of different solutions. Write a program in python to show the nature of the solution on based on pH level. Follow the given rule:
pH level	- 	solution
1 - 3 			strong acid
4 - 6 			weak acid
7 			neutral
8 - 11			weak base
12-14			strong base
Else			not valid ph level
Take pH level as input and print the nature of the solution on the screen.
"""


"""
Chris looked at the calendar and found that a few months consist of 31 days and 
other months consist of only 30 days. ( February contains only 28/29 days - exceptional ). 
Chirs already knew that we denote the months in numbers like 
January – 1, February – 2, March – 3, April – 4, May – 5, etc. Based on Chris's observation 
write a program in python where we can put the month as input and 
it will show the number of days that month contains. ( Hint: Use "if – elif – else" condition ).
"""
# Check number of days in a month

month = int(input("Enter number for month :"))

if (month >=1 or month <= 12):
    if(month == 2):
        print("Contains 28/29 days")

    elif(month%2 == 0 and month <= 7):
        print("This month contains 30 days")

    elif(month%2 != 0 and month >=8):
        print("This month contains 31 days")

else:
    print("Invalid month")

