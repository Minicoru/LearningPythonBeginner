from tkinter import *

g = Tk()
g.title('Radio Buttons 2nd App')
g.geometry('400x300+100+100')

v = IntVar()
v.set(1)
Radios = [('Java', 1, 'red'), ('Python', 2, 'green'), ('PHP', 3, 'grey'),
          ('Ruby', 4, 'orange'), ('JavaScript', 5, 'yellow')]
t = StringVar()
t.set(Radios[v.get()][0])
c = StringVar()
c.set(Radios[v.get()][2])


def get_radio_button_selected():
    global v, t, label
    print(v.get())
    for text, index, color in Radios:
        if index == v.get():
            t.set(text)
            c.set(color)
            label.config(bg=color)


Label(text='Computer programming language selection:', width=50).pack(anchor=W)
label = Label(textvariable=t, width=50, pady=20, font=20, bg=c.get())
label.pack(anchor=W)
get_radio_button_selected()


for text, index, color in Radios:
    Radiobutton(text=text, padx=10, pady=10, variable=v, value=index,
                command=get_radio_button_selected, indicatoron=0, width=50).pack(anchor=W)

g.mainloop()
