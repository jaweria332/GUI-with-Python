#Import Tkinter, a library used for GUI in Python
from tkinter import *

#Importing filedialog
from tkinter import filedialog

#Importing messagebox
from tkinter import messagebox

#Declaring a root object
root=Tk()

#Define title of your window
root.title("Gets Started with Python GUI")

#Defining the windows size
root.geometry("800x600+300+50")

#Defining background color
root.config(bg="#FFFFFF")


#Declaring whether windows in resizable or not
root.resizable(False, False)

#Defining a functions
#OPENFILE
def openFile():
    op=filedialog.askopenfile(title="Select File", filetypes=(("text file", ".txt"),))
    if op!=None:
        lbl_name.config(text="FileName : "+str(op.name.split("/")[-1]))
        var_filename.set(str(op.name))
        
        for i in op:
            txt_area.insert(END, str(i))
        op.close()

#SAVE AS
def saveAs():
    op=filedialog.asksaveasfile(title="Save As", filetypes=(("text file", ".txt")))
    if op!=None:
        lbl_name.config(text="Filename : ")
        var_filename.set(str(op.name))
        
        op.write(txt_area.get('1.0', END))
        op.close()
        messagebox.showinfo("Save As", "File has been saved")


#SAVE
def save_file():
    if var_filename.get()=="":
        saveAs()
    else:
        op=open(var_filename.get(), "w")
        op.write(txt_area.get('1.0', END))
        op.close()
        messagebox.showinfo("Save", "File has been saved")


#Defining buttons
btn1=Button(root, text="Open", command=openFile)
btn1.place(x=0, y=0, width=100)

btn2=Button(root, text="Save", command=save_file)
btn2.place(x=100, y=0, width=100)

btn3=Button(root, text="Save As", command=saveAs)
btn3.place(x=200, y=0, width=100)

var_filename=StringVar()

#Defining label for filename
lbl_name=Label(root, text="FileName", font=("times new roman", 16, "bold"))
lbl_name.place(x=50, y=50)

txt_area=Text(root, font=("times new roman", 14, "normal"), bd=2, relief=RIDGE)
txt_area.place(x=50, y=100, width=700, height=450)
#Indicate to hold windows infinitely
root.mainloop()