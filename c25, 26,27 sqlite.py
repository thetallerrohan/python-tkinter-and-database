#SQ-Lite is a database to store data or information which we get from the user and lateron we can use that information exampel when the user signs up his details
#are stored in a database and later when he logs in we  atch up those login details with the previosu store sign up details. If it matche sup it allows us to login.
#Database is like a memory where we can store so many things.For exampel you have created a game and you wanted to store something from the game but the game doesnt have enough memory.
#Which means there is no database because of lack of memory. This means we cannot store anything permanently in that game.
#Advantages:
#SQ-lite is an in built database library in python. You do not have to install or setup.
#This saves time.
#No setup process which makes it quicker.
#Lightweight
#Disadvantage:
# It has less space so it can only be used to store small data.
#Neutral:
#SQ-lite database can be used with games, softwares, websites, apps, etc.

#But in case if yu want to store large data databases like MYSQL, firebase, oracle are used.

#Also coding for database is pretty much the same. queries are same. so if you learm one database you can do coding in other databases by yourself.

#database also uses language called as SQL.

#Steps to to code in Sqlite
#1. import sqlite library
#2. connect with sqlite database usig connect method. syntax : variablname=sqlite3.connect("database.db"). if database is alreday there with that name it will get connect to existing db but if not there then it will create database with that name
#3. Create cusror object using cusror function . cursor() helps you to execute the query once written.
#4. Create table as data here is always stored in grid form. syntax to create table : CREATE TABLE tablename(columnname datatype, columname2 datatype, columname3 datatype, coulnname4 datatype and so on)
#5. Insert data in table using insert syntax : INSERT Into tablename VALUES (data1, data2, data3 so on)
#6. want to get data on screen : use select to select what data you want and then use fetchall. syntax : SELECT * from tablename. Use fetchall to get data afterwards
#7. To update any data syntax : UPDATE tablename set name="hamzah" where id=1.
#8. To delete the data syntax : DELETE table tablename where id=1

#To get thinsg from entry box use get and to insert use insert ()


#SQ-Lite Coding
import sqlite3 #We are using the latest version of sqlite 
#--------------------------------------------sqlite connection----------------------------------------
sq=sqlite3.connect("database.db")
cursor=sq.cursor()
#We will use create table query to create a table and the cursor is going to execute the query.
#----------------------------------------------create table---------------------------------------------
cursor.execute("""
create table emp1 (
Staff_number int,
First_name text,
last_name text,
Gender text,
date_of_joining varchar(100)
)
""") #Table name is always according to whatever game or software we are creating. For example, if we are storign teh student details the nwe will give the name as "student". The two column names will be whatever is comign from teh Tkinter screen. 
#datatype is given for each column: int, text, varchar(30): when it has text, number, special character.30 is limit we cannot ahve more than 30 alpahabets

#----------------------------------------------------Insert data in tkinter--------------------------------------------------
#when we click on add button then data goes in database. so we do coding of adding data in database in one function and then call that function on button.
def add():
    #so first we get data from textboxes using get() and then we give this data to the table emp, to there columns
    Staff=e1.get()
    first_name=e2.get()
    last_name=e3.get()
    gender=e4.get()
    date_of_joining=e5.get()
    #now we give these values to insert query who will put these values into the table emp. all queries are written always in cusror.exceute(0 as we know that cusror exceutes all queries)
    cursor.execute("""   
    INSERT into emp1(Staff_number, First_name, last_name, Gender, date_of_joining) values(?, ?, ?, ?, ?)
    """, (Staff, first_name, last_name, gender, date_of_joining))
    #insert into (column1, column2...) values(give variablenames) ? is temporary key use to write in place of variables as we cannot write variable name directly.
    #use commit() to save 
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    sq.commit()


#---------------------------------------get detail from database--------------------------------
#so first a person will enter a staff no in entrybox e6, then we will get that staff number and serach for it in database if we get details we get that usieng select() and fetchall() function and display it using label on screen.

def getdetail():
    staffnumber=e6.get()
    cursor.execute("Select * from emp1 where Staff_number=?",(staffnumber,))
    record=cursor.fetchall()
    records=""
    #record has all data now we use for loop to get one by one data and label to use for dispaying on screen
    for i in record:
        records=str(i[0]) +"\n" +str(i[1]) +"\n" +str(i[2]) +"\n" +str([3]) +"\n" +str(i[4])+"\n"
    l8=Label(screen, text=records)
    l8.grid(row=29, column=4)
    sq.commit()

