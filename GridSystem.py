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

#Displaying Label using grid system
lbl = Label(root, text="Name : ", font=("Times New Roman", 16, "bold")).grid(row=0, column=0, pady=15)
lbl2 = Label(root, text="Email : ", font=("Times New Roman", 16, "bold")).grid(row=1, column=0, pady=15)
lbl3 = Label(root, text="Password : ", font=("Times New Roman", 16, "bold")).grid(row=2, column=0, pady=15)

lbl_res_1 = Label(root, text=" Enter your name ", font=("Times New Roman", 14, "normal"), bg="lightblue", fg="blue").grid(row=0, column=1, pady=15)
lbl_res_2 = Label(root, text=" Enter your Email ", font=("Times New Roman", 14, "normal"), bg="lightblue", fg="blue").grid(row=1, column=1, pady=15)
lbl_res_3 = Label(root, text=" Enter your Password ", font=("Times New Roman", 14, "normal"), bg="lightblue", fg="blue").grid(row=2, column=1, pady=15)

#text defines what label should be 
#font defines some font properties
#grid defines that windows should follow grid system
#pady defines the external padding in label
#bg defines background color
#fg defines background color

#Indicate End of windows and to hold windows infinitely
root.mainloop()