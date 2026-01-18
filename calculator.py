from tkinter import *
from tkinter.messagebox import * 


calc = Tk()
calc.title('Калькулятор')
calc.geometry('1000x1000+500+100')
calc.config(bg="#1B1A1A")


def f1():
    x = float(ent.get())
    y = float(ent1.get())
    w = x + y
    ent2.delete(0, END)
    ent2.insert(0, str(w))

def f2():
    x = float(ent.get())
    y = float(ent1.get())
    w = x - y
    ent2.delete(0, END)
    ent2.insert(0, str(w))

def f3():
    x = float(ent.get())
    y = float(ent1.get())
    w = x * y
    ent2.delete(0, END)
    ent2.insert(0, str(w))

def f4():
    x = float(ent.get())
    y = float(ent1.get())
    w = x / y
    ent2.delete(0, END)
    ent2.insert(0, str(w))

def f5():
    x = float(ent.get())
    y = float(ent1.get())
    w = x ** y
    ent2.delete(0, END)
    ent2.insert(0, str(w))

def clear():
    ent.delete(0, END)
    ent1.delete(0, END)
    ent2.delete(0, END)

def resres():
    ent2.delete(0, END)


ent = Entry(font=('Arial 15'))
ent.grid(column=0, row=1, padx=20, pady=20, ipady=15)
ent1 = Entry(font=('Arial 15'))
ent1.grid(column=3, row=1, ipady=15)
ent2 = Entry(font=('Arial 15'))
ent2.grid(column=4, row=1, padx=60, ipady=15)


btn = Button(text='+', command=f1)
btn.config(width=4, height=2)
btn.grid(column=1, row=1)
btn1 = Button(text='-', command=f2)
btn1.config(width=4, height=2)
btn1.grid(column=1, row=2)
btn2 = Button(text='*', command=f3)
btn2.config(width=4, height=2)
btn2.grid(column=1, row=3, padx=60)
btn3 = Button(text=':', command=f4)
btn3.config(width=4, height=2)
btn3.grid(column=1, row=4, padx=60)
btn_resres = Button(text='C', command=resres, width=8, height=5)
btn_resres.grid(column=0, row=5)
btn_sq = Button(text='^', command=f5, width=4, height=2)
btn_sq.grid(column=1, row=5, padx=60)
btn_c = Button(text='AC', command=clear, width=8, height=5)
btn_c.grid(column=0, row=3)




calc.mainloop()