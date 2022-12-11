"""
Shivam just started freelancing. He is Indian but his clients are from the US and pay him in dollars.
Each time he needs to calculate the amount in rupees manually. To make his work easy write a program
that can convert dollars into rupees easily. The program should take the input in dollars and should print equivalent rupees.
Hint: 1 United States Dollar equals 74.31 Indian Rupee
"""

print(int(input("Enter Dollars"))*74.31)


"""
Kapil invests money in the stock market. Sometimes he wants to calculate the profit he will make on 
selling the shares at a particular price before he actually sells the shares. To help Kapil write a program 
in python that can take the buying price with the number of shares and selling price with the number of shares as 
input and can show the profit that he will make.
"""
num=int(input("Number of shares= "))
buy=int(input("Buying price= "))
sell=int(input("selling price= "))
print("balance= ",(sell-buy)*num)