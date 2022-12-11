"""
Yash, Shubham, and Rishi are three friends and they want to know who is good at mathematics among them.
For this, they want to make a competition to declare the winner. Rishi wants to create a python program for the competition.
The program should generate ten random questions like 123+456, 754-34, etc.
Then it should ask the user to enter the correct answer and also calculate the time taken for each answer.
At the end, it should show an overall score out of 10 and the time taken by the user to answer all the questions.
Create such a program to help Rishi and also check who is good at calculations among your friends.
# Creating mathematics quiz
# Create random arithmetic questions
"""
import random
import time


# function to create the random questions

def createQuestion():
    operators = ("+" , "-" , "*" , "/")
    operator = random.choice(operators)

    if operator == "+" :

        number1 = random.randint(1,1000)
        number2 = random.randint(1,1000)

        question = str(number1) + operator + str(number2)

        return question

    elif operator == "-" :

        number1 = random.randint(1,1000)
        number2 = random.randint(0 , number1)

        question = str(number1) + operator + str(number2)

        return question

    elif operator == "*" :

        number1 = random.randint(1,100)
        number2 = random.randint(1,10)

        question = str(number1) + operator + str(number2)

        return question

    else :
        number1 = random.randint(1,100)
        number2 = random.randint(1,10)
        while(number1%number2 != 0):
            number1 = random.randint(1,100)
            number2 = random.randint(1,10)

        question = str(number1) + operator + str(number2)

        return question

# function to get the answer of the question

def getAnswer(question):
    answer = eval(question)
    return answer

score = 0
start = time.time()

for i in range(10):
    print()
    question = createQuestion()
    print("Question.",i+1," :")
    print(question)
    print()
    usrAns = input("Enter your answer :")

    if usrAns.isnumeric():
        if int(usrAns) == getAnswer(question) :
            score += 4

        else :
            score -= 1

    elif usrAns == "" :
        score += 0

    else :
        print("Invalid Input | No change in score")



end = time.time()

time_taken = end - start
minutes = int(time_taken/60)
seconds = int(time_taken%60)


print("Your Score :" , str(score)+"/40")
print("Time Taken :" , minutes , "Minutes and" , seconds , "Seconds")



