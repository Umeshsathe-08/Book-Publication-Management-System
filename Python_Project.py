from tkinter import *
import tkinter
from tkinter import messagebox
import mysql.connector
windo = tkinter.Tk()
windo.geometry("800x550")
windo.config(bg="White")
windo.title('Book Publication Management System')
L =Label(windo, text = "Enter Book Id: ",font =('italic',20),fg='black',bg="white")
L.grid(row=0,column=0)
E=Entry(windo, bd=5, width=50)
E.grid(row=0, column=1)
L1 =Label(windo, text = "Enter Book Name: ",font =('italic',20),fg='black',bg="white")
L1.grid(row=1,column=0)
E1=Entry(windo, bd=5, width=50)
E1.grid(row=1, column=1)
L2 =Label(windo, text = "Enter Year of Publication: ",font =('italic',20),fg='black',bg="white")
L2.grid(row=2,column=0)
E2=Entry(windo, bd=5, width=50)
E2.grid(row=2, column=1)
L3 =Label(windo, text = "Enter Author Name: ",font =('italic',20),fg='black',bg="white")
L3.grid(row=3,column=0)
E3=Entry(windo, bd=5, width=50)
E3.grid(row=3, column=1)
L4 =Label(windo, text = "Enter Edition: ",font =('italic',20),fg='black',bg="white")
L4.grid(row=4,column=0)
E4=Entry(windo, bd=5, width=50)
E4.grid(row=4, column=1)
L5 =Label(windo, text = "Enter Name of Publishing Company: ",font =('italic',20),fg='black',bg="white")
L5.grid(row=5,column=0)
E5=Entry(windo, bd=5, width=50)
E5.grid(row=5, column=1)


def myButtonEvent(selection):
  print("Book ID is : ", E.get())
  print("Book Name is : ", E1.get())
  print("Year of Publication is : ", E2.get())
  print("Author Name is : ", E3.get())
  print("Edition is : ", E4.get())
  print("Name of Publishing Company is : ", E5.get())

  ID = E.get()
  Name = E1.get()
  Year = E2.get()
  Author = E3.get()
  Edition = E4.get()
  Company = E5.get()
  if  selection in ('Insert'):
         con = mysql.connector.connect(host="localhost", user="root", passwd="Usathe_008", database="BPMsys")
         print(con)
         cur = con.cursor()

         insQuery = "insert into BPMsystem(ID,Name,Year,Author,Edition,Company ) values ('%s','%s','%s','%s','%s','%s')" % (ID, Name, Year,Author,Edition,Company)
         cur.execute(insQuery)
         con.commit()
  elif selection in ('Update'):

     con = mysql.connector.connect(host="localhost", user="root", passwd="Usathe_008", database="BPMsys")
     print(con)
     cur = con.cursor()

     query = "update BPMsystem set Name ='%s'" % (Name) + ",Author='%s'" % (Author) + "where ID ='%s'" % (ID)

     cur.execute(query)
     con.commit()


  elif selection in ('Delete'):

    con = mysql.connector.connect(host="localhost", user="root", passwd="Usathe_008", database="BPMsys")
    print(con)
    cur = con.cursor()

    query = "delete from BPMsystem where ID ='%s'" % (ID)

    cur.execute(query)
    con.commit()


  elif selection in ('Select'):

    con = mysql.connector.connect(host="localhost", user="root", passwd="Usathe_008", database="BPMsys")
    print(con)
    cur = con.cursor()

    query = "select * from BPMsystem where ID ='%s'" % (ID)

    cur.execute(query)
    rows = cur.fetchall()
    Company = ''
    Name1 = ''
    ID1 = ''
    for row in rows:
        ID1 = row[0]
        Name1 = row[1]
        Company = row[5]
        E.delete(0, END)
        E1.delete(0, END)
        E2.delete(0, END)

        E.insert(0, ID1)
        E1.insert(0, Name1)
        E2.insert(0, Company)

BInsert = tkinter.Button(text='Insert', fg='Black', bg='Gray', font=('bold serif', 17, 'italic'),
                         command=lambda: myButtonEvent('Insert'))
BInsert.grid(row=10, column=0)

BUpdate = tkinter.Button(text='Update', fg='black', bg='Gray', font=('bold script', 17, 'italic'),
                         command=lambda: myButtonEvent('Update'))
BUpdate.grid(row=10, column=1)

BDelete = tkinter.Button(text='Delete', fg='black', bg='Gray', font=('typewriter', 17, 'italic'),
                         command=lambda: myButtonEvent('Delete'))
BDelete.grid(row=20, column=0)

BSelect = tkinter.Button(text='Select', fg='black', bg='Gray', font=('italic', 17, 'italic'),
                         command=lambda: myButtonEvent('Select'))
BSelect.grid(row=20, column=1 )

windo.mainloop()