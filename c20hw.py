from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
screen=Tk()
screen.geometry("900x1100")
screen.title("vertical slider")
screen.configure(bg="blue")
s=Scale(screen, from_=0, to=100, orient=VERTICAL)
s.grid(row=1, column=0)
def display():
    cat=Label(screen,text=("THE VALUE IS,",s.get()))
    cat.grid(row=1,column=1)
b3=Button(screen, text="Click here tp get no from slider", command=display)
b3.grid(row=3, column=1)
mainloop()