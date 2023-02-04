from tkinter import *
from tkinter.filedialog import *

g = Tk()



def file_dialog():
    file_opened = askopenfile()
    file_readed = file_opened.name
    file = open(file_readed)
    my_label = Label(text=file_opened.name)
    my_label.pack()
    my_string_var = StringVar()
    my_string_var.set(file.read())
    my_entry = Entry(textvariable=my_string_var, width=50)
    my_entry.pack()
    # my_text = Label(text=file.read(), width=50)
    # my_text.pack()


btn = Button(text='Open file', width=50, command=file_dialog)
btn.pack()

g.mainloop()
