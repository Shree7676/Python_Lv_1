Homework
    questions
A teacher gave a challenge to all the students in a class . He said to create a word that contains vowels.The student who will write a meaningful word with the maximum number of vowels present in it will win the challenge.There were around 30 students in the class and each student was trying to create the word multiple times.So Subh decided to create a python program that can take words as input and can print the number of vowels present in the word.But Shubh doesn’t know how to use for loop in python.Help Shubh to create a program that can print the number of vowels present in the word.

 Answer
# Count the number of vowels in a given word

 word = input("Type your word here :")

 vowels = 0

 for i in word:
         if (
                i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
                 vowels += 1

 print("The total number of vowels in the given word is", vowels)
.

    ________________________________________
Rishi
    sent
    a
    mail
    to
    his
    friends.The
    mail is quite
    big and wants
    to
    count
    the
    number
    of
    lines in the
    mail.He
    already
    has
    a
    program in python
    that
    can
    count
    the
    number
    of
    words
    for him but he especially wants to know the number of lines.To help Rishi write a program in python that takes a paragraph(s) as input and can print the number of lines present in the paragraph.
 Hint: count “.”
