from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox

GUI = Tk() #จอหลัก
GUI.title('โปรแกรมบันทึกข้อมูล') #ชื่อโปรแกรม
GUI.geometry('500x500')

b1 = ttk.Button(GUI,text='มีเงินกี่บาท')
b1.pack(iadx=20,ipady=20)

def Botton2():
    text = 'ตอนนี้มีเงิน200บาท'
    massagebox.showinfo('เงิน',text)

Fb1 = Frame(GUI)
Fb1.place(x=100,y=300)
B2 = ttk.Botton(Fb1,text='มีเงินกี่บาท',command=botton2)
B2.pack(ipadx=20,ipady=20)

GUI.mainloop()
