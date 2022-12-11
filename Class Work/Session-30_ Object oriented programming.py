"""
Shubham wants to create a car racing game. But he is not aware of object-oriented programming.
Using the concept of OOP, show him how we can create a class of the car.
With parameters(brand, color, weight, height, and length) also add methods for
start, stop, increase speed, decrease speed, turn on headlights, and turn off headlights.
Also, create different objects(cars) using the class car.
"""
# Creating the class for the car

class Car:
    def __init__(self, brand, color, weight, height, length):
        self.brand = brand
        self.color = color
        self.weight = weight
        self.height = height
        self.length = length

        self.engine = "OFF"
        self.headLights = "OFF"

        self.wheels = 4 # for all cars | wheels = 4

    def start(self):
        self.engine = "ON"
        print("Starting Car")

    def stop(self):
        self.engine = "OFF"
        print("Stopping car")

    def increase_speed(self):
        print("Increasing speed")

    def apply_break(self):
        print("Applying break")

    def onHeadLights(self):
        self.headLights = "ON"
        print("Turning on headlights...")

    def offHeadLights(self):
        self.headLights = "OFF"
        print("Turning off headlights")

# Creating car - bmw

bmw = Car("BMW" , "black" , 1020 , 1.4 , 5.2)

# Printing information about the car

print("Information about car")
print()
print("Brand :", bmw.brand)
print("Color :", bmw.color)
print("Weight :", bmw.weight)
print("Height :", bmw.height)
print("Length :", bmw.length)
print()

# Checking whether the car is working properly or not :D

print("Checking engine..")
print()
print(bmw.engine)
bmw.start()
print(bmw.engine)
bmw.stop()
print(bmw.engine)

print()
print("Checking headlights..")
print()
print(bmw.headLights)
bmw.onHeadLights()
print(bmw.headLights)
bmw.offHeadLights()
print(bmw.headLights)

"""
Nidhi just learned object-oriented programming, now she thinks that she can create data structures 
like lists, tuples, sets, and dictionaries. But she has no idea how to create a constructor for this problem. 
To explain this, create a class book that can store values(t consider each element as one page of the class book ) 
like a list but it should have a method only to add new elements and not remove them. 
Include show method as well in the program to print all the pages ( elements ) of the book.
"""
# Creating class Book

class Book:
    def __init__(self):
        self.pages = []

    def add(self , page):
        self.pages.append(page)

    def show(self):
        for i in self.pages:
            print(i)

# Creating books ( Object )

book1 = Book()

print()
print("Adding pages to book")
print()
book1.add("page1")
book1.add("page2")
book1.add("page3")

print("Displaying pages")
print()
book1.show()
print()
