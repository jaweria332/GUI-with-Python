#Import Tkinter, a library used for GUI in Python
from tkinter import *

#Declaring a root object
root=Tk()

#Define title of your window
root.title("Gets Started with Python GUI")

#Defining the windows size
root.geometry("500x350+700+80")

#Defining background color
root.config(bg="#FFFFFF")

#Declaring whether windows in resizable or not
root.resizable(False, False)


#Making header
title = Label(root, text="User Entry Form", font=("Times New Roman", 22, "normal"),borderwidth=3, relief="sunken", bg="#FFFFFF", fg="red").pack(fill=X)


#Defining label and entry for UserName email 
name = Label(root, text="Username", font=("Times New Roman", 14, "normal"), bg="#FFFFFF", fg="black").place(x=80, y= 50)
email = Label(root, text="Email", font=("Times New Roman", 14, "normal"), bg="#FFFFFF", fg="black").place(x=80, y= 100)

name_entry = Entry(root, font=("Times New Roman", 14, "normal"), bg="#FFFFFF", fg="black").place(x=180, y= 50)
email_entry = Entry(root, font=("Times New Roman", 14, "normal"), bg="#FFFFFF", fg="black").place(x=180, y= 100)


#Defining Gender Radion Button
gender=StringVar()

Gender = Label(root, text="Gender",font=("Times New Roman", 14, "normal"), bg="#FFFFFF", fg="black").place(x=80, y=150)

male=Radiobutton(root, text="Male",value="male",variable=gender,font=("Times New Roman", 14, "normal"),bg="#FFFFFF",fg="black",activebackground="#FFFFFF", activeforeground="black").place(x=150, y=150)
female=Radiobutton(root, text="Female",value="female",variable=gender,font=("Times New Roman", 14, "normal"),bg="#FFFFFF",fg="black",activebackground="#FFFFFF", activeforeground="black").place(x=230, y=150)
other=Radiobutton(root, text="Other",value="other",variable=gender,font=("Times New Roman", 14, "normal"),bg="#FFFFFF",fg="black",activebackground="#FFFFFF", activeforeground="black").place(x=310, y=150)
gender.set("male")


#CheckBox
check_condition = Checkbutton(root, text="Agree terms and conditions", variable=gender,font=("Times New Roman", 14, "normal"),bg="#FFFFFF",fg="black",activebackground="#FFFFFF", activeforeground="black").place(x= 100, y= 200)


#Defining Buttons
btn = Button(root, text="Submit",font=("Times New Roman", 14, "normal"), bg="orange", fg="brown", padx=20, cursor="hand2", activebackground="lightgreen", activeforeground="green").place(x=200,y=250)


#Indicate End of windows and to hold windows infinitely
root.mainloop()