# Python program to illustrate a stop watch
# using Tkinter
# importing the required libraries
import mysql.connector
import tkinter as Tkinter
from datetime import datetime
from tkinter import *


counter = 0
running = False


def counter_label(label):
    def count():
        if running:
            global counter

            # To manage the intial delay.
            if counter == 0:
                display = "Starting..."
            else:
                tt = datetime.fromtimestamp(counter)
                string = tt.strftime("%M:%S")
                display = string

            label['text'] = display  # Or label.config(text=display)

            # label.after(arg1, arg2) delays by
            # first argument given in milliseconds
            # and then calls the function given as second argument.
            # Generally like here we need to call the
            # function in which it is present repeatedly.
            # Delays by 1000ms=1 seconds and call count again.
            label.after(1000, count)
            counter += 1

    # Triggering the start of the counter.
    count()


# start function of the stopwatch
def start(label):
    global running
    running = True
    counter_label(label)
    Start['state'] = 'disabled'
    Stop['state'] = 'normal'
    Reset['state'] = 'normal'


# Stop function of the stopwatch
def stop():
    global running
    Start['state'] = 'normal'
    Reset['state'] = 'normal'
    running = False
    customer_name = my_var.get()

    if customer_name:
        insert_mysql()
        label = Tkinter.Label(text="Reset", fg="black", font="Verdana 30 bold")
    else:
        Start['state'] = 'disabled'
        Reset['state'] = 'disabled'
        displayerror()


def displayerror():
    label = Tkinter.Label(text="You need a Customer!", fg="black", font="Verdana 30 bold")
    label.pack()


def insert_mysql():
    mydb = mysql.connector.connect(
        host="localhost",
        user="timetracker",
        password="Timetracker2020",
        database="timetracker"
    )
    mycursor = mydb.cursor()
    tt = datetime.fromtimestamp(counter)
    string = tt.strftime("%M:%S")
    display = string
    customer_name = my_var.get()
    sql = "INSERT INTO entries (customer, time_entry) VALUES (%s, %s)"
    val = (customer_name,  string)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")


# Reset function of the stopwatch
def reset(label):
    global counter

    counter = 0
    # If rest is pressed after pressing stop.
    if not running:
        label['text'] = 'Welcome!'
        label = Tkinter.Label(text="Reset", fg="black", font="Verdana 30 bold")

    # If reset is pressed while the stopwatch is running.
    else:
        label['text'] = 'Starting...'
        label = Tkinter.Label(text="Reset", fg="black", font="Verdana 30 bold")


def displaydb():
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel()


    # sets the title of the
    # Toplevel widget
    newWindow.title("Database")

    # sets the geometry of toplevel
    newWindow.minsize(width=350, height=200)

    # A Label widget to show in toplevel
    # Connection MYSQL
    my_connect = mysql.connector.connect(
        host="localhost",
        user="timetracker",
        password="Timetracker2020",
        database="timetracker"
    )
    # Connection MYSQL

    # Create a display grid---
    my_conn = my_connect.cursor()
    my_conn.execute("SELECT customer,time_entry,TIMESTAMP FROM entries  ORDER BY id DESC LIMIT 10")
    i = 0
    for entries in my_conn:
        for j in range(len(entries)):
            e = Entry(newWindow, width=25, fg='blue')
            e.grid(row=i, column=j)
            e.insert(END, entries[j])
        i = i + 1
    # ---Create a display grid
    newWindow.mainloop()


root = Tkinter.Tk()
root.title("TimeTracker")

# Fixing the window size.
root.minsize(width=250, height=200)
label = Tkinter.Label(root, text="Welcome To TimeTracker!", fg="black", font="Verdana 30 bold")
f = Tkinter.Frame(root)


# name using widget Label
my_var = StringVar()
enter_name = Tkinter.Entry(f, text="First Name", textvariable=my_var)
enter_name.pack()

label.pack()
Start = Tkinter.Button(f, text='Start', width=6, command=lambda: start(label))
Stop = Tkinter.Button(f, text='Submit', width=6, state='disabled', command=stop)
Reset = Tkinter.Button(f, text='Reset', width=6, state='disabled', command=lambda: reset(label))
ShowDB = Tkinter.Button(text='Display DB', width=25, command=displaydb)


f.pack(anchor='center', pady=5)
Start.pack(side="left")
Stop.pack(side="left")
Reset.pack(side="left")
ShowDB.pack(side=BOTTOM)
root.mainloop()
