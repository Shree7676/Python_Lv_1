"""
Part-1
In a school a teacher was assigning questions for homework to the students.
The teacher randomly selected some textbook exercise questions and told students
to note the question number. Rohit wanted to solve all the questions in order but
he had written question numbers in random order. To help Rohit in arranging the question
numbers in ascending order, write a program in python that takes different numbers as
input given by the user and print it in ascending order.
Hint:
Take the input from the user and store the numbers in a list.
Sort the list using nested for loops.
Note: Don’t use the inbuilt sort function/method to sort the list.
Sample run:
>> Enter total number of questions: 4
>> Enter question numbers here:
>>23
>>7
>>15
>>3
>>Selected questions are: [ 23,7,15,3 ]
>>Selected questions in order: [ 3,7,15,23 ]

"""

"""
Part-2
Rohit was not able to solve a few questions given by his teacher. 
But still he wanted to maintain the order of solving questions. 
He thought of leaving the pages for those questions that he is not able to solve. 
So now he wants to know the page number where he has to write the solution to a specific question. 
( Assume page number starts from 1 ). To help Rohit in this 
modify the existing program so that it can take the question number as 
input and can print page number for that question.
Hint:
Search for the question in the list and print index+1 on the screen.
Example:
If Selected questions in order is [ 3,7,15,23 ] ( same as above )
Then, sample run
>> Enter the question number: 15
>> Solve it on page number 3.
.
Note: If question number is not available in the list then print
>> you don’t have to solve this question.
"""
