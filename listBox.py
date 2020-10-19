#Import Tkinter, a library used for GUI in Python
from tkinter import *
#Combobox is a widget of ttk module of tkinter
from tkinter import ttk

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

#Defining function
def get_depart():
    get_crsr=Depart.curselection()
    
    #For bydefault select mode of list ie, BROWSE
    #print(get_crsr, Depart.get(get_crsr))

    #For MULTIPLE selectmode of list
    for i in get_crsr:
        print(Depart.get(i))

#Defining an object of listbox
Depart = Listbox(root, justify=CENTER, selectmode= EXTENDED)
Depart.place(x=100, y=50, width=150, height=150)

#Loop for values 
for i in range(1, 21):
    Depart.insert(i, "Department" + str(i) )

#Defining a button
btn = Button(root,command=get_depart, text="Submit",font=("Times New Roman", 14, "normal"), bg="orange", fg="brown", padx=20, cursor="hand2", activebackground="lightgreen", activeforeground="green").place(x=200,y=250)


#Function for deletion
def delete_data():
    get_crsr_delete=myList.curselection()
    myList.delete(get_crsr_delete)


#LETS SEE HOW CAN WE IMPLEMENT DELETE OPERATION ON LIST
myList = Listbox(root, justify=CENTER)
myList.place(x= 100, y=300,  width=150, height=150)
for i in range(1,11):
    myList.insert(i, "List" + str(i))

#Defining a button
btn_delete = Button(root, command=delete_data,text="Delete",font=("Times New Roman", 14, "normal"), bg="pink", fg="red", padx=20, cursor="hand2", activebackground="orange", activeforeground="brown").place(x=200,y=480)

#Indicate to hold windows infinitely
root.mainloop()