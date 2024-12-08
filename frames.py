#Frames means a box  in which we can create or put things like button, label, entry etc...

from tkinter import *

r=Tk()
r.title("frame")
r.geometry("800x800")

f=Frame(r, width=100, height=100, bg="green")
f.pack(padx=30, pady=30)

#create button inside this frame, give f as button we create here
f1=Button(f, text="Click")
f1.pack()

r.mainloop()