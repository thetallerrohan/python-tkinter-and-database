#message box means a pop up notification poping up on screen like a simple message,waring message,error message
from tkinter import *
from tkinter import messagebox
route = Tk()
route.title("message box screen")
route.geometry("800x800")

#different function are used in different situations
#we do not use any pack(),  grid() place() for the messagebox as they notification messahe which come seperately not on screen
#this one is for simple message. for all messahebox we see different different icons eg : for error its different icon, for warning its different icon ...
messagebox.showinfo("Info", "Your details have been submitted")
#tnis one is for error message
messagebox.showerror("Error", "There was a error whiel downloading a file")
#this one is for warning message
messagebox.showwarning("Warning", "Be careful while downloading the file it might contain virus")
#this one is when you want to ask a question to confirm it has different buttons, there are total 4 functions to ask question diffrence is all have different buttons.
messagebox.askokcancel("Question", "Do you want to confirm or not ?")
#this is for askyesno
messagebox.askyesno("Question", " Do you want to confirm it or not?")
#this has askyesnocancel button
messagebox.askyesnocancel("Question", "Do you want to confirm or not?")
#this means askretrycancel
messagebox.askretrycancel("Question", "D you want to confirm tjis or not?")

#-------------------------------------------Another Screen--------------------------------------------
#so we will creatre one button on first page hwne we click on the button it takes us to second page. Always creatye one function and inside that
#use Tk() to create new page and call taht function on button

def newscreen():
    screen2=Tk()
    #now create one button on this page remember wehnver you create a thing on second page write the name of second page like in this case it is 
    screen2
    b2=Button(screen2, text="Submitted")
    b2.pack()

#remember use command to call function in tkinter.
b1=Button(route, text="Click here to go new page", command=newscreen)
b1.pack()

route.mainloop()


#--------------------------------------Assignment-------------------------------
#do session 19 assignment 
