"""
Yash had created a class rectangle and methods to get the area and perimeter of the rectangle. 
He did the same thing for square as well. Write a python program to show 
Yash how he can use the rectangle class to create the class square with the help of inheritance.
Hint: Square is a special case of a rectangle
"""
# Creating a class rectangle

class Rectangle :
    def __init__(self , length , breadth):
        self.length = length
        self.breadth = breadth

    def getArea(self):
        area = self.length * self.breadth
        return area

    def getPerimeter(self):
        perimeter = 2 * ( self.length + self.breadth )
        return perimeter

# creating class square | Inheritance

class Square(Rectangle):

    def __init__(self , side):
        self.length = side
        self.breadth = side

# Creating first square ( object )

square1 = Square(34)

area = square1.getArea()
print()
print("Area of square:",area)
perimeter = square1.getPerimeter()
print("Perimeter of square:",perimeter)
print()

# Creating first rectangle ( object )

rectangle1 = Rectangle(20 , 5)

area = rectangle1.getArea()
print("Area of rectangle :" , area)

perimeter = rectangle1.getPerimeter()
print("Perimeter of rectangle :" , perimeter)
"""
Yash now learned how he could use inheritance to create a square 
class with the help of the existing rectangle class. 
Now with the help of method overriding, he wants to change the side of the squares as well. 
He just need to redefine the method setLength() and setBreadth()
# Creating a class rectangle
"""
class Rectangle :
    def __init__(self , length , breadth):
        self.length = length
        self.breadth = breadth

    def getArea(self):
        area = self.length * self.breadth
        return area

    def getPerimeter(self):
        perimeter = 2 * ( self.length + self.breadth )
        return perimeter

    def setLength(self):
        newLength = int(input("Enter new length :"))
        self.length = newLength
        print("Length of the rectangle changed to :" , newLength)

    def setBreadth(self):
        newBreadth = int(input("Enter new width for rectangle :"))
        self.breadth = newBreadth
        print("Breadth of the rectangle set to :" , newBreadth)

# creating class square | Inheritance

class Square(Rectangle):

    def __init__(self , side):
        self.length = side
        self.breadth = side

    def setLength(self):
        newLength = int(input("Enter new side :"))
        self.length = newLength
        self.breadth = newLength
        print("Side of the rectangle changed to :" , newLength)

    def setBreadth(self):
        print("Use setLength() method to change the side")
        pass

# Creating first square ( object )

square1 = Square(34)

area = square1.getArea()
print()
print("Area of square:",area)
perimeter = square1.getPerimeter()
print("Perimeter of square:",perimeter)
print()

# Changing the side

square1.setLength()

print("After changing the side")
print()

area = square1.getArea()
print("Area of square :" , area)
perimeter = square1.getPerimeter()
print("Perimeter of square :" , perimeter)