#-------------------------------------------delete data ---------------------------
#Who so ever employee detail we want to delete, that employees staff number we will eneter in the entrybox(e6)
def delete():
    staffnumber=e6.get()
    cursor.execute("delete from emp1 where Staff_number=?",(staffnumber,))
    sq.commit() 
#----------------------------------------update data------------------------------
#For updating the data we create a second new screen where we have the same details at the first page. Same labels and boxes wil lbe same.
#But on the second screen the textbokes are filled and then we can anythign and 
#so we will create one function update () -> craete simsilar interface as first page/screen, use select and fetchall query to get data 
#and insert into textbox/entrybox.
#create edit() function : upate query is used to update person details

def edit():
    staffnumber=e11.get()
    firstname=e12.get()
    lastname=e13.get()
    Gender=e14.get()
    dateofjoining=e15.get()
    search=e6.get()
    cursor.execute("""Update emp1 set Staff_number=?,First_name=?,Last_name=?,Gender=?,date_of_joining=? where staff_number=?""",(staffnumber,firstname,lastname,Gender,dateofjoining,search))
    sq.commit()
    
   

def update():
    screen1=Tk()
    global e11,e12,e13,e14,e15
    l11=Label(screen1, text="Staff number")
    l11.grid(row=2,column=1)

    l12=Label(screen1, text="First Name")
    l12.grid(row=4,column=1)

    l13=Label(screen1, text="Last Name")
    l13.grid(row=8,column=1)

    l14=Label(screen1, text="Gender")
    l14.grid(row=12, column=1)

    l15=Label(screen1, text="Date of Joining")
    l15.grid(row=16, column=1)
    
    e11=Entry(screen1)
    e11.grid(row=1, column=4)

    e12=Entry(screen1)
    e12.grid(row=4, column=4)

    e13=Entry(screen1)
    e13.grid(row=8, column=4)

    e14=Entry(screen1)
    e14.grid(row=12, column=4)

    e15=Entry(screen1)
    e15.grid(row=16, column=4)

    staffnumber=e6.get()
    cursor.execute("Select * from emp1 where Staff_number=?",(staffnumber,))
    record=cursor.fetchall()
    records=""
    for i in record:
        e11.insert(END, i[0])
        e12.insert(END, i[1])
        e13.insert(END, i[2])
        e14.insert(END, i[3])
        e15.insert(END, i[4])
    b11=Button(screen1, text="Update",command=edit)
    b11.grid(row=20,column=3)
    
    sq.commit()

#------------------------------------------------------------------------------------------------------------------
from tkinter import*

screen=Tk()
screen.title("Class 25")
screen.geometry("1000x1000")

l1=Label(screen, text="Staff number")
l1.grid(row=1,column=1)

l2=Label(screen, text="First Name")
l2.grid(row=4,column=1)

l3=Label(screen, text="Last Name")
l3.grid(row=8,column=1)

l4=Label(screen, text="Gender")
l4.grid(row=12, column=1)

l5=Label(screen, text="Date of Joining")
l5.grid(row=16, column=1)

e1=Entry(screen)
e1.grid(row=1, column=4)

e2=Entry(screen)
e2.grid(row=4, column=4)

e3=Entry(screen)
e3.grid(row=8, column=4)

e4=Entry(screen)
e4.grid(row=12, column=4)

e5=Entry(screen)
e5.grid(row=16, column=4)

b1=Button(screen, text="Add record to database", command=add)
b1.grid(row=20, column=3)

b2=Button(screen, text="Query to database", command=getdetail)
b2.grid(row=24, column=3)
#Below l6 (label) and e6 (entrybox) is that entrybox which is used by query button, delete button, and update button.
# This is the extra entry box which is created so that if a person wants to get anyones detail, we can eneter his id over here. If we want to delete someones detail, eneter his id in this entrybox and the nclick on teh delete button. That persons detail will be deleted. 
# In order to update anyones detail, we have to enter that person's ID in that entry box and then a new screen will opened and where the details of the persons will already be filled on the entryboxes.
# And the person can delete the details. This extra entrybox is like a search box  
l6=Label(screen, text="Enter staff number whose detail you would liike to check")
l6.grid(row=28, column=3)

e6=Entry(screen)
e6.grid(row=28, column=4)

b3=Button(screen, text="Update", command=update)
b3.grid(row=30, column=3)

b4=Button(screen, text="Delete", command=delete)
b4.grid(row=32, column=3)

screen.mainloop()
