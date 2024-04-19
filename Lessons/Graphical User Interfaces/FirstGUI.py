from tkinter import *

window = Tk()


def Km_To_Miles():
    miles = float(E1_Value.get())*1.6
    t1.insert(END, miles)

b1 = Button(window, text = "Press Me", command = Km_To_Miles)
b1.grid(row = 0, column = 0)

E1_Value = StringVar()

e1 = Entry(window, textvariable = E1_Value)
e1.grid(row = 0, column = 1)

t1 = Text(window, height = 1, width = 20,)
t1.grid(row =1, column =0, columnspan = 2)


window.mainloop()