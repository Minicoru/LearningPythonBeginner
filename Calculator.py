from tkinter import *

root = Tk()
root.title('Calculator')

operator = ''
txt_input = StringVar()


import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.total = tk.StringVar()
        self.total.set("0")

        self.entry = tk.Entry(master, textvariable=self.total)
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=10, ipady=10)

        self.create_buttons()

    def create_buttons(self):
        button1 = tk.Button(self.master, text="1", padx=40, pady=20, command=lambda: self.button_click(1))
        button2 = tk.Button(self.master, text="2", padx=40, pady=20, command=lambda: self.button_click(2))
        button3 = tk.Button(self.master, text="3", padx=40, pady=20, command=lambda: self.button_click(3))
        button4 = tk.Button(self.master, text="4", padx=40, pady=20, command=lambda: self.button_click(4))
        button5 = tk.Button(self.master, text="5", padx=40, pady=20, command=lambda: self.button_click(5))
        button6 = tk.Button(self.master, text="6", padx=40, pady=20, command=lambda: self.button_click(6))
        button7 = tk.Button(self.master, text="7", padx=40, pady=20, command=lambda: self.button_click(7))
        button8 = tk.Button(self.master, text="8", padx=40, pady=20, command=lambda: self.button_click(8))
        button9 = tk.Button(self.master, text="9", padx=40, pady=20, command=lambda: self.button_click(9))
        button0 = tk.Button(self.master, text="0", padx=40, pady=20, command=lambda: self.button_click(0))
        button_clear = tk.Button(self.master, text="Clear", padx=79, pady=20, command=self.button_clear)
        button_add = tk.Button(self.master, text="+", padx=39, pady=20, command=lambda: self.button_click("+"))
        button_equal = tk.Button(self.master, text="=", padx=91, pady=20, command=self.button_equal)

        button1.grid(row=1, column=0)
        button2.grid(row=1, column=1)
        button3.grid(row=1, column=2)
        button4.grid(row=2, column=0)
        button5.grid(row=2, column=1)
        button6.grid(row=2, column=2)
        button7.grid(row=3, column=0)
        button8.grid(row=3, column=1)
        button9.grid(row=3, column=2)
        button0.grid(row=4, column=0)
        button_clear.grid(row=4, column=1)
        button_add.grid(row=4, column=2)
        button_equal.grid(row=5, columnspann=3)

    def button_clear(self):

        operator = ''
        self.total.set('')
        self.entry.insert(0, 'Start calculating...')


