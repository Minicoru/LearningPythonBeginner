from tkinter import *
from  tkinter import ttk

counter = 0


def mark_lap():
    global treeview
    size = treeview.size()
    print(size)
    treeview.insert(parent='', index='end', iid=treeview.size(), text='', values=[treeview.size()+1])


def reset_counter():
    global counter
    global myLabel
    counter = 0
    myLabel.config(text=str(counter))


def digit_counter(myLabel: object):
    counter = 0

    def digit():
        global counter
        counter += 1
        myLabel.config(text=str(counter))
        myLabel.after(1000, digit)

    digit()


g = Tk()
g.title('Digit Counter')
myLabel = Label(text='', fg='red', font=50)
myLabel.pack()
laps_frame = Frame(g)
laps_frame.pack()
treeview = ttk.Treeview(laps_frame)
treeview['columns'] = 'lap'
treeview.column("#0", width=0,  stretch=NO)
treeview.column("lap", anchor=CENTER, width=80)
treeview.heading("lap", text="Lap", anchor=CENTER)
digit_counter(myLabel)
btn_lap = Button(text='Lap', width=50, command=mark_lap)
btn_lap.pack()
btn_reset = Button(text='Reset', width=50, command=reset_counter)
btn_reset.pack()
btn = Button(text='Terminate', width=50, command=g.destroy)
btn.pack()
g.mainloop()
