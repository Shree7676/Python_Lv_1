In-class exercise
●	Shubham is worried about his health. He keeps checking his height and weight daily. Recently he came to know about the BMI report, and now he wants to calculate his own BMI by writing a python program. Write a program in python to check your BMI by putting your height and weight as input.
●	Note:
●	Body Mass Index is a simple calculation using a person's height and weight. The formula is BMI = kg/m2 where kg is a person's weight in kilograms and m2 is their height in meters squared. A BMI of 25.0 or more is overweight, while the healthy range is 18.5 to 24.9. BMI applies to most adults 18-65 years.
●
●	Answer
➔	# Find the BMI report
➔
➔	height = int(input("Enter your height in cms :"))
➔	heightInMeters = height/100
➔
➔	weight = int(input("Enter your weight in kgs :"))
➔
➔	bmi = weight / heightInMeters ** 2
➔
➔	print("Your bmi is :" , bmi)
➔
➔	if(bmi<18.5):
➔	    print("Your are underweight")
➔	elif(bmi>24.9):
➔	    print("Your are overweight")
➔	else:
➔	    print("Your bmi is at healthy range")
●
●	.
●
●	________________________________________
●	.
●	A year consists of 365 days. But once every four years, it consists of 366 days. And that is known as a leap year. Shisha wants to know whether the current year is a leap year or not. She found that any year divisible by 4 is a leap year, if the year is divisible by 100 then it will not be a leap year, and if the year is divisible by 400 then it will be a leap year. Write a program in python to check whether the given year is a leap year or not to help Shisha.
●	Hint: Use if elif else condition
●
●	Answer
➔	# Python program to check if a year is a leap year or not
➔
➔	year = int(input("Enter a year: "))
➔
➔	if (year % 4) == 0:
➔	   if (year % 100) == 0:
➔	       if (year % 400) == 0:
➔	           print(year, "is a leap year")
➔	       else:
➔	           print(year, "is not a leap year")
➔	   else:
➔	       print(year, "is a leap year")
➔	else:
➔	   print(year, "is not a leap year")
●	.
●	.
●	.
________________________________________
●
●	Anu wants to fence the garden in front of her house, on three sides with lengths 20 m, 12 m, and 12 m. Find the cost of fencing at the rate of ` 150 per meter.
●
●	Answer
➔	# Find the cost of fencing the garden with three sides
➔
➔	first_side = int(input("Enter the lenght of first side :"))
➔	second_side = int(input("Enter the lenght of second side :"))
➔	third_side = int(input("Enter the length of third side :"))
➔
➔	total_length = first_side + second_side + third_side
➔
➔	ratePerMeter = 3
➔
➔	total_cost = ratePerMeter * total_length
➔
➔	print("The total cost for the fence is:", total_cost)
●	.
●	.
●	.
________________________________________
●
●	.
●	A farmer dug a flower bed of radius 7 m at the center of a field. He needs to purchase fertilizer. If 1 kg of fertilizer is required for 1 square meter area, how much fertilizer should he purchase? Write a python program to find the answer.
●
●	Answer
➔	# Find the amount of fertilizer required
➔
➔	radius = int(input("Enter the radius of flower bed :"))
➔	pi = 3.14
➔	area = pi * radius ** 2
➔
➔	# fertilizer ( in kg ) Per Meter Square
➔	fpms = 1
➔
➔	total_quanty = fpms * area
➔	total_quanty = round(total_quanty)
➔
➔	print(total_quanty,"kg of fertilizer is required")
●	.
