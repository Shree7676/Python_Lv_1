#Creating an authentication system that checks whether that user is allowed access or not. 
# Creating authentication system

database = open("database.txt", "a")
database.close()


# signUp System

def signUp():
    print()
    print("Enter following details to signUp")
    print()
    username = input("Enter username :")

    # Check if username is not blank
    if len(username) == 0:
        print("Username can not be blank")
        print("Please try again")
        return

    # Check if already exist
    database = open("database.txt", "r")

    for data in database:
        u, p = data.split(",")
        if username == u:
            print("Username already exist")
            print("Please try again")
            database.close()
            return

    database.close()

    password = input("Enter your password :")

    # Check if password contains less than 4 characters
    if len(password) < 4:
        print("Password should contain more than 4 characters")
        print("Please try again")
        return

    # One extra password input to confirm
    password_c = input("Enter your password again :")

    # Checking whether both the passwords are same or not
    if password != password_c:
        print("Entered password are not same. Please try again.")
        return

    # Putting username and password in the database

    database = open("database.txt", "a")

    record = username + "," + password + "\n"
    database.write(record)
    print()
    print("signUp successful")
    print()

    database.close()


# logIn system

def logIn():
    print()
    print("Enter following details to login")
    print()

    username = input("Enter username :")

    database = open("database.txt", "r")
    flag = 0
    for data in database:
        u, p = data.split(",")
        if username == u:
            flag = 1
            print(p)
            break

    database.close()

    if flag == 0:
        print()
        print("username do not exist")
        print("Please try again")
        print()
        return

    else:
        password = input("Enter the password :")
        if password + "\n" == p:
            print()
            print("---Login Successful---")
            print()
            quit()

        else:
            print()
            print("Incorrect password entered")
            print("Please try again")
            print()
            return


# Main Program

while True:
    print()
    print("---Welcome---")
    print()
    print("1 --> SignUp/Register")
    print("2 --> LogIn")
    print("0 --> Exit")
    print()
    ch = int(input("Enter your choice :"))
    if ch == 1:
        signUp()
    elif ch == 2:
        logIn()
    elif ch == 0:
        print("Thank You")
        break
    else:
        print("Invalid Input")
        print("Please try again")
        continue

# The End
