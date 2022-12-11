"""
Homework questions
Shubham had created a BMI calculator to check his health condition daily.
But he is not able to record the values. He wants to see how his BMI is changing.
So he decided to connect his BMI program with a text file using the concept of file handling.
Now, when he uses his BMI program, his height, weight, BMI, and date get added to a text file "bmi.txt".
Create a program that can do the same thing for you.
"""
# Find the BMI report
from datetime import date

file = open("myBMI.txt" , "a")

height = int(input("Enter your height in cms :"))
heightInMeters = height/100

weight = int(input("Enter your weight in kgs :"))

bmi = weight / heightInMeters ** 2

print("Your bmi is :" , bmi)

if(bmi<18.5):
    print("Your are underweight")
elif(bmi>24.9):
    print("Your are overweight")
else:
    print("Your bmi is at healthy range")

currentDate = str(date.today())
height = str(height)
weight = str(weight)
bmi = str(bmi)

# Generating record to insert
record = "On "+currentDate+" | height:"+height+"cms | weight:"+weight+"kgs | BMI:"+bmi

# Writing content in the text file
file.write(record)


"""
Arvind has a huge text file and he wants to put a serial number at the beginning of each line. 
Doing this task manually can take a lot of time. He is not aware of python file handling. 
Write a python program that can put a serial number in front of each line in any specified text file.
"""
# To read the content of a given text file

# Opening file with python

file = open("aboutPython.txt" , "r")

# Reading content of the file

fileContent = file.read()

newContent = "1. "

lineNumber = 2
for i in fileContent :
    if i == "\n":
        newContent += i
        newContent += str(lineNumber)
        newContent += ". "
        lineNumber+=1
    else:
        newContent += i

# Closing file
file.close()

# Opening file again to put new content
file = open("aboutPython.txt" , "w")
file.write(newContent)

print()
print("Serial Numbers added to the text file.")
print()



