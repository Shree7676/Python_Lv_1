"""Arvind wants to unlock his father's mobile. The mobile contains a four-digit password that includes numbers
from 1 to 9 without repetition of any number. He wants to know the number of possible passwords in this situation.
Write a program in python to find the maximum number of attempts required by Arvind to unlock the mobile.
Assume: Arvind is not aware of the correct password already
Hint: Use loops
"""
# Find the number of attempts

password_length = int(input("Enter the length of the password"))
numbers_included = int(input("Enter total number of digits included :"))

maxPossiblePassword = 1

upperLimit = numbers_included
lowerLimit = upperLimit - password_length + 1

print(upperLimit)
print(lowerLimit)

for i in range(lowerLimit , upperLimit + 1):
    maxPossiblePassword *= i

print("Maximum number of attempts required :" , maxPossiblePassword)


"""
Rishi knows how to check whether a given number is prime or not. 
But he wants to get the list of all the prime numbers which occur within a given range. 
The nested loop is making the program complicated for him. 
Use functions and help Rishi to get the list of prime numbers.
Hint: Use for loop and call function to check whether a number is prime or not.
"""
# Creating a list of prime numbers in a given range

# Function to check Prime
def isPrime(num):
    for i in range(2,num//2):
        if num%i == 0 :
            return False
    return True

start = int(input("Enter the lower limit :"))
end = int(input("Enter the upper limit :"))

primeList = []

for i in range(start , end):
    if isPrime(i):
        primeList.append(i)

print("List of prime numbers :")
print(primeList)

"""
Yash has a file that might contain continuous duplicate words. 
He wants to remove all the repeating words. To help Yash in doing so, 
write a program in python that can remove repeating words.
"""
# Program to remove duplicate words from a given paragraph

paragraph = input("Paste/Write your paragraph here :")

lastWord = ""
currentWord = ""
newParagraph = ""


for currentWord in paragraph.split(" ") :
    if lastWord != currentWord :
        newParagraph += currentWord
        newParagraph += " "

    lastWord = currentWord

print()
print("Paragraph without repeating words :")
print()
print(newParagraph)
