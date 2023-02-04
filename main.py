# Libraries
import tkinter
from tkinter import *
from tkinter import messagebox
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


g = Tk()
# g_alt = Tk()

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def gui():  # Function to define the GUI to use.
    g.title('G (MW)')
    g.geometry('1260x720+100+100')

    chooser = Menu()

    item_file = Menu()
    item_file.add_command(label='New project', command=addWindow)
    item_file.add_command(label='Save', command=saved)
    item_file.add_separator()
    item_file_options = Menu()
    item_file_options_gender = Menu()
    for text, key in [('Male', 'm'), ('Female', 'f'), ('They', 't')]:
        item_file_options_gender.add_radiobutton(label=text, value=key)
    item_file_options.add_cascade(label='F.Gender', menu=item_file_options_gender)
    item_file.add_cascade(
        label='Options',
        menu=item_file_options
    )
    item_file.add_separator()
    item_file.add_command(label='Open')
    item_file.add_command(label='Close',command=close)

    item_edit = Menu()
    item_edit.add_command(label='Copy')
    item_edit.add_command(label='Cut')
    item_edit.add_command(label='Paste')
    item_edit.add_command(label='Delete')

    item_navigate = Menu()
    item_code = Menu()
    item_run = Menu()
    item_tools = Menu()
    item_help = Menu()


    chooser.add_cascade(label='File', menu=item_file)
    chooser.add_cascade(label='Edit', menu=item_edit)
    chooser.add_cascade(label='Navigate', menu=item_navigate)
    chooser.add_cascade(label='Code', menu=item_code)
    chooser.add_cascade(label='Run', menu=item_run)
    chooser.add_cascade(label='Tools', menu=item_tools)
    chooser.add_cascade(label='Help', menu=item_help)

    g.config(menu=chooser)
    # g_alt.title('G (MW Alternative)')
    # g_alt.geometry('1260x720+500+500')
    fields()
    g.mainloop()
    # g_alt.mainloop()


def fields():  # Function to eet fields for gui Function
    Label(text='Pack Label').pack()
    Label(text='Place Label').pack()  # .place(x=200, y=200)
    Label(text='Grid Label').pack()  # .grid(row=10, column=10, sticky='E')
    Button(text='Try me b*#!@#', command=addTextLabel).pack()
    Button(text='Try me b*#!@# 2 (tha...)', command=addWindow).pack()


def addTextLabel():
    Label(text="Add new label").pack()


def addWindow():
    newWindow = Tk()
    newWindow.title('New Window from G.')
    newWindow.geometry('1260x720+400+400')
    newWindow.mainloop()


def saved():
    messagebox.showinfo('', 'Project saved, please continue...')


def close():
    choice = messagebox.askquestion('','Are you sure to close the proyect?')
    if (choice=='yes'):
        messagebox.showinfo('', 'Closing proyect...')
        g.destroy()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    gui()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
