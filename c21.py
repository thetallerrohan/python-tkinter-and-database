from tkinter import *
screen=Tk()
screen.geometry("900x1100")
screen.title("chatbox")
screen.configure(bg="blue")

#checkbox and dropdown

#checkbox : it is used to create the checkbox out of which we can select multiple options. in checkbox we create one tkinter variable for every checkbutton
#tkinter vfariable will store the tey answer that if checkbox is selected or not. We have onvalue=1 and offvalue=0 which means if person selects a checkbox then variable will get 1. if person has not selected a checkbox then variable will gte 0.
#in checkbox case vraiable always stores either 1 or 0
var1=IntVar()
c1=Checkbutton(screen, text="C++", onvalue=1, offvalue=0, selectcolor="black", fg="red", padx=10, pady=10, variable=var1)
var2=IntVar()
c2=Checkbutton(screen,text="Python", onvalue=1, offvalue=0, selectcolor="green", fg="black", padx=10, pady=10, variable=var2)
c1.grid(row=0, column=0)
c2.grid(row=1, column=1)

def c():
    #so when person selects any language it should display a message that this language has been selected.
    #we will check if var1 and var2  have 1 or 0 and  display message according to that.
    if var1==1 and var2==0:
        print("Person has selected C++ and no python")
        l1=Label(screen, text="Person has selected C++ and no python")
        l1.grid(row=3, column=1)
    elif var1==1 and var2==1:
        print("Person has selected both C++ and python")
        l1=Label(screen, text="Person has selected both C++ and python")
        l1.grid(row=3, column=1)
    elif var1==0 and var2==1:
        print("Person has selected python and not C++")
        l1=Label(screen, text="Person has selected python and not C++")
        l1.grid(row=3, column=1)
    else:
        print("Person has not selected any language")
        l1=Label(screen, text="Person has not selected any language")
        l1.grid(row=3, column=1)
b1=Button(screen, text="Click me", command=c)
b1.grid(row=2, column=2)

#Dropwdown : its a dropsdown list where we select one thing or item from list. Here w ecreate one variable mbecause only value will be selected.

#We will create seperate list and put that list in optionmenu
#one tkinter variable

options=[
    "Burger",
    "Dosa",
    "Pizza",
    "Chicken",
    "sea food",
    "Cold drink"      
    ]
var=StringVar() # cox the value which we selected from list is string so value which will be stored is string  so StringVar() function is used to create variable
var.set("Chinese")
drop=OptionMenu(screen,var, *options) # give list name with * and variable name
drop.grid(row=3,column=1)

#we will create a button and whatever value is slected we get and display as label
def d():
    l2=Label(screen, text=var.get())
    l2.grid(row=5, column=0)
b2=Button(screen, text="Hello mr click this please", command=d)
b2.grid(row=4, column=0)
mainloop()