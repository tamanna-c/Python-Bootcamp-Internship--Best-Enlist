#importing library
from tkinter import *
from tkinter import ttk

window = Tk()
#Declaring Window Title
window.title("Registration Form")
#Declaring Window size
window.geometry('600x600')
#Declaring Window Color
window.configure(background = "#17202A")
label_0= Label(window,text=" Student Registration form",width=20,font = ("bold",30))
label_0.grid(row =0,column = 4)
#below four fields are declared
Firstname = Label(window ,text = "First Name",font = ("Arial",12), bg = "#17202A", fg = "white").grid(row = 2,column = 0)
LastName = Label(window ,text = "Last Name",font = ("Arial",12), bg = "#17202A", fg = "white").grid(row = 3,column = 0)
Email = Label(window ,text = "Email Id",font = ("Arial",12), bg = "#17202A", fg = "white").grid(row = 4,column = 0)
Mobile = Label(window ,text = "Contact Number",font = ("Arial",12), bg = "#17202A", fg = "white").grid(row = 5,column = 0)
pan = Label(window ,text = "Pan Number",font = ("Arial",12), bg = "#17202A", fg = "white").grid(row = 7,column = 0)
adhaar = Label(window ,text = "Adhaar Number",font = ("Arial",12), bg = "#17202A", fg = "white").grid(row = 8,column = 0)
college = Label(window ,text = "College name",font = ("Arial",12), bg = "#17202A", fg = "white").grid(row = 10,column = 0)
school = Label(window ,text = "School name",font = ("Arial",12), bg = "#17202A", fg = "white").grid(row = 11,column = 0)
roll = Label(window ,text = "Roll number",font = ("Arial",12), bg = "#17202A", fg = "white").grid(row = 13,column = 0)
age = Label(window ,text = "Age",font = ("Arial",12), bg = "#17202A", fg = "white").grid(row = 14,column = 0)


Firstname1 = Entry(window,width=30).grid(row = 2,column = 1)
Lastname1 = Entry(window,width=30).grid(row = 3,column = 1)
Email1 = Entry(window,width=30).grid(row = 4,column = 1)
Mobile1 = Entry(window,width=30).grid(row = 5,column = 1)
pan1 = Entry(window,width=30).grid(row = 7,column = 1)
adhaar1 = Entry(window,width=30).grid(row = 8,column = 1)
college1 = Entry(window,width=30).grid(row = 10,column = 1)
school1 = Entry(window,width=30).grid(row = 11,column = 1)
roll1 = Entry(window,width=30).grid(row = 13,column = 1)
age1 = Entry(window,width=30).grid(row = 14,column = 1)


var1=IntVar()
Checkbutton(window,text= "accept terms and condition", variable=var1).place(x=70,y=300)
#function declaration
def clicked():
        res = "Welcome to " + txt.get()
        lbl.configure(text= res)
btn = ttk.Button(window ,text="Submit").place(x = 70,y=350)
window.mainloop()
