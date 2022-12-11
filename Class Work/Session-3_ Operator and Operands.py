"""
Nidhi and Shubh are two students in the same grade. They have a total of 3 subjects in the school.
After examination, they want to check whether their total marks are equal or not. So to help them
write a program in python to take marks as input from two students. Print the overall score of both
the students. Also, print "true" if they have an equal score or print "false" on the screen.
Hint: Take the input for marks and then use the “==“ operator to print the answer.
"""
print("Marks of first Student")
physics = int(input("Enter your marks in Physics :"))
chemistry = int(input("Enter your marks in Chemistry :"))
mathematics = int(input("Enter your marks in Mathematics :"))

first_student_total = physics + chemistry + mathematics

# Marks of the second student

print("Marks of second Student")
physics = int(input("Enter your marks in Physics :"))
chemistry = int(input("Enter your marks in Chemistry :"))
mathematics = int(input("Enter your marks in Mathematics :"))

second_student_total = physics + chemistry + mathematics

print()

print("Total score of first student :" , first_student_total)
print("Total score of second student :" , second_student_total)

condition = first_student_total == second_student_total

print("Total Score is equal :" , condition)

"""
Varun is using a stopwatch to calculate his running speed. 
The stopwatch shows the time taken in seconds. He wants to convert it into minutes and seconds. 
Write a program to help him with this.

Example:
For input :
Enter the number of seconds:  125 
Output :
>> 2 minutes and 5 seconds

"""
sec=int(input("Enter the number of seconds:\t"))
print(sec//60,"minutes",sec%60,"seconds")


"""
Varun measures his running speed in kilometers per hour. 
For a better understanding, he wants to know his speed in meters per second as well. 
But he is facing a problem in calculating his speed in meters per second. 
Write a program for Varun where he can enter the speed in kilometers per hour and 
he can get the speed in meters per second.
Hint: divide the speed value by 3.6
"""
km=int(input("enter the speed in kilometers per hour: \t"))
print("speed in meters per second=",km/3.6)