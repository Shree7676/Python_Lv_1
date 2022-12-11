"""
Homework questions
Yash created a class square ( shape ) to create squares of different dimensions.
Also, he developed methods to get the area and perimeter of the squares.
Now he wants to develop a similar class for rectangle ( shape ) as well.
Also, he wants to add methods to change the dimensions of the rectangle.
Help Yash in creating the class rectangle.
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

    def setLength(self):
        newLength = int(input("Enter new length :"))
        self.length = newLength
        print("Length of the rectangle changed to :" , newLength)

    def setBreadth(self):
        newBreadth = int(input("Enter new width for rectangle :"))
        self.breadth = newBreadth
        print("Breadth of the rectangle set to :" , newBreadth)

# Creating first rectangle ( object )

rectangle1 = Rectangle(20 , 5)

area = rectangle1.getArea()
print("Area of rectangle :" , area)

perimeter = rectangle1.getPerimeter()
print("Perimeter of rectangle :" , perimeter)
"""
Arvind loves playing video games. He wants to know how players in the game are 
created with the help of object-oriented programming.  
To show this to Arvind, create a class Player and create different players ( objects ) 
using the class Player. Create methods like walk, run, jump, move left, and move right, etc. 
also gender, height, and weight should be the attributes of the class player.
"""
# Creating class Player

class Player:
    def __init__(self , gender , height , weight):
        self.gender = gender
        self.height = height
        self.weight = weight

    def walk(self):
        print("Player is walking ...")
        # program to make players walk in the game

    def run(self):
        print("Player is running ...")
        # program to make players run in the game

    def jump(self):
        print("Player is jumping ...")
        # program to make players jump in the game

    def moveLeft(self):
        print("Player is moving left ...")
        # program to make players move left in the game

    def moveRight(self):
        print("Player is moving right ...")
        # program to make players move right in the game


# Creating a player ( object )

player1 = Player("Male" , 175 , 75)

# Player actions
print()
player1.walk()
player1.run()
player1.jump()
player1.moveLeft()
player1.moveRight()
print()

# Creating few more players

player2 = Player("Female" , 155 , 45)
player1 = Player("Male" , 167 , 67)


