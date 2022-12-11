"""Mini-Project 5
Rishi wants to check how fast he can type. He created a program in python to check his typing speed.
Finally, he came to know that his typing speed is 180 CPM ( Click Per Minute ) / 38 WPM ( Word Per Minute )
with an accuracy of 93%. Write a program like Rishi and check your typing speed and accuracy.

Hint: Use for loop
"""
# Program to check the typing speed

import time
import random

while True :
    print()
    print("--Check your typing speed here--")
    print()
    print("1 -> Select a random sentence :")
    print("2 -> Create your own sentence :")
    ch = int(input("Enter your choice :"))

    if ch == 1 :
        sentence1 = "Python can be easy to pick up whether you're a first time programmer or you're experienced with other languages."
        sentence2 = "Programming is the process of creating a set of instructions that tell a computer how to perform a task."
        sentence3 = "A computer is a machine that can be programmed to carry out sequences of arithmetic or logical operations automatically."
        sentences = (sentence1 , sentence2 , sentence3)
        sentence = random.choice(sentences)
        break

    elif ch == 2 :
        sentence = input("Enter your sentence here :")
        break

    else:
        print("Invalid input")
        print("Please try again ...")

print()
confirm = input("Press enter to start :")
print()

start = time.time()
print(">>",sentence)
write = input(">> ")
end = time.time()

time_taken = end - start
minutes = time_taken/60

sentence_length = len(sentence)
write_length = len(write)

score = 0

for i in range(min(sentence_length , write_length)):
    if sentence[i] == write[i] :
        score += 1

cpm = score/minutes
wpm = int(cpm/4.5) # Each word contains approximately 4.5 characters
accuracy = (score/sentence_length)*100

print()
print("--Your Result--")
print("CPM :" , cpm)
print("WPM :" , wpm)
print("Accuracy :" , accuracy)
print()

