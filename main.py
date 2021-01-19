import time
import mysql.connector


from tkinter import *
window=Tk()


window.title('StopWatch')
window.geometry("300x200+10+20")


window.mainloop()

# Code to add widgets will go here...


def time_convert(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),int(sec)))


customerval = txtfld=Entry(window, text="This is Entry Widget", bd=5)
input("Press Enter to start")
start_time = time.time()

input("Press Enter to stop")
end_time = time.time()

time_lapsed = end_time - start_time
time_convert(time_lapsed)


lbl=Label(window, text=time_lapsed, fg='red', font=("Helvetica", 16))

mydb = mysql.connector.connect(
  host="localhost",
  user="timetracker",
  password="Timetracker2020",
  database="timetracker"
)

mycursor = mydb.cursor()


sql = "INSERT INTO entries (customer, time_entry) VALUES (%s, %s)"
val = (customerval, time_lapsed)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

