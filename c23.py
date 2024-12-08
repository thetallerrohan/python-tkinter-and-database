#list box means a box whre we cana have a lot of items out of which we can select one or multiple
from tkinter import *
route=Tk()
L1=Listbox(route,width=15,height=10)
#put items in this list box using insert function
L1.insert(1,"rice")
L1.insert(2,"apple")
L1.insert(3,"cashew")
L1.insert(4,"oranges")
L1.insert(5,"bannana")
L1.grid(row=1,column=1)
#delete, select, delete all, select all, ,multiple select
L2=Label(route)
L2.grid(row=7,column=0)
def delete():
    L1.delete(ANCHOR)
    L2.config(text="")
def select():
    #select one item at one time from list and show as label
    L2.config(text=L1.get(ANCHOR))
    

def deleteAll():
    L1.delete(0,END)
    #delete all items from list

def selectAll():
    #select all items from list  and display as label on screen
    result=' '
    for item in L1.curselection():
        result=result+str(L1.get(item))+'\n'
        #we are getall data which we selected through cursor in for loop and the  one by one store in r variable and through we display that data by using label on screen.
    L2.config(text=r)



def deletemultiple():
    #multiple items can be selected  and displayed as label on screen
    for item in reversed(L1.cusrselection()):
        L1.delete(item)
        L2.config(text=" ")
#confif() is used when we want to change properties of lebl, button, textbox etc.. there text, bg, fg etc..



b1=Button(route,text="delete", command=delete)
b1.grid(row=2,column=1)
b2=Button(route,text="select",command=select)
b2.grid(row=3,column=1)
b3=Button(route,text="delete all", command=deleteAll)
b3.grid(row=4,column=1)
b4=Button(route,text="select all", command=select)
b4.grid(row=5,column=1)
b5=Button(route,text="mutiple delete",command=deletemultiple)
b5.grid(row=6,column=1)
route.mainloop()


