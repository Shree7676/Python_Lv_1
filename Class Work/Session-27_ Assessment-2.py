"""Assessment question
Build a Vehicle management system where the vehicles are allowed to park for a particular duration, while the vehicle is entering the user shall enter the vehicle number, duration of parking, entry time, and based on duration, the fees shall be displayed to the user. While making the exit, if the duration exceeds the actual duration ( exit time - entry time ) then extra fees may be claimed from the user.
Hint:
Use 24 hour format time for easier calculation.
Take the input of time in float format: for eg- for 9:30 am 9.30 and for 6:30 pm 18.30 can be used. In this way, it will be easier to calculate the actual duration.
Also, take duration only in multiple of half-hour in float format for easier calculation.
Create two function: entry() and exit()
Instead of using global and local variables try to use a list with tuple to store the values. { Note: You can access and edit the elements of a list in different functions.
"""
# Vehical Management System

records = [] # Initially record is empty
chargePerHour = 10
penaltyPerHour = 30


# Entry function

def entry():
    vehical_number = input("Enter vehical number :")
    duration = float(input("Enter duration in hrs :"))
    entry_time = float(input("Enter entry time :"))

    # Creating tuple of the information
    data = (vehical_number , duration , entry_time)

    records.append(data)

    # Generating receipt based on duration

    cost = duration * chargePerHour

    print()
    print("----------")
    print("Vechical Number :" , vehical_number)
    print("Entry time :" , entry_time)
    print("Given duration :" , duration)
    print("Cost :" , cost)
    print("----------")
    print()

# Exit Function

def exit():
    vehical_number = input("Enter vehical number :")
    exit_time = float(input("Enter exit time :"))

    flag = 0
    index = 0

    for data in records:
        if data[0] == vehical_number :
            flag = 1
            entry_time = data[2]
            actual_duration = exit_time - entry_time
            given_duration = data[1]
            if actual_duration > given_duration :
                extra_duration = actual_duration - given_duration
                extra_cost = extra_duration * penaltyPerHour
            else :
                extra_cost = 0

            records.pop(index)

        index += 1
    if flag == 0 :
        print("Vechicle do not exist in the database")

    else :
        print()
        print("----------")
        print("Vechical Number :" , vehical_number)
        print("Entry time :" , entry_time)
        print("Given duration :" , given_duration)
        print("Actual duration :" , actual_duration)
        print("Extra duration :" , extra_duration)
        print("Cost :" , given_duration*chargePerHour)
        print("Penalty :" , extra_cost)
        print("----------")
        print()

# Main Program

while True :
    print()
    print("Vechical Management System")
    print()
    print("1 --> Put entry")
    print("2 --> Put Exit")
    print("3 --> Show Records")
    print("0 --> EndProgram")
    print()
    ch = int(input("Enter your choice :"))
    if ch == 1 :
        entry()
    elif ch == 2 :
        exit()
    elif ch == 3 :
        print("Vehical No.,Duration,Entry Time")
        print("-------------------------------")
        for i in records :
            print(i)
    elif ch == 0 :
        print("Thank You")
        break
    else :
        print("Invalid Input")
        print("Try again")
        continue

# The end
