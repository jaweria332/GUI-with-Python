#Import Tkinter, a library used for GUI in Python
from tkinter import *

#Declaring a root object
root=Tk()

#Define title of your window
root.title("WINDOWS FRAMES")

#Defining the windows size
root.geometry("500x600+700+80")

#Defining background color
root.config(bg="#262626")

#Declaring whether windows in resizable or not
root.resizable(False, False)

#Defining frame without label
windows1 = Frame(root, bg="white")
windows1.place(x=10, y=50, height=400, width=200)

#Definig frame with label
window2= LabelFrame(root,bg="white",text="student info")
window2.place(x=220, y=50)

#Defining button in windows2
btn = Button(windows1, text="Show")
btn.place(x=50, y=200)
#Indicate to hold windows infinitely
root.mainloop()
