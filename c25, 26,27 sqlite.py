#sqlite is a inbuilt database prsent in python in the form of library which needs to import and use it. It's a small library which can hold small amount if data.OFF so ist good only for small software applications. This does not needs to be installed like other database which is good.

#---------------Queries , commands needs to be operated in database Steps to be followed-------------------
#1. import library. 
#2. use connect function with database if database exist then it will get connected to that otherwise new dtaabase will be created

#syntax : variablename=sqlite3.connect(databasename)
#3. Use cusror function thsi is for exexcuting teh command.create object of this

#4. Create table command to create table as data in database is always stored in table. Once it is done then use cursor object to execute the table command
#5. Insert command to unsert data. use cursor command to execute the insert command
#6 select to select data and fetch it
#7. Update command to update the data in database
#8. Delete command to delete the data from database


#Note: After all 5 commands : create table, Insert data, select, update, delete after all these commands cursor object need to used to execute all these commands

#--------------------syntax for queries-------------------
#1. create table :
#create table nameofthetable(coulunname1 datatype, coulnme2 datatype, coulnname3.......................)

#datatypes are int, text, varchar() this when specific chracter, numbers alphabets together come.

#Always columns are according to data which is coming from software

#2, Insert in table :
#Insert tablename into(coluname1, coluname2, columname3...) values(value1, vavalue2m value3, value3,)