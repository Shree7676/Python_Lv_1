"""
Arunima created a text file on programming where she wrote the word language incorrectly many times.
Now she wants to replace the incorrect word with the correct word.
Doing it manually can take a lot of time plus she can miss out few words at the end.
To help Arunima to replace the words write a python program. Use the concept of file handling and make changes in the text file.
"""
# Opening file with python

file = open("aboutPython.txt" , "r")

# Reading content of the file

fileContent = file.read()

incorrectWord = input("Enter the incorrect word :")
correctWord = input("Enter the correct word :")

newContent = ""

for i in fileContent.split(" ") :
    if i == incorrectWord:
        newContent += correctWord

    else:
        newContent += i

    newContent += " "

# Closing file
file.close()

# Opening file again to put new content
file = open("aboutPython.txt" , "w")
file.write(newContent)

print()
print("Incorrect word replaced by correct word")
print()

"""
Ayman wants to modify one of his text files. In his text file, he wants to start a new line 
whenever he encounters a number followed by a period(.). So he decides to do the same with the help of the python program. 
Write a program for Ayman.
"""
# Opening file with python

file = open("aboutPython.txt" , "r")

# Reading content of the file

fileContent = file.read()

prevCharacter = ""
currCharacter = ""

newContent = ""

for i in fileContent:

    currCharacter = i

    if prevCharacter.isnumeric() and currCharacter=="." :
        newContent = newContent[:-1]+"\n"+prevCharacter+currCharacter

    else:
        newContent += i

    prevCharacter = currCharacter

# Closing file
file.close()

# Opening file again to put new content
file = open("aboutPython.txt" , "w")
file.write(newContent)

print()
print("Task Completed")
print()

