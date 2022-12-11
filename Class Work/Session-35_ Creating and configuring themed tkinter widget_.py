
"""
Nidhi's younger sister requested to decorate the same GUI application of the multiplication table.
So write a python program to design the GUI application in this manner.
Hint: Use properties like : bg, fg, padx, pady, relief, root.config() etc

# To display multiplication table of a number
"""
from tkinter import *

root = Tk()
root.geometry("700x500")
root.title("Multiplication Table")
root.config(bg="yellow" , relief=SUNKEN , borderwidth=4)

for i in range(1, 11):
    for j in range(1,11):
        label = Label(text=f"{i} x {j} = {i*j}" , bg="blue" , fg="white", relief=RAISED , borderwidth=2)
        label.grid(row = j , column=i , pady=12 , padx=3)

root.mainloop()

"""
Arvind got to know that he can put images in a GUI application created in python. 
Now he is very interested to create the model of his school id card using the Tkinter module. 
Create the GUI program as given below :
"""
# Creating id card using tkinter

from tkinter import *

root = Tk()
root.geometry("500x500")
root.title("Id Card")

photo = PhotoImage(file="mid.png")

img_label = Label(image=photo)
img_label.pack()

Label(text="Name : Arvind" , font=("Arial" , 30), fg="blue").pack()
Label(text="Grade: IX" , font=("Arial" , 30), fg="blue").pack()
Label(text="Adm. : 32400" , font=("Arial" , 30), fg="blue").pack()
Label(text="Blood: B+" , font=("Arial" , 30), fg="blue").pack()

root.mainloop()

