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

#Defining frame
myFrame1=Frame(root, bd=2, relief=RIDGE)
myFrame1.place(x=50,y=100)

#Scroll Bar
scroll1 = Scrollbar(myFrame1, orient=VERTICAL)
scroll1.pack(side=RIGHT, fill=Y)

#Defining list
mylist=Listbox(myFrame1, font=("Times New Roman", 15, "normal"), justify=CENTER, yscrollcommand=scroll1.set)
mylist.pack()
scroll1.config(command=mylist.yview)

#Inserting data in list
for i in range(0, 51):
    mylist.insert(i, "List Item : "+str(i))

#Indicate to hold windows infinitely
root.mainloop()
