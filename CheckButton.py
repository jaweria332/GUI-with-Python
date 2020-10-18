#Import Tkinter, a library used for GUI in Python
from tkinter import *

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

#Defining a function
def get_value():
    print(check_var.get())

#Defining variable of int type
check_var=IntVar()

#Defining check button
check1=Checkbutton(root, text="Accept Lisence agreement", onvalue=1, offvalue=0,variable=check_var, font=("Times New Roman", 16, "bold"), bg="#262626", fg="white").place(x=150, y=150)
check_var.set(0)

#Defining button
btn = Button(root, text="Submit",font=("Times New Roman", 14, "normal"),command=get_value, bg="orange", fg="brown", padx=20, cursor="hand2", activebackground="lightgreen", activeforeground="green").place(x=200,y=250)

#Indicate End of windows and to hold windows infinitely  *.md; *.txt; *.rst; *.adoc; *.html
root.mainloop()