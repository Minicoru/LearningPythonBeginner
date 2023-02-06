from tkinter import *

appMemory = {
    'entries': [{
        'label': {'text': 'Radius'},
        'entry': {}
    }, {
        'label': {'text': 'Area'},
        'entry': {}
    }],
    'in': [],
    'records': []
}


def form1():
    globals()
    config = {
        'padx': 10,
        'pady': 2,
        'width': 10
    }
    radius = IntVar()
    area = IntVar()

    def clear():
        globals()
        area.set(0)
        radius.set(0)

    def calculate():
        globals()
        area.set(3.142 * radius.get() * radius.get())

        # for entry in appMemory.get('entries'):

    label = Label(text='Radius', width=config.get('width'))
    label.pack(padx=config.get('padx'), pady=config.get('pady'))
    entry = Entry(width=config.get('width'), textvariable=radius)
    entry.pack(padx=config.get('padx'), pady=config.get('pady'))
    label = Label(text='Area', width=config.get('width'))
    label.pack(padx=config.get('padx'), pady=config.get('pady'))
    entry = Entry(width=config.get('width'), textvariable=area)
    entry.pack(padx=config.get('padx'), pady=config.get('pady'))

    Button(text='Calculate', command=calculate).pack(padx=config.get('padx'), pady=config.get('pady'))
    Button(text='Clear', command=clear).pack(padx=config.get('padx'), pady=config.get('pady'))


root = Tk()
root.title("Entries test.")

form1()
for widget in root.children:
    print(widget)

root.mainloop()
