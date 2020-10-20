#Import Tkinter, a library used for GUI in Python
from tkinter import *

#Importing module for file
from tkinter import filedialog

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

#Defining functions
def openFile():
    #To fetch folder
    #op=filedialog.askdirectory(title="Select Folder")
    
    #To Get name
    #op=filedialog.askopenfilename(title="Select Folder")

    #To fetch file
    #op=filedialog.askopenfile(title="Select File")
    
    #To select multiple file names
    #op=filedialog.askopenfiles(title="Select File")
    
    #To get multiple files
    #op=filedialog.askopenfilenames(title="Select File")

    #To ask to save files
    #op=filedialog.asksaveasfile(title="Select File")

    #To ask to save as file name
    op=filedialog.asksaveasfilename(title="Select File", filetype=(("text file", ".txt"), ("all files", '"."')))

    print(op)

#Defining button
btn=Button(root, text="Select File", command=openFile).place(x=50, y=100)

#Indicate to hold windows infinitely
root.mainloop()