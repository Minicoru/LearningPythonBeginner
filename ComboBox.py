from tkinter import *
from tkinter import ttk

root = Tk()
root.title('ComboBox app')

combobox_selection = StringVar(value='Choose a fruit')
counter = IntVar(value=0)


def show_selection():
    globals()
    counter.set(counter.get() + 1)
    if combobox_selection.get() != 'Choose a fruit':
        ttk.Label(text=combobox_selection.get()).grid(row=counter.get(), column=1)


combobox = ttk.Combobox(width=25, textvariable=combobox_selection)
combobox['values'] = ('Apple', 'Orange', 'Mango', 'Cashew', 'Papaya', 'Melon')
combobox.grid(row=0, column=1)

ttk.Label(text='Select your fruit').grid(row=0, column=0)
ttk.Button(text='Show Selection', command=show_selection).grid(row=1, column=0)

root.mainloop()
