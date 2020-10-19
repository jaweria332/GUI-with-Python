#Import Tkinter, a library used for GUI in Python
from tkinter import *
from tkinter import messagebox

#Declaring a root object
root=Tk()

#Define title of your window
root.title("Gets Started with Python GUI")

#Defining the windows size
root.geometry("500x600+700+80")

#Defining background color
root.config(bg="#262626")

#Declaring whether windows in resizable or not
root.resizable(False, False)

#Defining function
def departdetail():
    messagebox.showinfo("Menu", "This message box is for MENU")

#Defining a menu
myMenu=Menu(root)
myMenu2=Menu(myMenu, tearoff=0)

menu2_detail=Menu(myMenu, tearoff=0)
menu2_detail.add_command(label="Cascade")
menu2_detail.add_command(label="Restrict")

#Label contain which type of label is menu
myMenu2.add_command(label="Add", command=departdetail)
myMenu2.add_cascade(label="Delete", menu=menu2_detail)
myMenu2.add_command(label="View", command=departdetail)
myMenu2.add_separator()
myMenu2.add_command(label="Display", command=departdetail)
myMenu2.add_command(label="Cascade", command=departdetail)

myMenu3=Menu(myMenu, tearoff=0)

#Label contain which type of label is menu
myMenu3.add_command(label="Add", command=departdetail)
myMenu3.add_command(label="Delete", command=departdetail)
myMenu3.add_command(label="View", command=departdetail)

#Cascading menus
myMenu.add_cascade(label="Departments", menu=myMenu2)
myMenu.add_cascade(label="Employees", menu=myMenu3)

root.config(menu=myMenu)

#Indicate to hold windows infinitely
root.mainloop()
