Homework questions
●
●	Shubh and Nidhi know how much they have scored in each subject in the examination. Now they want to calculate the overall percentage they scored. Write a program to take marks of 5 subjects in the examination and then print the overall percentage student has achieved.
●	Answer
●	# Calculating percentage based on marks
●
●	subject1 = int(input("Enter marks in first subject :"))
●	subject2 = int(input("Enter marks in second subject :"))
●	subject3 = int(input("Enter marks in third subject :"))
●	subject4 = int(input("Enter marks in forth subject :"))
●	subject5 = int(input("Enter marks in fifth subject :"))
●
●	total_marks = 500
●	marks_obtained = subject1 + subject2 + subject3 + subject4 + subject5
●
●	percentage = marks_obtained / total_marks * 100
●
●	print("Overall percentage :" , percentage)
●	.
●
________________________________________
●	Aarush recently learned probability in his school. He was finding the probability of different events and he wondered whether he can develop a program to do the same thing or not. To help Aarush create a program in python where user can enter number of favorable outcomes and total number of possible outcomes and then program will print the probability of that event on the screen.
●	Note:
●	Print the probability of the event only up to 2 decimal places. ( For this use round() function )
●	Sample run
●	>>Enter the number of favorable outcomes: 1
●	>>Enter the total number of possible outcomes: 2
●	>>Probability: 0.5

