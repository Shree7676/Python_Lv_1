"""
All the information displayed on the PAN Card are in capital letters only. It doesn’t
matter how you entered the value. In the same way, Jesna is creating a form where she
wants to take the input and display the information only in capital letters.
To help Jesna write a program in python that can make any string value to the capital letters.
Take the basic informations from the user and display it in capital letters.
Hint: Use upper() method.
"""
data=input("enter ur data : ")
print(data.upper())
"""
The date consists of three different parts. Date – Month – Year, where date 
contains maximum two-digit, month, consists of maximum two-digit, and the year 
consists of maximum four-digit. Saahil is a boy who is still confused with the format of the date. 
He wants a program to practice with different dates to check whether it is valid or invalid. 
Write a program in python to take three inputs from the user like date, month, and year and 
then print whether the given date is valid or not.
Hint: Use “==” operator and use logical operator to combine the conditions.
Note: Don’t include leap year. ( Assume February always contains 28 days)
"""

date = int(input("Enter date :"))
month = int(input("Enter month :"))
year = int(input("Enter year :"))

# First condition for correct date
correct_date1 = ((date >= 1 and date <=31) and (month% 2 != 0) and (month != 2)) 
# Second condtion for correct date
correct_date2 = ((date >=1 and date<=30) and (month%2 == 0) and (month != 2))
# Third condition for correct date
correct_date3 = ((date >=1 and date <=28) and (month == 2))

correct_date = correct_date1 or correct_date2 or correct_date3
correct_month = (month >= 1 and month <= 12)
correct_year = (year >= 1)

correct_date_format = correct_date and correct_month and correct_year

print("This is correct date format :" , correct_date_format)