def calculator():


    def button(numbers):
        global operator
        operator = operator + str(numbers)
        txt_input.set(operator)

    def clear():
        global operator
        operator = ''
        txt_input.set('')
        display.insert(0, 'Start calculating...')

    def equal():
        global operator
        sumup = float(eval(operator))
        txt_input.set(str(sumup))
        operator = ''

    # ====================================
    display = Entry(
        root,
        font=('JetBrains', 30, 'bold'),
        fg='white',
        bg='black',
        justify=RIGHT,
        bd=10,
        textvariable=txt_input
    )
    display.grid(columnspan=4)
    # ====================================
    button_7 = Button(
        root,
        padx=22,
        bd=8,
        fg='grey',
        font=('JetBrains', 30, 'bold'),
        text='7',
        command=lambda: button(7)
    )
    button_7.grid(row=1, column=0, columnspan=1)
    button_8 = Button(
        root,
        padx=22,
        bd=8,
        fg='grey',
        font=('JetBrains', 30, 'bold'),
        text='8',
        command=lambda: button(8)
    )
    button_8.grid(row=1, column=1, columnspan=1)
    button_9 = Button(
        root,
        padx=22,
        bd=8,
        fg='grey',
        font=('JetBrains', 30, 'bold'),
        text='9',
        command=lambda: button(9)
    )
    button_9.grid(row=1, column=2, columnspan=1)
    button_Clear = Button(
        root,
        padx=22,
        bd=8,
        fg='purple',
        bg='black',
        font=('JetBrains', 30, 'bold'),
        text='C',
        command=lambda: clear()
    )
    button_Clear.grid(row=1, column=3, columnspan=1)
    # ====================================
    button_4 = Button(
        root,
        padx=22,
        bd=8,
        fg='grey',
        font=('JetBrains', 30, 'bold'),
        text='4',
        command=lambda: button(4)
    )
    button_4.grid(row=2, column=0, columnspan=1)
    button_5 = Button(
        root,
        padx=22,
        bd=8,
        fg='grey',
        font=('JetBrains', 30, 'bold'),
        text='5',
        command=lambda: button(5)
    )
    button_5.grid(row=2, column=1, columnspan=1)
    button_6 = Button(
        root,
        padx=22,
        bd=8,
        fg='grey',
        font=('JetBrains', 30, 'bold'),
        text='6',
        command=lambda: button(6)
    )
    button_6.grid(row=2, column=2, columnspan=1)
    button_Plus = Button(
        root,
        padx=22,
        bd=8,
        fg='orange',
        bg='black',
        font=('JetBrains', 30, 'bold'),
        text='+',
        command=lambda: button('+')
    )
    button_Plus.grid(row=2, column=3, columnspan=1)
    # ====================================
    button_1 = Button(
        root,
        padx=22,
        bd=8,
        fg='grey',
        font=('JetBrains', 30, 'bold'),
        text='1',
        command=lambda: button(1)
    )
    button_1.grid(row=3, column=0, columnspan=1)
    button_2 = Button(
        root,
        padx=22,
        bd=8,
        fg='grey',
        font=('JetBrains', 30, 'bold'),
        text='2',
        command=lambda: button(2)
    )
    button_2.grid(row=3, column=1, columnspan=1)
    button_3 = Button(
        root,
        padx=22,
        bd=8,
        fg='grey',
        font=('JetBrains', 30, 'bold'),
        text='3',
        command=lambda: button(3)
    )
    button_3.grid(row=3, column=2, columnspan=1)
    button_Minus = Button(
        root,
        padx=27,
        bd=8,
        fg='orange',
        bg='black',
        font=('JetBrains', 30, 'bold'),
        text='-',
        command=lambda: button('-')
    )
    button_Minus.grid(row=3, column=3, columnspan=1)
    # ====================================
    button_Dot = Button(
        root,
        padx=26,
        bd=8,
        fg='orange',
        bg='black',
        font=('JetBrains', 30, 'bold'),
        text='.',
        command=lambda: button('.')
    )
    button_Dot.grid(row=4, column=0, columnspan=1)
    button_0 = Button(
        root,
        padx=22,
        bd=8,
        fg='grey',
        font=('JetBrains', 30, 'bold'),
        text='0',
        command=lambda: button(0)
    )
    button_0.grid(row=4, column=1, columnspan=1)
    button_Div = Button(
        root,
        padx=26,
        bd=8,
        fg='orange',
        bg='black',
        font=('JetBrains', 30, 'bold'),
        text='/',
        command=lambda: button('/')
    )
    button_Div.grid(row=4, column=2, columnspan=1)
    button_Mult = Button(
        root,
        padx=20,
        bd=8,
        fg='orange',
        bg='black',
        font=('JetBrains', 30, 'bold'),
        text='X',
        command=lambda: button('*')
    )
    button_Mult.grid(row=4, column=3, columnspan=1)
    # ====================================
    button_Equ = Button(
        root,
        padx=80,
        bd=8,
        fg='orange',
        bg='black',
        font=('JetBrains', 30, 'bold'),
        text='=',
        command=lambda: equal()
    )
    button_Equ.grid(row=5, column=0, columnspan=2)
    button_Openbrackets = Button(
        root,
        padx=25,
        bd=8,
        fg='orange',
        bg='black',
        font=('JetBrains', 30, 'bold'),
        text='(',
        command=lambda: button('(')
    )
    button_Openbrackets.grid(row=5, column=2, columnspan=1)
    button_Closebrackets = Button(
        root,
        padx=25,
        bd=8,
        fg='orange',
        bg='black',
        font=('JetBrains', 30, 'bold'),
        text=')',
        command=lambda: button(')')
    )
    button_Closebrackets.grid(row=5, column=3, columnspan=1)


if __name__ == '__main__':
    # calculator()
    Calculator(root)
    root.mainloop()
