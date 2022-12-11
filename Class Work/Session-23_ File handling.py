"""
Priyanka wants to read a text file using python and she wants to print the content of that file in the terminal. But she is unable to specify the file name correctly. To help Priyanka write a program in python and show how to read the content of the text file and print it on the screen using python.
Name of the text file: aboutPython.txt
Content:
Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. It's high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together. Python's simple, easy to learn syntax emphasizes readability and therefore reduces the cost of program maintenance. Python supports modules and packages, which encourages program modularity and code reuse. The Python interpreter and the extensive standard library are available in source or binary form without charge for all major platforms, and can be freely distributed.
.
Hint:
Create a text file aboutPython.txt
Copy the given content in that file
Using python read the content of the file.
Use the concept of file handling.
"""
# To read content of a given text file

# Opening file with python

file = open("aboutPython.txt" , "r")

# Reading content of the file

fileContent = file.readlines()

# Printing the content
for i in fileContent :
    print(i)

# Closing file

file.close()



"""
Himanshi has a text file and she wants to check whether that file contains any numerical value. 
So to help Himanshi write a python program that can check whether the text file includes any numerical value or not. 
As text files contain so many lines, so print the line number that has numerical values.
"""
# To read content of a given text file

# Opening file with python

file = open("aboutPython.txt" , "r")

# Reading content of the file

fileContent = file.read()

# Checking for numerical value

flag = 0
lineNumber = 1
for i in fileContent :
    if i.isnumeric():
        flag=1
        break
    if i == "\n":
        lineNumber+=1

print()

if flag == 1 :
    print("Yes numerical value is present")
    print("On line :" , lineNumber)

else :
    print("No numerical value exist in the program")

# Closing file

file.close()

