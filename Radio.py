#Import Tkinter, a library used for GUI in Python
from tkinter import *

#Declaring a root object
root=Tk()

#Define title of your window
root.title("RADIO BUTTONS")

#Defining the windows size
root.geometry("500x600+700+80")

#Defining background color
root.config(bg="#262626")

#Declaring whether windows in resizable or not
root.resizable(False, False)

#Defining a function
def get_gender():
    print(gender.get())
#Defining a string variable
gender=StringVar()

#Defining label for Radio Button
Gender=Label(root, text="Select Gender : ", font=("Times New Roman", 16, "bold"), bg="#262626",fg="white").place(x=50, y=100)

#Defining button for male, female and other
male=Radiobutton(root, text="Male",value="male",variable=gender,font=("Times New Roman", 16, "bold"),bg="#262626",fg="white",activebackground="#262626", activeforeground="white").place(x=50, y=200)
female=Radiobutton(root, text="Female",value="female",variable=gender,font=("Times New Roman", 16, "bold"),bg="#262626",fg="white",activebackground="#262626", activeforeground="white").place(x=150, y=200)
other=Radiobutton(root, text="Other",value="other",variable=gender,font=("Times New Roman", 16, "bold"),bg="#262626",fg="white",activebackground="#262626", activeforeground="white").place(x=250, y=200)
gender.set("male")

#Defining button
btn = Button(root, text="Submit",font=("Times New Roman", 14, "normal"), bg="orange", fg="brown", padx=20, cursor="hand2", activebackground="lightgreen", activeforeground="green", command=get_gender).place(x=200,y=300)

#Indicate End of windows and to hold windows infinitely
root.mainloop()
