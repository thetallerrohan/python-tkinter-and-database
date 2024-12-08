from tkinter import *
from tkinter import messagebox
route = Tk()
route.title("message box screen")
route.geometry("800x800")
messagebox.showinfo("this is a toplevel1 window")
messagebox.showinfo("this is a toplevel2 window")
def nextscreen2():
    route3 = Tk()
    route3.title("message box screen 33")
    b3=Button(route3,text="hello world")
    b3.grid(row=1,column=1)
    l3=Label(route3,text="hellow world3")
    l3.grid(row=1, column=2)
def nextscreen():
    route2 = Tk()
    route2.title("message box screen 2")
    b2=Button(route2,text="click to interact", command=nextscreen2)
    b2.grid(row=1,column=1)
    l2=Label(route2,text="hellow world2")
    l2.grid(row=1, column=1)

l1=Label(route,text="hello world")
l1.grid(row=0,column=1)
b1=Button(route,text="click here to go to the next screen",command=next)
b1.grid(row=1,column=1)
mainloop()