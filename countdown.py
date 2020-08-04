import time
from tkinter import *
from tkinter import messagebox

#creating TK window
root=Tk()
#set size for the window
root.geometry("300x250")
#give title
root.title("Time Counter")

hour=StringVar()
minute=StringVar()
second=StringVar()
#default values
hour.set("00")
minute.set("00")
second.set("00")
#use Entry class to get input from the user
hourEntry=Entry(root,width=3,font=('Arial',18,''),textvariable=hour)
hourEntry.place(x=80,y=20)
minuteEntry=Entry(root,width=3,font=('Arial',18,''),textvariable=minute)
minuteEntry.place(x=130,y=20)
secondEntry=Entry(root,width=3,font=('Arial',18,''),textvariable=second)
secondEntry.place(x=180,y=20)

def submit():
    try:
        #user input is stored in temp
        temp=int(hour.get())**3600+int(minute.get())*60+int(second.get())
    except:
        print("Please enter valid input")
    while temp > -1:
        mins,secs=divmod(temp,60)
        hours=0
        if mins>60:
            hours,mins=divmod(mins,60)
        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))
        root.update()
        time.sleep(1)
        if temp==0:
            messagebox.showinfo("Time's up")
        temp-=1
#button
btn=Button(root,text="Set Time Countdown",bd='5',command=submit)
btn.place(x=70,y=120)
#infinite loop
root.mainloop()
