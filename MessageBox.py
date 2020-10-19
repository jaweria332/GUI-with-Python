#Import Tkinter, a library used for GUI in Python
from tkinter import *

#Importing messagebox from tkinter
from tkinter import messagebox


#Declaring a root object
root=Tk()

#Define title of your window
root.title("Message Box for user")

#Defining the windows size
root.geometry("500x600+700+80")

#Defining background color
root.config(bg="#262626")

#Declaring whether windows in resizable or not
root.resizable(False, False)

#Defining a function
def message1():
    messagebox.showerror("Show Error", "This message is to show error!")

def message2():
    messagebox.showwarning("Show Warning", "This message is to show warning!")

def message3():
    messagebox.showinfo("Show Info", "This message is to show Information!")

def message4():
    messagebox.showinfo("Enjoy!", "Have a good time with GUI using tkinter")


#Defining button
btn1=Button(root, text="Hey", command=message1).place(x=50, y=50, height=40, width=100)
btn2=Button(root, text="Hello", command=message2).place(x=200, y=50, height=40, width=100)
btn3=Button(root, text="Howdy", command=message3).place(x=50, y=200, height=40, width=100)
btn4=Button(root, text="High", command=message4).place(x=200, y=200, height=40, width=100)


#Indicate to hold windows infinitely
root.mainloop()
