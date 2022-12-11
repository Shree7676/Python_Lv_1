"""
A school has the following rules for the grading system.
a. Below 25 - F
b. 25 to 45 - E
c. 45 to 50 - D
d. 50 to 60 - C
e. 60 to 80 - B
f. Above 80 – A

By mistake, the grades ( A, B, C, D, E ) were not printed in some of the student's mark sheets.
They want to know their grades, but they are confused with the grading system.
Himanshi decided to create a python program where students can enter their marks and
it will show their grades on the screen. However, she got stuck in between with her program.
So write a program in python to solve the same issue and help Himanshi. What did you learn from Himanshi? Discuss.
Ask the user to enter marks and print the corresponding grade.
"""
# Find grades on the basis of marks

marks = int(input("Enter your marks :"))
grade = Z

if marks < 0 :
    grade = "Invalid"

elif marks < 25 :
    grade = "F"

elif marks < 45 :
    grade = "E"

elif marks < 50 :
    grade = "D"

elif marks < 60 :
    grade = "C"

elif marks < 80 :
    grade = "B"

elif marks < 100 :
    grade = "A"

else:
    grade = "Invalid"

print("Your grade is :", grade)

"""
Raju is in first grade and his teacher has assigned him a few questions. 
He needs to find the greatest among three given numbers. He has to solve the question as given below.

After solving all the questions he is not sure whether his answers are correct or not. 
To help Raju write a program in python where he can enter three different numbers 
and can get the greatest among all the three numbers on the screen.
Hint: Use if-elif-else condition and compare all the three values with each other.
"""