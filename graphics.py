from tkinter import *

root = Tk()
root.title('Graphics')

canvas = Canvas(width=300, height=300)
canvas.pack()

reddraw = canvas.create_line(0,0,300,50,fill='red')
bluedraw = canvas.create_line(0,150,300,50,fill='blue')
yellowbox = canvas.create_rectangle(25,25,150,70,fill='yellow')

canvas.delete(ALL)

root.mainloop()