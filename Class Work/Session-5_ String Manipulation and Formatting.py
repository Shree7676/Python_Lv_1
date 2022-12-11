"""
A palindrome is a word, number, phrase, or other sequences of characters that reads the same
backward as forward, such as madam or racecar. Arunima got a new puppy (pet) and she wants to
decide the name for her pet. The name of the pet should be a palindrome. Write a program to
take the pet name as input and print "true" if it is palindrome or print "false" on screen.
Help Arunima to decide the name ( should be palindrome ) of the puppy.
Hint: reverse the name and compare it with the original name.
"""
original_name = input("Suggest the name for pet :")
reverse_name = original_name[::-1]
isPalindrome = (original_name == reverse_name)
print("The given name is palindrome :" , isPalindrome)

"""
Aarush and Yash are two friends in the same grade and they decided to create their secret 
language to communicate with each other. First of all, they decided to reverse each word. 
For example: come here = "emoc ereh". But this was very easy to understand for other students. 
They tried to make it a bit difficult and decided to put all the characters which are at odd 
indices first then all the characters which are at even indices. 
For example: come here = "oecm eehr". Write a program in python to create such type of 
secret language and convert the word Codeyoung into secret language using the same program. 
Can we convert the secret language back to normal language using python? Discuss
"""

original_word = input("Enter the original word :")

firstHalf = original_word[::2]
secondHalf = original_word[1::2]

secret_word = firstHalf + secondHalf

print("After conversion :" , secret_word)

"""
Vishal is creating a form and he wants to take the contact number as input. However, 
some people do not enter the number properly. Vishal is confused about how to verify 
whether the given number is in the correct format or not. To help Vishal write a python 
program to show how we can verify whether a given phone number is valid or not. 
Note: A valid phone number contains 10 digits with 9,8 or 7 as the first digit. 
Phone number only contains numbers and not any character.
Hint: 
User len() function to verify the number of digits.
Use isnumeric() function to check it only contains numeric values.
Use indexing to check whether the first character is 9,8 or 7 or not. 
"""

num=input("Enter Number= ")
print("number is numeric ",num.isnumeric())
print("Length of num=10",len(num)==10)
print("Num starts with 9 or 8 or 7",num[0]==9 or num[0]==8 or num[0]==7) # if else not used bcz its not yet covered ...next topic


