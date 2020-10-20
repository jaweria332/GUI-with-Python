#Import Tkinter, a library used for GUI in Python
from tkinter import *

#To read jpg file you need to import pillow
from PIL import ImageTk

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

#Importing image
my_img=ImageTk.PhotoImage(file="E:\\Python GUI\\GUI-with-Python\\Images\\cloud1.jpg")

#Defining label for images 
lbl_img=Label(root, text="Cloud", image=my_img,compund=LEFT, font=("times new roman", 20, "bold"))
lbl_img.place(x=50, y=100)

#To set image as a background
#lbl_img=Label(root, image=my_img).place(x=0, y=0)
#Indicate to hold windows infinitely
root.mainloop()
