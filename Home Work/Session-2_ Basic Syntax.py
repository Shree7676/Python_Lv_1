"""
Shubh is excited to do something mathematical in python. He decided to create a program
that could add, subtract, multiply and divide two numbers. To help Shubh write a python
program to apply addition, subtraction, multiplication, and division between two numbers.
"""
first_number = int(input("Enter first number :"))
second_number = int(input("Enter second number :"))

addition = first_number + second_number
subtraction = first_number - second_number
multiplication = first_number * second_number
division = first_number / second_number

print("Sum of numbers is :" , addition)
print("Difference in numbers :" , subtraction)
print("Product of numbers is " , multiplication)
print("Division of numbers is :" , division)

"""
Rakshita wants to calculate her age. So she subtracted her year of birth from the current year. 
Her classmates also wanted to find their age in the same way. So she decides to write a 
python program where students can input their year of birth, then the program will print their age. 
Write the same program to find your age and help your classmates in finding their age
"""
birth_year = int(input("Enter your year of birth :"))
current_year = 2021
age = current_year - birth_year
print("Your age is :" , age) 
