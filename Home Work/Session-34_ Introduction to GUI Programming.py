
"""Homework questions
.Arvind recently created a program where he printed his name at the center. Now he wants to modify his program so that he gets his name at a random place each time when he runs the program. Write a program to print your name at a random position on the screen.
Hint: Use random module
:
# To display name in GUI window at a random place
"""
from tkinter import *
import random

root = Tk()
root.geometry("500x500")
root.title("Show Name")

x_position = random.randint(1,500)
y_position = random.randint(1,500)

name_lable = Label(text="Arvind")
name_lable.place(x = x_position , y = y_position)

root.mainloop()
