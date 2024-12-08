#--------------------------------file Handling---------------------------------------------------
#File Hanlding means means we download and upload a file. the file can be be text file. python file, image file, html file =.. any file. 
 
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
screen=Tk()
screen.geometry("900x1100")
screen.title("File Hanlding & Scale")
screen.configure(bg="green")

 #create two button download and upload. when we click on the buttons it should download and upload
def download():
    #all coding of download here
    #Step to download file
    #1. fildialog is imported at the top.
    #2. we use function called as asksaveasfile and inside taht we mention all files names which we can save.
    file=filedialog.asksaveasfile(filetypes=(("Python File", ".py"), ("Image File", ".png"), ("Image File", ".jpg"), ("HTML File", ".html"), ("Text File", ".txt")))
    

def upload():
    #all coding of upload here
    #Steps to upload file
    #1. fildialog is imported at the top
    #2. create variable and use inside that askopenfilename  and inside mention all files which we can upload
    #3. let say we upload image then we use image function Photoimage, import PIL at top and label to show image on screen. but if yiu are uploading a file like python file, text file then directly use label.
    file1=filedialog.askopenfilename(initialdir="C:/users/downloads",filetypes=(("Python File", ".py"), ("Image File", ".png"), ("Image File", ".jpg"), ("HTML File", ".html"), ("Text File", ".txt")) )
    global S
    S=ImageTk.PhotoImage(Image.open(file1))
    l1=Label(screen, image=S)
    l1.grid(row=1, column=1)


b1=Button(screen, text='Download', command=download)
b1.grid(row=0, column=1)

b2=Button(screen, text="upload", command=upload)
b2.grid(row=0, column=0)

#----------------------------------------------------Scale-------------------------------------------------------
#Scale is used to create a slider where we can select the range.
#we wil;l create a slider and then select number on it and then get that number and display as label ons creen

def display():
    l1=Label(screen, text="Hello the number is " + str(s.get()))
    l1.grid(row=2, column=1)


s=Scale(screen, from_=0, to=100, orient=HORIZONTAL)
s.grid(row=1, column=0)

b3=Button(screen, text="Click here tp get no from slider", command=display)
b3.grid(row=3, column=1)


mainloop()