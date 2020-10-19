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

#Defining a function to get the the value of languages
def get_data():
    print(Language.get())

Language = ttk.Combobox(root, value=("PHP", "JavaScript", "Python","C++","C#","Ruby","HTML", "CSS"), font=("Times New Roman", 13, "normal"), state="readonly")
Language.place(x=50, y=100, width=150, height=30)
Language.set("Select language")


#Which value should be use as default
#Language.current(0)

#Defining a button
btn = Button(root, text="Submit",font=("Times New Roman", 14, "normal"), bg="orange", fg="brown",command= get_data, padx=20, cursor="hand2", activebackground="lightgreen", activeforeground="green").place(x=200,y=250)

#Indicate to hold windows infinitely
root.mainloop()