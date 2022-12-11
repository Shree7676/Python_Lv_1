"""
A teacher told students to write an essay on themselves.
Nidhi created a python program that can generate an essay just by taking inputs.
She shared the program with her friends to help them. Write a python program that
can take inputs like name, age, address, etc, and convert it into an essay.
"""
name = input("Enter your name :")
age = input("Enter your age :")
address = input("Enter your address :")
school = input("Enter name of your school :")
grade = input("Enter your grade")
f_name = input("Enter your father's name :")
f_occupation = input("Enter your father's occupation :")
m_name = input("Enter your mother's name :")
m_occupation = input("Enter your mother's occupation :")

# Generating essay using these variables
print()
print("Essay on Myself")
print()
print("My name is", name,"and I am", age, "years old. I stay at", address, "and I study in ")
print(school,". I am in class", grade, ". My father’s name is", f_name, "and he is")
print(f_occupation, "My mother’s name is", m_name, "and she is a", m_occupation)


"""
Rakshita wants to create a simple chatbot using python language. 
Write a program in python to help Rakshita in creating the chatbot.
Hint: with the help of variables store the answers of the user and 
use it for further conversation by the chatbot.

Example :
>>
Hi, I am a chatbot. What is your name?
>>Nidhi
Oh, Nidhi in which grade you are right now?
>>8
Nidhi you are in 8th grade. Can I ask you one question? yes or no?
>>yes
Tell me 1024+98=?
>>1122
Good! Your answer is correct. Bye
>>bye
"""

name=input("Hi, I am a chatbot. What is your name? \n")
grade=input(f"Oh, {name} in which grade you are right now? \n")
que=input(f"{name} you are in {grade}th grade. Can I ask you one question? yes or no?\n")
que1=input("Tell me 1024+98=?\n")
ans="1122"==que1
bye=input(f"Your answer is {ans}. Bye\n")

"""
Himanshu sells notebooks. Sometimes it becomes a bit difficult for him to 
calculate the total amount to charge from the customer. 
To help Himanshu create a program that asks the user to enter the number of books 
to buy and then print the amount to be paid.
Hint: Assume the cost of one notebook - $2
"""

num=int(input("enter the number of books"))
print("amount to be paid=",num*2)
