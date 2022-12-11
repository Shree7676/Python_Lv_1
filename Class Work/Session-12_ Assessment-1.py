Assessment question

●	Aarush wants to create his application in python. He just knows the basics and wants to create something useful. Finally, he decided to create a calculator. He added some extra functionality which was useful for him. Taking inspiration from Aarush, Create your functioning calculator.
●	Note :
●	Add the basic functions in the calculator like addition, subtraction, multiplication, and division.
●	Put the entire program inside a loop so that users don’t need to run the program again and again to calculate anything.
●	Handle all the exceptions.
●
●	Answer
➔	# Calculator
➔
➔	while True :
➔
➔	    first = input("Enter the first number :")
➔
➔	    if first.isnumeric() :
➔	        first = int(first)
➔	    else :
➔	        print("Invalid Input. Please try again.")
➔	        continue
➔
➔	    op = input("Enter the operator :")
➔
➔	    if op != "+" and op != "-" and op != "*" and op != "/" :
➔	        print("Invalid Input. Please try again.")
➔	        continue
➔
➔	    second = input("Enter the second number :")
➔
➔	    if second.isnumeric() :
➔	        second = int(second)
➔	    else :
➔	        print("Invalid Input. Please try again.")
➔	        continue
➔
➔	    if op == "+" :
➔	        print("Sum of two numbers is:",first+second)
➔
➔	    elif op == "-":
➔	        print("The difference between two numbers is",first-second)
➔
➔	    elif op == "*":
➔	        print("The product of two number is:",first*second)
➔
➔	    else :
➔	        print("On division:" , first/second)
➔
➔
➔	    flag = 1
➔	    print()
➔
➔	    while True :
➔
➔	        print("1 - Calculate Again")
➔	        print("0 - Exit")
➔
➔	        ch = int(input("Enter your choice :"))
➔
➔	        if ch == 1 :
➔	            break
➔
➔	        elif ch == 0 :
➔	            flag = 0
➔	            break
➔
➔	        else :
➔	            continue
➔
➔	    if flag == 1 :
➔	        continue
➔
➔	    else :
➔	        break
➔
➔	    print()
➔
➔	print("Thank you")
●	.
●	.
●
________________________________________
