
"""
Homework questions

Sahil wants to create a program where he wants to display different sides of the dice each time he runs the program.
He used images for this purpose. Write the same program to create virtual dice with GUI programming.
"""
# Creating id card using tkinter

from tkinter import *
import random

root = Tk()
root.geometry("500x500")
root.title("Dice")

photoOne = PhotoImage(file="diceOne.png")
photoTwo = PhotoImage(file="diceTwo.png")
photoThree = PhotoImage(file="diceThree.png")
photoFour = PhotoImage(file="diceFour.png")
photoFive = PhotoImage(file="diceFive.png")
photoSix = PhotoImage(file="diceSix.png")

dice = (photoOne , photoTwo , photoThree, photoFour , photoFive , photoSix)

roll = random.choice(dice)

roll_label= Label(image=roll)
roll_label.pack()

root.mainloop()
