#Import Tkinter, a library used for GUI in Python
from tkinter import *

#Declaring a root object
root=Tk()

#Define title of your window
root.title("PACK AND PLACE SYSTEM FOR WIDGETS")

#Defining the windows size
root.geometry("500x600+700+80")

#Defining background color
root.config(bg="#262626")

#Declaring whether windows in resizable or not
root.resizable(False, False)


#------------Label with PACK SYSTEM-----------#
lbl_res_title = Label(root, text=" PACK SYSTEM ", font=("Times New Roman", 20, "bold"), bg="orange", fg="brown", padx=20, pady=20).pack(fill=X)
lbl_res_1 = Label(root, text=" Enter your name ", font=("Times New Roman", 14, "normal"), bg="lightblue", fg="blue").pack(padx=5, pady=5)
lbl_res_2 = Label(root, text=" Enter your Email ", font=("Times New Roman", 14, "normal"), bg="lightblue", fg="blue").pack(padx=5, pady=5)
lbl_res_3 = Label(root, text=" Enter your Password ", font=("Times New Roman", 14, "normal"), bg="lightblue", fg="blue").pack(padx=5, pady=5)
#By default pack system always align widgets in center


#------------Label with PLACE SYSTEM-------------#
lbl_res_title2 = Label(root, text=" PLACE SYSTEM ", font=("Times New Roman", 20, "bold"), bg="orange", fg="brown", padx=150, pady=20).place(x=0,y=200)
lbl_res_4 = Label(root, text=" Enter your name ", font=("Times New Roman", 14, "normal"), bg="lightblue", fg="blue").place(x=180,y=280)
lbl_res_5 = Label(root, text=" Enter your Email ", font=("Times New Roman", 14, "normal"), bg="lightblue", fg="blue").place(x=180,y=320)
lbl_res_6 = Label(root, text=" Enter your Password ", font=("Times New Roman", 14, "normal"), bg="lightblue", fg="blue").place(x=180,y=360)


#Indicate to hold windows infinitely
root.mainloop()
