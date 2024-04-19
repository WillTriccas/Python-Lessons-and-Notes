from tkinter import *

window = Tk()


def Kg_Convert():
    grams = float(E1_value.get())*1000
    t1.delete("1.0", END)
    t1.insert(END, grams)

    Ounces = float(E1_value.get())*35.274
    t2.delete("1.0", END)
    t2.insert(END, Ounces)

    Pounds = float(E1_value.get())*2.20462
    t3.delete("1.0", END)
    t3.insert(END, Pounds)

    #The t.2.delete() function deletes anything that was previous in the box so that if you use the app again it relays only the numbers you
    #care about in the text box (the "1.0",END makes sure that everything from the start to the 'END' is deleted from the text box)


b1 = Button(window, text = "Convert!", command = Kg_Convert)
b1.grid(row = 0, column = 0)

E1_value = StringVar()

e1 = Entry(window, width = 40, textvariable = E1_value)
e1.grid(row = 0, column = 1, columnspan = 2)

t1 = Text(window, height = 1, width = 20)
t2 = Text(window, height = 1, width = 20)
t3 = Text(window, height = 1, width = 20)
t1.grid(row = 1, column =0)
t2.grid(row = 1, column =1)
t3.grid(row = 1, column =2)


window.mainloop()