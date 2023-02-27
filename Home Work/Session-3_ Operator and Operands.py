"""
Nidhi loves to travel to different countries. She is now in a country where the
temperature is measured in Fahrenheit and she is not able to understand it in a better way.
To help her in this situation, write a program to convert temperature from Fahrenheit to celsius.
Hint: (0°C × 9/5) + 32 = 32°F #f-32*(9/5)
"""
f=int(input("Farenheat = "))
c=f-32*(9/5)
print("Celsius = ",c)

"""
In a school, the teacher asks students to tell whether the given number on the board is odd or even. 
Students were taking a lot of time to find out the answer. But Chirag realized that even and odd depends 
only on the last digit of the number. So write a program in python to take a number as input and then print only 
the last digit of the number. Also, discuss whether the given number is odd or even. If given number is even then print 
True on the screen and if the given number is odd then print False on the screen.
Hint: Take the number as input and then use “%10” to extract the last digit of the given number.
"""
# If last digit of number is 0, 2, 4, 6, 8 -> Even
# If last digit of number is 1, 3, 5, 7, 9 -> Odd
number = int(input("Enter the number :"))
lastDigit = number%10
print("The last digit of the number is :" , lastDigit)
print(lastDigit%2==0)

"""
Shubham and his two more friends decided to share their chocolates equally among them. 
But they couldn't divide chocolates equally as they need a few more chocolates. 
Write a program to take three inputs for the number of chocolates and then print 
how many more chocolates they need to buy to divide it equally.
"""
first = int(input("Enter total chocolates with first child :"))
second = int(input("Enter total chocolates with second child :"))
third = int(input("Enter total chocolates with third child :"))

total_chocolates = first + second + third 
extra_chocolates = total_chocolates % 3
required_chocolates = 3 - extra_chocolates

print()

print("Extra number of chocolates they need to buy:", required_chocolates)
