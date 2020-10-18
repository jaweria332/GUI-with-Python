#Import Tkinter, a library used for GUI in Python
from tkinter import *

#Declaring a root object
root=Tk()

#Define title of your window
root.title("Gets Started with Python GUI")

#Defining the windows size
root.geometry("800x500+300+80")

#Defining background color
root.config(bg="#262626")

#Declaring whether windows in resizable or not
root.resizable(False, False)

#-----------------SHOW DATA----------------------#
def show_data():
    var_data.set(str(txt_Text.get('1.0',END)))
    print(var_data.get())


var_data=StringVar()
#------------------------------TEXTAREA---------------------------#

txt_Text=Text(root, font=("Times New Roman", 14, "normal"), bg="white", fg="black")
txt_Text.place(x=180, y=200, height=80, width=200)

btn = Button(root, text="Submit",font=("Times New Roman", 14, "normal"), bg="orange", fg="brown", padx=20, cursor="hand2", activebackground="lightgreen", activeforeground="green", command=show_data()).place(x=200,y=300)
#We can't pass variable to text, we have to set a variable first

#Indicate End of windows and to hold windows infinitely
root.mainloop()