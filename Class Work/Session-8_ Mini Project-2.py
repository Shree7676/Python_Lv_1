In-class exercise
●	Yash and Vishal have invested 10000$ in their bank. Yash is getting 6% simple interest from his bank and Vishal is getting 6% compound interest from his bank. Write a python program to calculate the difference in their returns after 30 years. What is the difference in their return in one year? What is the reason for this difference? Discuss.
●	Hint: Use the following parameters to calculate interest
●	Principal amount
●	Time
●	Rate of interest
●	Answer
➔	# Calculating the simple and compound interest
➔
➔	p = int(input("Enter the principal amount :"))
➔	r = int(input("Enter the rate of interest in % :"))
➔	t = int(input("Enter the time of investment in yrs :"))
➔	print()
➔	print("1 - Simple interest")
➔	print("2 - Compound interest")
➔	print()
➔	ch = int(input("Enter your choice :"))
➔	print()
➔	if ch == 1 :
➔	    si = p*r/100*t
➔	    print("Your return :" , si)
➔
➔	elif ch == 2 :
➔	    ci = p*(1+r/100)**t - p
➔	    print("Your return :" , ci)
➔
➔	else :
➔	    print("Invalid input")
➔
●
________________________________________
●
●	Nidhi's father is not able to calculate his annual tax correctly. He is a bit confused with the taxation rule also each year his total annual income is different. So to help her father Nidhi decides to write a python program that can calculate the tax to be paid based on annual income. Write the same program to calculate the tax to be paid based on annual income.
●	Hint: take the annual income as input from the user and print the amount of tax to be paid. These are tax rules.
●
●	Answer
➔	# Income tax calculator
➔
➔	annual_income = int(input("Enter your annual income :"))
➔	tax = 0
➔
➔	if annual_income < 250000 :
➔	    tax = 0
➔
➔	elif annual_income < 500000:
➔	    tax = annual_income * 5/100
➔
➔	elif annual_income < 750000 :
➔	    tax = annual_income * 10/100
➔
➔	elif annual_income < 1000000 :
➔	    tax = annual_income * 15/100
➔
➔	elif annual_income < 1250000 :
➔	    tax = annual_income * 20/100
➔
➔	elif annual_income < 1500000 :
➔	    tax = annual_income * 25/100
➔
➔	else :
➔	    tax = annual_income * 30/100
➔
➔	print("Tax to be paid :" , tax)
●	.
●	.
●
________________________________________
●	Vishnu is in third grade. He is curious to know how exactly any website verify whether given username and password is correct or not. To explain the same thing to Vishnu create a basic signup and login system.
●	Hint: Store the username and password inside variables signup and then use same variables for verification during login process.
●	Sample run:
●	>> Create your account ( Signup )
●	>> Enter username : Nidhi
●	>> Enter password : 1234
●	>> Confirm password : 1234
●	>> Your account is created : D
●	>> Login Here
●	>> Enter username: Nidhi
●	>> Enter password : 1234
●	>> Login Successful : D
●	Note:
●	If confirm password is not correct while signup then print: password not matching
●	If the username is not correct while login then print: Username not found
●	If the password is not correct while login then print: Incorrect password. Login failed
●	After any incorrect information stop the program using quit() function.
