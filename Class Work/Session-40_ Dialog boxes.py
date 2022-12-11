

"""
{GUI mini-project-1} Shubham still wants some improvement in his GUI program. Sometimes he saves the incorrect data and then it becomes difficult for him to delete that. So he needs a confirmation question before he saves the data. Also, after saving the record in the text file, he wants a message box on the screen that can either show data saved successfully or it was not successful. Write the program for the same.
Hint: Use messagebox: showinfo() , askquestion()
"""
"""
Nidhi wants to create a notepad application. Write a program in python and the Tkinter module to create a GUI notepad application.
Hint:
Use TextArea widget.
Use MenuBar to show different options like save and
"""

from tkinter import *
from tkinter.messagebox import showinfo

# required functions

def newFile():
    pass

def openFile():
    pass

def saveFile():
    pass

def quitApp():
    pass

def cut():
    pass

def copy():
    pass

def paste():
    pass

def about():
    pass


root = Tk()
root.title("Untitled - Notepad")
root.geometry("644x788")

TextArea = Text(root, font="lucida 13")
file = None
TextArea.pack(expand=True, fill=BOTH)

MenuBar = Menu(root)

FileMenu = Menu(MenuBar, tearoff=0)

FileMenu.add_command(label="New", command=newFile)


FileMenu.add_command(label="Open", command = openFile)

FileMenu.add_command(label = "Save", command = saveFile)
FileMenu.add_separator()
FileMenu.add_command(label = "Exit", command = quitApp)
MenuBar.add_cascade(label = "File", menu=FileMenu)

EditMenu = Menu(MenuBar, tearoff=0)

EditMenu.add_command(label = "Cut", command=cut)
EditMenu.add_command(label = "Copy", command=copy)
EditMenu.add_command(label = "Paste", command=paste)

MenuBar.add_cascade(label="Edit", menu = EditMenu)

HelpMenu = Menu(MenuBar, tearoff=0)
HelpMenu.add_command(label = "About Notepad", command=about)
MenuBar.add_cascade(label="Help", menu=HelpMenu)

root.config(menu=MenuBar)

Scroll = Scrollbar(TextArea)
Scroll.pack(side=RIGHT,  fill=Y)
Scroll.config(command=TextArea.yview)
TextArea.config(yscrollcommand=Scroll.set)

root.mainloop()

