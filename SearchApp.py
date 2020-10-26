#Import libraries

import wikipedia
from tkinter import *
from tkinter import messagebox

#Defining class for search app
class SearchApp:
    def __init__ (self, root):
        self.root=root
        self.root.title("Search App | Developed by Jaweria | Tkinter")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#262626")

        #Defining top title
        lbl_title=Label(self.root, text="GOOGLE ULTRA LITE", font=("times new roman", 40, "bold"), bg="white", fg="#262626")
        lbl_title.place(x=0, y=0, relwidth=1)

        #Label for search
        sear_lbl=Label(self.root, text="Type Here",font=("times new roman", 16, "bold"), bg="#262626", fg="white")
        sear_lbl.place(x=10, y=100, width=200)

        #defining variable
        self.var_search=StringVar()

        #Defining Entry for search
        entry_search=Entry(self.root, textvariable=self.var_search, font=("courier new", 16, "normal"), bg="white", fg="black")
        entry_search.place(x=250, y=100, width=400)

        #Defining search button
        search_btn=Button(self.root, text="Search", command=self.search_text, font=("courier new", 14, "normal"), bg="orange", fg="brown", activebackground="lightgreen", activeforeground="green")
        search_btn.place(x=680, y=100, width=100)

        #Defining Reset button
        search_btn=Button(self.root, text="Reset", font=("courier new", 14, "normal"),command=self.clear_text, bg="orange", fg="brown", activebackground="lightgreen", activeforeground="green")
        search_btn.place(x=800, y=100,width=100)

        #Defining Enable button
        search_btn=Button(self.root, text="Enable", font=("courier new", 14, "normal"),command=self.enable, bg="orange", fg="brown", activebackground="lightgreen", activeforeground="green")
        search_btn.place(x=920, y=100,width=100)

        #Defining Disable button
        search_btn=Button(self.root, text="Disable", font=("courier new", 14, "normal"),command=self.disable, bg="orange", fg="brown", activebackground="lightgreen", activeforeground="green")
        search_btn.place(x=1040, y=100,width=100)

        #Defining label to mention mode
        self.lbl_mode=Label(self.root, text="APP MODE : ", font=("times new roman", 16, "bold"), bg="#262626", fg="yellow")
        self.lbl_mode.place(x=80,y=150)
        
        #Defining frame for search result
        frame1=Frame(self.root, bd=2, relief=RIDGE)
        frame1.place(x=80, y=180, width=1100, height=500)

        #Defining scrollbar for search window
        scroll1=Scrollbar(frame1, orient=VERTICAL)
        scroll1.pack(side=RIGHT, fill=Y)

        #Defining textarea for search frame
        self.txt_frame=Text(frame1, font=("times new roman", 14, "normal"), yscrollcommand=scroll1)
        self.txt_frame.pack(fill=BOTH, expand=1)

        scroll1.config(command=self.txt_frame.yview)
    
    #Defining function for clear
    def clear_text(self):
        self.var_search.set("")
        self.txt_frame.delete('1.0', END)
        self.lbl_mode.config(text="")

    #Defining function for enable
    def enable(self):
        self.txt_frame.config(state=NORMAL)
        self.lbl_mode.config(text="APP MODE : ENABLED")

    #Defining function for disable
    def disable(self):
        self.txt_frame.config(state=DISABLED)
        self.lbl_mode.config(text="APP MODE : DISABLED")

    #Defining function for search
    def search_text(self):
        if self.var_search.get()=="":
            messagebox.showerror("Error", "Search area is empty!")

        else:
            fetch_data=wikipedia.summary(self.var_search.get())
            self.txt_frame.insert('1.0', fetch_data)

root=Tk()
obj=SearchApp(root)
#Indicate to hold windows infinitely
root.mainloop()
