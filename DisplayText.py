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

#Definig  a function to get the text
def get_label_text():
    res_entry.config(text=str(txt_name.get())

#Title
lbl_res_title=Label(root, text="LETS DISPLAY USER TEXT", font=("Times New Roman", 20, "bold"), bg="orange", fg="brown", padx=20, pady=20).pack(fill=X)


#Label and entry for name
lbl_name = Label(root, text=" Enter text ", font=("Times New Roman", 14, "normal"), bg="lightblue", fg="blue").place(x=20, y=100)
txt_name = Entry(root, font=("Times New Roman", 14, "normal"), bg="white", fg="black")
txt_name.place(x=160, y=100)

#Defining button
btn = Button(root, text="Submit",font=("Times New Roman", 14, "normal"), bg="orange", fg="brown", padx=20, cursor="hand2", activebackground="lightgreen", activeforeground="green", command=get_label_text()).place(x=200,y=150)


#Header
lbl_res = Label(root, text="YOU ENTERED", font=("Times New Roman", 22, "bold"), bg="#262626", fg="white").place(x=140, y=250)
res_entry=Entry(root, font=("Times New Roman", 18, "normal"), bg="black", fg="white")
res_entry.place(x=140, y=300)


#Indicate End of windows and to hold windows infinitely
root.mainloop()