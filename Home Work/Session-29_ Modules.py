"""
Homework questions
Arvind worked with the getArea() module and now he wants to make the getPerimeter() module as well to get the perimeter of different shapes. Create a getPerimeter() module in python to help him. Using the above module create a separate py file to find the length of the tape that would be required to mark the perimeter of a cricket field of radius 70m
"""
# Module to get the perimeter of different shapes
# getPerimeter.py

# function to find the perimeter of the square

def square(side):
    perimeter = side*4
    return perimeter

# function to find the perimeter of the rectangle

def rectangle(length , breadth):
    perimeter = 2*(length+breadth)
    return perimeter

# function to find the perimeter of the circle

def circle(radius):
    pi = 3.14
    perimeter = pi*radius*2
    return perimeter



