from tkinter import *

g = Tk()
g.title('Radio Buttons App')
g.geometry('1000x100+100+100')

v = IntVar()
v.set(2)
t = StringVar()
t.set('...')


def get_radio_button_selected(label: object):
    def radio_button_selected():
        global v, t
        print(v.get())
        if v.get() == 1:
            t.set('Java')
        if v.get() == 2:
            t.set('Python')
        if v.get() == 3:
            t.set('PHP')
        if v.get() == 4:
            t.set('Ruby')

        label.after(250, radio_button_selected)

    radio_button_selected()


Label(text='Computer programming language selection:').grid(column=0, row=0)
label = Label(textvariable=t)
label.grid(column=3, row=0)
get_radio_button_selected(label)
Radiobutton(text='Java', padx=10, pady=10, variable=v, value=1).grid(column=0, row=1)
Radiobutton(text='Python', padx=10, pady=10, variable=v, value=2).grid(column=1, row=1)
Radiobutton(text='PHP', padx=10, pady=10, variable=v, value=3).grid(column=2, row=1)
Radiobutton(text='Ruby', padx=10, pady=10, variable=v, value=4).grid(column=3, row=1)
g.mainloop()