"""
In a school, a football competition is going to be held. The sports captain needs to create a list 
of the players with their heights. According to the rule, only those students can participate in 
the competition who have a height greater than 167cm. To make things easier write a python program. 
Create a list of tuples with the name of the player and their height in cm. 
Note: while taking the input from the users, don’t include the players whose height is less than 167cm. 
( Use continue statement )
Sample list: [ (“Chris” , 170) , (“Aditya” , 182) , (“Chirag” , 176 ) ]
"""
num = int(input("Enter the number of players : "))
players = []
for i in range(num):
    name = input("Enter your name :")
    height = int(input("Enter your height :"))
    if height < 167 :
        continue
    players.append((name,height))

print(players)
"""
Nidhi is interested to know how many palindrome numbers are there in the first one thousand numbers. 
Also, she wants to look at all the palindrome numbers in one place. Write a python program that can 
create a list of all palindrome numbers in the first one thousand numbers.
"""
lst = []

for i in range(1001):
    temp = i
    rev = 0
    while(temp>0):
        lastDigit = temp%10
        rev = rev*10 + lastDigit
        temp //= 10

    if i == rev :
        lst.append(i)

print()
print("Number of palindrome numbers :" , len(lst))
print()
print("List of all the palindrome numbers are :")
print(lst)

"""
Shubham created a list and now he wants to remove all the duplicate elements from that list. 
Write a program to remove repeating elements from a list.
Sample list: [4,9,7,12,67,4,68,43,25,4,90,75]
"""
lst = [5,6,8,7,5,5234,234,564,56,23,4,564,1,231,23,41,54,2,1,3,5,35,98,5,4,5,5,5,5,4,54,54,74,54,54,5,5,5,55,5,5,5,5,5,7,8,78,7,7,7,4,1,4,44,4]
print("This is the list before removing duplicates :")
print(lst)

uniqueList = []

for i in lst:
    if i not in uniqueList:
        uniqueList.append(i)

lst = uniqueList

print()
print("List after removing duplicates :")
print(lst)


#Alternate way
# Removing the duplicate elements from a given list

lst = [1,2,3,4,5,4,4,4,4,5,6,7,7,7,1]

i = 0

while i < len(lst):
    element = lst[i]
    j = i+1
    while j < len(lst):
        if element == lst[j] :
            lst.pop(i)
            continue
        j += 1
    i+=1

print(lst)


