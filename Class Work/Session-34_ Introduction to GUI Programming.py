"""
Arvind learned how to create GUI applications using python for the first time.
He wants to show his name in the program at the center of the screen.
Write a program to display the name Arvind at the center of the root window. Display your name as well.
Hint: use .place()
"""
# To display name in GUI window

from tkinter import *

root = Tk()
root.geometry("500x500")
root.title("Show Name")

name_lable = Label(text="Arvind")
name_lable.place(x = 250 , y = 250)

root.mainloop()

"""
Nidhi wants to create a GUI program using the python Tkinter module. 
She wants to display the multiplication table of any number on the screen 
and then show her program to her younger sister. Write the same program as 
Nidhi and show it to your friends.
Hint: Use .pack() and for loop
"""


# To display multiplication table of a number

from tkinter import *

root = Tk()
root.geometry("500x500")
root.title("Multiplication Table")

number = 7

for i in range(1, 11):
    label = Label(text=f"{number} x {i} = {number*i}")
    label.pack()

root.mainloop()

"""
Nidhi's younger sister requested her to create a program that can display the multiplication table of all the numbers from 1 to 10 at the same time. Nidhi got stuck and she is not able to create such type of program. Write a python program to help Nidhi.

Hint: Use .grid() and nested for loop.
# To display multiplication table of a number
"""
from tkinter import *

root = Tk()
root.geometry("700x500")
root.title("Multiplication Table")

for i in range(1, 11):
    for j in range(1,11):
        label = Label(text=f"{i} x {j} = {i*j}")
        label.grid(row = j , column=i)

root.mainloop()

