#Import Tkinter, a library used for GUI in Python
from tkinter import *
#Combobox is a widget of ttk module of tkinter
from tkinter import ttk

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


#Defining the function to bring value on to the scale
def get_price(price_):
    lbl_result.config(text=str(price.get()))

#Defining scale
price=Scale(root, from_=10, to=100,sliderlength=60, orient=HORIZONTAL, showvalue=FALSE, command=get_price)

#Placing scale
price.place(x=150, y=100, width=200)

#Defining label for scale
lbl_result=Label(root, bg="#262626", fg="white")

#Placing label
lbl_result.place(x=0, y=150, relwidth=1)


#Indicate to hold windows infinitely
root.mainloop()