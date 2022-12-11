"""
Mosh went to a swimming pool and he was curious to know how much water is there
inside the swimming pool. To calculate this, he measured the length, breadth, and
depth of the pool but was unable to use the measurements. To help Mosh, write a program
in python to find how much water can be stored inside the given swimming pool.
Hint: Find the volume of the cuboid. A cubic meter equals 1000 liters of water.
"""

length = int(input("Enter the length of the swimming pool :"))
breadth = int(input("Enter the breadth of the swimming pool :"))
height = int(input("Enter the height of the swimming pool :"))

volume = length*breadth*height
water = volume*1000

print("The amount of water in the pool:", water)

"""
Arvind is playing on garden slides. He wants to know the length of the 
slides but it’s a bit difficult for him to do it directly. Although he knows 
the height and width of the garden slide. Write a python program to find the length 
of the slide using height and width.
Hint: Apply Pythagoras theorem.
Note: The height of the slide is 2 meters and the length of the slide is 3 meters
"""

height = int(input("Enter the height of the slide :"))
base = int(input("Enter the base length of the slide :"))

# hypotenuse of triangle

length = ( height**2 + base**2 )**0.5

print("The length of the slide is:", length)

"""
Shubham decided to run 5km a day. He started running around the circular football 
field with a radius of 25 meters. Now He is confused and doesn’t know how many times 
he should run around the circular ground to achieve his goal. Write a program in python 
to find the answer. How many times he should run around the circular field if he increases 
his daily goal by 10%.Discuss.
Hint: Use the perimeter of the football field.
"""
goal = int(input("Enter your goal in kms :"))
goal_meters = goal * 1000

radius = int(input("Enter the radius of the field in meters :"))

pi = 3.14
perimeter = 2 * pi * radius 
rounds = goal_meters / perimeter
rounds = round(rounds)  # Round off value 

print("Number of times you should run around the field: ", rounds)



