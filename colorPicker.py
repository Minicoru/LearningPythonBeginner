from tkinter import *
from tkinter.colorchooser import *

g = Tk()


def my_color():
    color = askcolor()
    my_label = Label(text='This is your preferred color',bg=color[1]).pack()


btn = Button(text='Pick color', command=my_color)
btn.pack()

g.mainloop()

