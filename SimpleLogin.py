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

#Entries are input fields

#Title
lbl_res_title = Label(root, text=" LOGIN FORM ", font=("Times New Roman", 20, "bold"), bg="orange", fg="brown", padx=20, pady=20).pack(fill=X)

#Label and entry for name
lbl_name = Label(root, text=" Enter your name ", font=("Times New Roman", 14, "normal"), bg="lightblue", fg="blue").place(x=20, y=100)
txt_name = Entry(root, font=("Times New Roman", 14, "normal"), bg="white", fg="black")
txt_name.place(x=180, y=100)

#Label and entry for email
lbl_email = Label(root, text=" Enter your email ", font=("Times New Roman", 14, "normal"), bg="lightblue", fg="blue").place(x=20, y=150)
txt_email = Entry(root, font=("Times New Roman", 14, "normal"), bg="white", fg="black")
txt_email.place(x=180, y=150)

#Label and entry for email
lbl_pass = Label(root, text=" Enter Password ", font=("Times New Roman", 14, "normal"), bg="lightblue", fg="blue").place(x=20, y=200)
txt_pass = Entry(root, font=("Times New Roman", 14, "normal"), bg="white", fg="black")
txt_pass.place(x=180, y=200)

#Defining button
btn = Button(root, text="Submit",font=("Times New Roman", 14, "normal"), bg="orange", fg="brown", padx=20, cursor="hand2", activebackground="lightgreen", activeforeground="green").place(x=200,y=250)

#Indicate End of windows and to hold windows infinitely
root.mainloop()