#----------------------------------Images/ icons/frames-----------------------------------
#Steps to give image on screen in tkinter
#1. import PIL library(Pillow) from there we use image func
#2. open file : use Image.open("imagename")
#3. use Imagetk.PhotoImage(variablename)
#4. label to display image on screen use text=image

#Steps to create icon 
#Photoimage to load the image
#1. use iconbitmap() for images of .ico extension. iconphoto() for png images. eg : screename.iconphoto(variablename)

from tkinter import *
from PIL import ImageTk, Image

# Create tkinter screen and caption
screen = Tk()
screen.title("Images, Icons, Frames")
screen.geometry("800x800")

# Set icon on screen
img_icon = PhotoImage(file="C:/Users/rohan/OneDrive/Desktop/python/download (14).jpeg")
screen.iconphoto(False, img_icon)

# Load and display image on screen
img = Image.open("C:/Users/rohan/OneDrive/Desktop/python/download (14).jpeg")
img_tk = ImageTk.PhotoImage(img)
l1 = Label(screen, image=img_tk)
l1.pack()

# Keep a reference to avoid garbage collection
l1.image = img_tk

screen.mainloop()
