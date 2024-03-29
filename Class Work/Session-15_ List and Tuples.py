"""In-class exercise
5 friends decided to go for a picnic and they start discussing the items which they have to take with them. They wanted to create a list where they can add items one by one. To help them, write a program in python to create an empty list. Then use for loop and append() method to add items one by one. ( Note: Range of loop depends on the number of items that have to be included in the list.) After adding all the items ask whether the user whether wants to remove any items or not and then print the whole list on the screen.
Answer"""
items = []
total_item = int(input("Enter the number of items for the list :"))

for i in range(total_item):
    item = input(f"Enter item -{i+1}:")
    items.append(item)

print()
print("This is the list of items :")
print(items)

remove_items = int(input("Enter the number of items to be removed :"))

for i in range(remove_items):
    item = input("Enter item to remove :")
    items.remove(item)

print()
print("The final list of items are :")
print(items)

"""A teacher created a list of names of the students. Now teachers want to get the name of all those students whose name starts with the letter “A”. To help the teacher write a python program and create a list of names of students. Then print the names which start with the letter “A”. (Hint: Use for loop and give condition I [0] == “A” )
"""
# Creating an initial list

students = []
student_count = int(input("Enter the number of students :"))

for i in range(student_count):
    student = input(f"Enter name of the student {i+1} :")
    students.append(student)

print()
print("This is the list of students :")
print(students)

# Extracting names of students starting with character 'A'

studentsWithA = []

for i in students :
    if i[0] == "A" :
        studentsWithA.append(i)

print()
print("This is the list of students whose name starts with 'A' :")
print(studentsWithA)


"""
In a class, the teacher decides to assign roll numbers to the students in alphabetical order of their names. The class consists of more than 60 students. So the class monitor decides to create a list in python to take the name of the students in any order and then will print the list in sorted order with roll numbers. ( Hint: use append() method to add the names in the list and then use sort() method on the list ) . After sorting the list, the Index number of the list can be used to assign the roll numbers to the students. ( Hint : roll no = index + 1 )
"""
# Creating an initial list

students = []
student_count = int(input("Enter the number of students :"))

for i in range(student_count):
    student = input(f"Enter name of the student {i+1} :")
    students.append(student)

print()
print("This is the list of students :")
print(students)

# Sorting list
students.sort()
print(students)

# Assigning roll numbers to the students in alphabetical order

size = len(students)

print("Roll Number , Name")

for i in range(size):
    print(i+1 , students[i])

