from tkinter import *
from tkinter import ttk
from tkinter import messagebox


GUI=Tk()
GUI.title('โปรแกรมบันทึกตารางเรียน')
GUI.geometry('500x400')

L1 = Label(GUI,text='ตารางเรียน')
L1.place(x=10,y=20)

def Button1():
    text='science math'
    messagebox.showinfo('วิชาที่เรียน',text)

FB1 = Frame(GUI)
FB1.place(x=20,y=50)
B1=ttk.Button(FB1,text='Monday',command=Button1)
B1.pack(ipadx=20,ipady=20)

##########################################

def Button2():
    text='history biology'
    messagebox.showinfo('วิชาที่เรียน',text)

FB2=Frame(GUI)
FB2.place(x=20,y=70)
B2=ttk.Button(FB1,text='Tuesday',command=Button2)
B2.pack(ipadx=20,ipady=20)

##########################################

def Button3():
    text='chemistry'
    messagebox.showinfo('วิชาที่เรียน',text)

FB3=Frame(GUI)
FB3.place(x=20,y=90)
B3=ttk.Button(FB1,text='Wednesday',command=Button3)
B3.pack(ipadx=20,ipady=20)

##########################################

def Button4():
    text='english computer'
    messagebox.showinfo('วิชาที่เรียน',text)

FB4=Frame(GUI)
FB4.place(x=20,y=110)
B4=ttk.Button(FB1,text='Thursday',command=Button4)
B4.pack(ipadx=20,ipady=20)
