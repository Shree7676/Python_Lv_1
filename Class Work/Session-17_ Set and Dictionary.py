"""
Sahil creates a list of fruits and prints the values.
Most of the time while creating the list, He enters some value multiple times.
He doesn’t want to repeat the value. Write a python program and use a set instead of a list.
Take the input from the users until users select to discontinue.
And print all the unique values at the end.
Hint: Use a while loop to repeat the main program and use the set to store the value.
"""
fruits = set()
while(True):
    value = input("Enter the name of the fruit : ")
    fruits.add(value)
    ch = int(input("Enter 0 to quit or any key to continue :"))
    if ch == 0 :
        break

for i in fruits:
    print(i)

"""
Chris recently got to know about his marks which he scored in various subjects. 
Now he wants to store his marks in the form of a dictionary. 
Write a python program to help Chris and his friends to store the marks inside the dictionary. 
Print the dictionary with the total marks of the student.
"""
score = {}
num = int(input("Enter the number of subjects : "))
for i in range(num):
    subject = input("Enter the name of the subject :")
    marks = int(input("Enter the marks :"))
    score[subject] = marks

print(score)
print("Total marks :" , end=" ")
print(sum(score.values()))
"""
Chris successfully stored his marks inside the dictionary. 
Now he wants to put all the data of his class inside a nested dictionary. 
He got confused while using the nested dictionary. 
Help him to write the program for the nested dictionary.
"""
# Marks of first student
marks1 = {"Math" : 100 , "Science" : 99 , "English" : 92}
# Marks of second student
marks2 = {"Math" : 90 , "Science" : 89 , "English" : 99}
# Marks of third student
marks3 = {"Math" : 94 , "Science" : 91 , "English" : 95}

# Marks of all the students with student names
students = {"student1" : marks1 , "student2" : marks2 , "stdents3" : marks3}

print(students)



