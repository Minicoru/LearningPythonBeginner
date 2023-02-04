from tkinter import *

g = Tk()
g.title('Checkbox App')
g.geometry('300x200')

valuesStates = []


def save_state():
    globals()
    # print((cbValue1.get(), cbValue2.get(), cbValue3.get(), cbValue4.get(), cbValue5.get()))
    valuesStates.append((cbValue1.get(), cbValue2.get(), cbValue3.get(), cbValue4.get(), cbValue5.get()))
    print(valuesStates[len(valuesStates)-1])


cbValue1 = IntVar()
cb1 = Checkbutton(text='Java', variable=cbValue1, command=save_state)
cb1.grid(row=1, column=0, sticky=W)
cbValue2 = IntVar()
cb2 = Checkbutton(text='Python', variable=cbValue2, command=save_state)
cb2.grid(row=2, column=0, sticky=W)
cbValue3 = IntVar()
cb3 = Checkbutton(text='PHP', variable=cbValue3, command=save_state)
cb3.grid(row=3, column=0, sticky=W)
cbValue4 = IntVar()
cb4 = Checkbutton(text='Ruby', variable=cbValue4, command=save_state)
cb4.grid(row=4, column=0, sticky=W)
cbValue5 = IntVar()
cb5 = Checkbutton(text='JavaScript', variable=cbValue5, command=save_state)
cb5.grid(row=5, column=0, sticky=W)


g.mainloop()
