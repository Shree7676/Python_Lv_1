"""
Himanshi wants to know how the code editor which she uses has different sections in the same GUI window.
Like an explorer, files, terminal, output window, etc. Use frames and create a basic structure of vs code
or pycharm to show Himanshi how these basic sections are divided.
Create the following GUI application.
"""
from tkinter import *

root = Tk()
root.geometry("500x500")
root.title("vs code")

frame1 = Frame(root , bg="brown" , relief=SUNKEN , borderwidth=10 )
frame1.pack(fill=Y , side=LEFT)

explorer_label = Label(frame1 , bg="brown" , fg="white" , text="EXPLORER    ...")
explorer_label.pack()


frame2 = Frame(root , bg="brown" , relief=SUNKEN , borderwidth=10)
frame2.pack(fill=X)

file_name = Label(frame2 , bg="red" , fg="white" , text="vscode.py")
file_name.pack(side=LEFT)

main = Label(frame2 , bg="maroon" , fg="white" , text="main.py" )
main.pack(side=LEFT)

frame3 = Frame(root , bg="maroon" , borderwidth=6)
frame3.pack(fill=X)

file_name = Label(frame3 , bg="maroon" , fg="white" , text="vscode.py  > ...")
file_name.pack(side=LEFT)

frame4 = Frame(root , bg="maroon" , borderwidth=6)
frame4.pack(fill=Y , side=RIGHT)


file_name = Label(frame4 , bg="maroon" , fg="white" , text="TERMINAL")
file_name.pack()

root.mainloop()


