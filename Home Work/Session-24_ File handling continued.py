
"""
Homework questions
	Nidhi has a bad habit of repeating the same word while typing.
	She wants a program that can remove duplicate phrases from paragraphs written by her.
	To help Nidhi write a python program that can connect with a text file and remove repeating words.
"""
# Program to remove duplicate words from a given text file

file = open("aboutPython.txt" , "r")

# Reading File

paragraph = file.read()

lastWord = ""
currentWord = ""
newParagraph = ""


for currentWord in paragraph.split(" ") :
    if lastWord != currentWord :
        newParagraph += currentWord
        newParagraph += " "

    lastWord = currentWord

# Closing file
file.close()

# Opening file again to put updated content

file = open("aboutPython.txt" , "w")

file.write(newParagraph)

file.close()

print()
print("File updated")
print()


