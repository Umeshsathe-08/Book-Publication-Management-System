
#Tkinter is the python standard GUI(Grafical User Interface) Library which is used to develope the web applications.

from tkinter import *           #inbuilt classes,functions,keywords can be accessed.
import tkinter                  #Library used to make GUI of Interactive Web applications. 
from tkinter import messagebox  #Module used for display the message boxes in python Web applications. 
import mysql.connector          #modulefor connection with database

# creating Instance/Object of the Tkinter frame
windo = tkinter.Tk() 

windo.title('Book Publication Management System')     #For title of the window 
windo.configure(width=1500, height=600, bg="gray")    #for configuration of window 

L = Label(windo, text=" BOOK PUBLICATION MANAGEMENT SYSTEM ", font=('Algerian',30), fg='Black', bg="gray", bd=5,
          width=40, justify=CENTER)           #It is widget/class in a tkinter used specify container box where we can place the text.
L.grid(row=0, column=0)   # It organises the widgets in a table like structure. #The master widget is split into rows ans columns.

L1 = Label(windo, text="Enter Book Id: ", font=('Rockwell Extra Bold', 20), fg='Purple', bg="white", justify="left")
L1.grid(row=2, column=0)
E1 = Entry(windo, bd=1, width=50, fg='red')  # Entry widget used to enter or display a single line of text.
E1.grid(row=2, column=1)
L2 = Label(windo, text="Enter Book Name: ", font=('Rockwell Extra Bold', 20), fg='Purple', bg="white", justify="left")
L2.grid(row=3, column=0)
E2 = Entry(windo, bd=1, width=50, fg='red')
E2.grid(row=3, column=1)
L3 = Label(windo, text="Enter year of publication: ", font=('Rockwell Extra Bold', 20), fg='Purple', bg="white",justify="left")
L3.grid(row=4, column=0)
E3 = Entry(windo, bd=1, width=50, fg='red')
E3.grid(row=4, column=1)
L4 = Label(windo, text="Enter author name: ", font=('Rockwell Extra Bold', 20), fg='Purple', bg="white", justify="left")
L4.grid(row=5, column=0)
E4 = Entry(windo, bd=1, width=50, fg='red')
E4.grid(row=5, column=1)
L5 = Label(windo, text="Enter Edition: ", font=('Rockwell Extra Bold', 20), fg='Purple', bg="white", justify="left")
L5.grid(row=6, column=0)
E5 = Entry(windo, bd=1, width=50, fg='red')
E5.grid(row=6, column=1)
L6 = Label(windo, text="Enter publishing company: ", font=('Rockwell Extra Bold', 20), fg='Purple', bg="white",justify="left")
L6.grid(row=7, column=0)
E6 = Entry(windo, bd=5, width=50, fg='red')
E6.grid(row=7, column=1)


def myButtonEvent(selection):
    print("Book id is : ", E1.get())
    print("Book  name is : ", E2.get())
    print("Year of publication is : ", E3.get())
    print("Author name is : ", E4.get())
    print("Edition is : ", E5.get())
    print("Publishaing Company is : ", E6.get())

    BookId = E1.get()
    BookName = E2.get()
    YOPublication = E3.get()
    AuthorName = E4.get()
    BookEddition = E5.get()
    PublicationName = E6.get()
    if selection in 'Insert':
        con = mysql.connector.connect(host="localhost", user="root", passwd="Usathe_008", database="book")
        print(con)         #printing returned object.
        cur = con.cursor() #it is used to execute query,retrieve data,one row at a time from a result set/relation.

        insQuery = "insert into bpmanagement (BookId,BookName,YOPublication,AuthorName,BookEddition,PublicationName) values ('%s','%s','%s','%s','%s','%s')" % (
        BookId, BookName, YOPublication, AuthorName, BookEddition, PublicationName)
        cur.execute(insQuery)  #query execution
        con.commit()   # it is used to update values in Table/Relation
    elif selection in 'Update':

        con = mysql.connector.connect(host="localhost", user="root", passwd="Usathe_008", database="book")
        print(con)
        cur = con.cursor()

        query = "update bpmanagement set BookId ='%s'" % BookId + ",AuthorName='%s'" % AuthorName + "where BookId ='%s'" % BookId

        cur.execute(query)
        con.commit()


    elif selection in 'Delete':

        con = mysql.connector.connect(host="localhost", user="root", passwd="Usathe_008", database="book")
        print(con)
        cur = con.cursor()

        query = "delete from bpmanagement where BookId ='%s'" % BookId

        cur.execute(query)
        con.commit()


   
        rows = cur.fetchall()
        YOPublication = ''
        BookName = ''
        BookId = ''
        for row in rows:
            BookId = row[1]
            BookName = row[2]
            YOPublication = row[3]
            E1.delete(0, END)
            E2.delete(0, END)
            E3.delete(0, END)

            E1.insert(0, BookId)
            E2.insert(0, BookName)
            E3.insert(0, YOPublication)


BInsert = tkinter.Button(text='Insert', fg='maroon', activeforeground="green", bg='white',
                         font=('Elephant', 15, 'bold'),
                         command=lambda: myButtonEvent('Insert'))
BInsert.grid(row=8, column=1,pady=8)

BUpdate = tkinter.Button(text='Update', fg='maroon', activeforeground="yellow", bg='white',
                         font=('Elephant', 15, 'bold'),
                         command=lambda: myButtonEvent('Update'))
BUpdate.grid(row=12, column=1,pady=8)

BDelete = tkinter.Button(text='Delete', fg='maroon', activeforeground="red", bg='white', font=('Elephant', 15,),
                         command=lambda: myButtonEvent('Delete'))
BDelete.grid(row=16,column=1,pady=8)

windo.mainloop()  #infinite loop is used to run the application,wait for an event to occur and process the event as long as window is not closed.
