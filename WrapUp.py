#Import Tkinter, a library used for GUI in Python
from tkinter import *

#Declaring a root object
root=Tk()

#Define title of your window
root.title("WRAP UP OF ALL BASIC CONCEPTS")

#Defining the windows size
root.geometry("500x450+700+80")

#Defining background color
root.config(bg="#FFFFFF")

#Declaring whether windows in resizable or not
root.resizable(False, False)


#Defining variables
var_name=StringVar()
var_email=StringVar()
var_gender=StringVar()
var_chk=IntVar()


#Defining functions
def get_data():
    if var_chk.get() == 1:
        result= "Name : " + var_name.get() + "\t" + "Gender : " + var_gender.get() + "\n" + "Email : " + var_email.get()
        lbl_result.config(text=str(result))

    else:
        lbl_result.config(text="Please Accept our terms and condition", fg="red")

#Making header
title = Label(root, text="User Entry Form", font=("Times New Roman", 22, "normal"),borderwidth=3, relief="sunken", bg="#FFFFFF", fg="red").pack(fill=X)


#Defining label and entry for UserName email 
name = Label(root, text="Username", font=("Times New Roman", 14, "normal"), bg="#FFFFFF", fg="black").place(x=80, y= 50)
email = Label(root, text="Email", font=("Times New Roman", 14, "normal"), bg="#FFFFFF", fg="black").place(x=80, y= 100)

name_entry = Entry(root,textvariable=var_name, font=("Times New Roman", 14, "normal"), bg="#FFFFFF", fg="black").place(x=180, y= 50)
email_entry = Entry(root, textvariable=var_email,font=("Times New Roman", 14, "normal"), bg="#FFFFFF", fg="black").place(x=180, y= 100)


#Defining Gender Radion Button

Gender = Label(root, text="Gender",font=("Times New Roman", 14, "normal"), bg="#FFFFFF", fg="black").place(x=80, y=150)

male=Radiobutton(root, text="Male",value="male",variable=var_gender,font=("Times New Roman", 14, "normal"),bg="#FFFFFF",fg="black",activebackground="#FFFFFF", activeforeground="black").place(x=150, y=150)
female=Radiobutton(root, text="Female",value="female",variable=var_gender,font=("Times New Roman", 14, "normal"),bg="#FFFFFF",fg="black",activebackground="#FFFFFF", activeforeground="black").place(x=230, y=150)
other=Radiobutton(root, text="Other",value="other",variable=var_gender,font=("Times New Roman", 14, "normal"),bg="#FFFFFF",fg="black",activebackground="#FFFFFF", activeforeground="black").place(x=310, y=150)
var_gender.set("male")


#CheckBox
check_condition = Checkbutton(root, text="Agree terms and conditions",onvalue=1, offvalue=0, variable=var_chk,font=("Times New Roman", 14, "normal"),bg="#FFFFFF",fg="black",activebackground="#FFFFFF", activeforeground="black").place(x= 100, y= 200)


#Defining Button
btn = Button(root, text="SHOW",font=("Times New Roman", 14, "normal"),command=get_data, bg="orange", fg="brown", padx=20, cursor="hand2", activebackground="lightgreen", activeforeground="green").place(x=200,y=250)


#Label for header
header_result = Label(root, text="Your entered information", font=("Times New Roman", 18, "normal"), bg="#FFFFFF", fg="green").place(x=100, y=300)

#Defining label for data display
lbl_result=Label(root, text="", font=("Times New Roman", 14, "normal"), bg="#FFFFFF", fg="black")
lbl_result.place(x=5 , y=350, relwidth=1)

#Indicate End of windows and to hold windows infinitely
root.mainloop()
