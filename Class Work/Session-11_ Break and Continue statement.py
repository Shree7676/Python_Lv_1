In-class exercise

●	Ayman created a python program where he took the full name of the student as input as his teacher told him to collect the name of all the students in a class. Now Ayman wants to print only the first name on the screen due to some reason. Write a python program that can print the first word of the name using a break statement.
●	Answer :
●	Code:
➔	name = "Arunima Sharma"
➔
➔	for i in name :
➔	    if i == ' ' :
➔	        break
➔	    print(i , end="")
●

________________________________________

●
●	Saisha created a python program where she takes the input from the user and saves it as a text file. But the text file which she saves has a limit of very few characters. So she wants to save the sentences after removing the spaces between the words and make the first character of each word capital. To help Saisha in this program create a python program that can take input from the user, remove the spaces between the word, make the first character of each word capital, and print it on the screen.
●	For example: Convert
●	I like programming. → ILikeProgramming
●	Answer :
●	Code
➔	sentence = input("Enter the sentence : ")
➔	flag=0
➔	for i in sentence :
➔	    if i == ' ':
➔	        flag=1
➔	        continue
➔	    if flag == 1 :
➔	        print(i.upper(), end="")
➔	    else:
➔	        print(i , end="")
➔	    flag = 0
●	.
●
________________________________________
●	Nidhi challenged her friends to check whether a given number is palindrome or not without using string manipulation. All her friends were not able to solve this problem. Write a program in python for the same.
●	Hint: Use a while loop and a temporary variable.
●	Answer
➔	# Check whether the given number is palindrome or not
➔
➔	number = int(input("Enter a number:"))
➔	temp = number
➔	rev = 0
➔
➔	while(temp>0):
➔	    lastDigit = temp%10
➔	    rev = rev * 10 + lastDigit
➔	    temp //= 10
➔
➔	if number == rev :
➔	    print("The given number is palindrome")
➔
➔	else:
➔	    print("The given number is not a palindrome")
➔	.
➔	.
➔
________________________________________
