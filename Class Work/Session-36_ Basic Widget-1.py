"""
Sahil had created a dice GUI program where it was showing different sides of the dice each
time he use to run the program. But now he wants to make it better by adding a button.
Create a python GUI program that shows random numbers each time you run the program.
Try to create the GUI given below.
"""

# Creating id card using tkinter

from tkinter import *
import random
from tkinter import font

root = Tk()
root.geometry("500x500")
root.title("Dice")
root.config(bg="yellow")


def rollDice():
    dice = 1 , 2 , 3 , 4 , 5 , 6
    roll = random.choice(dice)
    Label(text=roll , font=("Arial" , 250), fg="brown" , bg="cyan" , relief=SUNKEN , borderwidth=20).place(x=150 , y=20)

roll_button = Button(text="Roll" , font=("Arial Narrow" , 30), fg="brown" , bg="lightblue" , command=rollDice)
roll_button.place(x = 20 , y = 20)


root.mainloop()
"""
Ayman wants to create a college admission form and wants to know the preferred subjects of his friends. 
For this, he wants to create a GUI program in python where he wants to take the input using the entry widget.
Also after taking all the inputs he wants to store the data in a text file. 
But he is not able to work on this program perfectly. So write a python program to help him with this.

"""
# To display name in GUI window

from tkinter import *

root = Tk()
root.geometry("500x500")
root.title("College admission form")

# function to save the data in text file.

def save():
    file = open("records.txt" , "a+")
    record = name.get()+","+age.get()+","+grade.get()+","+course.get()+"\n"
    file.write(record)
    file.close()
    name.set("")
    age.set("")
    grade.set("")
    course.set("")

# creating text variables for the entry widget

name = StringVar()
age = StringVar()
grade = StringVar()
course = StringVar()


name_lable = Label(text="Name : " , font="Arial 15")
name_lable.grid(row=1 , column=0)

name_entry = Entry(root,font="Arial 15" , textvariable=name)
name_entry.grid(row=1 , column=1)

age_lable = Label(text="Age : " , font="Arial 15")
age_lable.grid(row=2 , column=0)

age_entry = Entry(root,font="Arial 15" , textvariable=age)
age_entry.grid(row=2 , column=1)

grade_lable = Label(text="Grades : " , font="Arial 15")
grade_lable.grid(row=3 , column=0)

grade_entry = Entry(root,font="Arial 15" , textvariable=grade)
grade_entry.grid(row=3 , column=1)

course_lable = Label(text="Course : " , font="Arial 15")
course_lable.grid(row=4 , column=0)

course_entry = Entry(root,font="Arial 15" , textvariable=course)
course_entry.grid(row=4 , column=1)

submit_button = Button(text="Submit" , font="Arial 15", width=20, bg="grey" , fg="brown" , command=save)
submit_button.grid(row=5 , column=1)

root.mainloop()
