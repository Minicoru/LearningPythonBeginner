from tkinter import *

root = Tk()
root.title('Calculator')

operator = ''
txt_input = StringVar()

def calculator():


    def btn(numbers):
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
    btn7 = Button(
        root,
        padx=22,
        bd=8,
        fg='grey',
        font=('JetBrains', 30, 'bold'),
        text='7',
        command=lambda: btn(7)
    )
    btn7.grid(row=1, column=0, columnspan=1)
    btn8 = Button(
        root,
        padx=22,
        bd=8,
        fg='grey',
        font=('JetBrains', 30, 'bold'),
        text='8',
        command=lambda: btn(8)
    )
    btn8.grid(row=1, column=1, columnspan=1)
    btn9 = Button(
        root,
        padx=22,
        bd=8,
        fg='grey',
        font=('JetBrains', 30, 'bold'),
        text='9',
        command=lambda: btn(9)
    )
    btn9.grid(row=1, column=2, columnspan=1)
    btnClear = Button(
        root,
        padx=22,
        bd=8,
        fg='purple',
        bg='black',
        font=('JetBrains', 30, 'bold'),
        text='C',
        command=lambda: clear()
    )
    btnClear.grid(row=1, column=3, columnspan=1)
    # ====================================
    btn4 = Button(
        root,
        padx=22,
        bd=8,
        fg='grey',
        font=('JetBrains', 30, 'bold'),
        text='4',
        command=lambda: btn(4)
    )
    btn4.grid(row=2, column=0, columnspan=1)
    btn5 = Button(
        root,
        padx=22,
        bd=8,
        fg='grey',
        font=('JetBrains', 30, 'bold'),
        text='5',
        command=lambda: btn(5)
    )
    btn5.grid(row=2, column=1, columnspan=1)
    btn6 = Button(
        root,
        padx=22,
        bd=8,
        fg='grey',
        font=('JetBrains', 30, 'bold'),
        text='6',
        command=lambda: btn(6)
    )
    btn6.grid(row=2, column=2, columnspan=1)
    btnPlus = Button(
        root,
        padx=22,
        bd=8,
        fg='orange',
        bg='black',
        font=('JetBrains', 30, 'bold'),
        text='+',
        command=lambda: btn('+')
    )
    btnPlus.grid(row=2, column=3, columnspan=1)
    # ====================================
    btn1 = Button(
        root,
        padx=22,
        bd=8,
        fg='grey',
        font=('JetBrains', 30, 'bold'),
        text='1',
        command=lambda: btn(1)
    )
    btn1.grid(row=3, column=0, columnspan=1)
    btn2 = Button(
        root,
        padx=22,
        bd=8,
        fg='grey',
        font=('JetBrains', 30, 'bold'),
        text='2',
        command=lambda: btn(2)
    )
    btn2.grid(row=3, column=1, columnspan=1)
    btn3 = Button(
        root,
        padx=22,
        bd=8,
        fg='grey',
        font=('JetBrains', 30, 'bold'),
        text='3',
        command=lambda: btn(3)
    )
    btn3.grid(row=3, column=2, columnspan=1)
    btnMinus = Button(
        root,
        padx=27,
        bd=8,
        fg='orange',
        bg='black',
        font=('JetBrains', 30, 'bold'),
        text='-',
        command=lambda: btn('-')
    )
    btnMinus.grid(row=3, column=3, columnspan=1)
    # ====================================
    btnDot = Button(
        root,
        padx=26,
        bd=8,
        fg='orange',
        bg='black',
        font=('JetBrains', 30, 'bold'),
        text='.',
        command=lambda: btn('.')
    )
    btnDot.grid(row=4, column=0, columnspan=1)
    btn0 = Button(
        root,
        padx=22,
        bd=8,
        fg='grey',
        font=('JetBrains', 30, 'bold'),
        text='0',
        command=lambda: btn(0)
    )
    btn0.grid(row=4, column=1, columnspan=1)
    btnDiv = Button(
        root,
        padx=26,
        bd=8,
        fg='orange',
        bg='black',
        font=('JetBrains', 30, 'bold'),
        text='/',
        command=lambda: btn('/')
    )
    btnDiv.grid(row=4, column=2, columnspan=1)
    btnMult = Button(
        root,
        padx=20,
        bd=8,
        fg='orange',
        bg='black',
        font=('JetBrains', 30, 'bold'),
        text='X',
        command=lambda: btn('*')
    )
    btnMult.grid(row=4, column=3, columnspan=1)
    # ====================================
    btnEqu = Button(
        root,
        padx=80,
        bd=8,
        fg='orange',
        bg='black',
        font=('JetBrains', 30, 'bold'),
        text='=',
        command=lambda: equal()
    )
    btnEqu.grid(row=5, column=0, columnspan=2)
    btnOpenbrackets = Button(
        root,
        padx=25,
        bd=8,
        fg='orange',
        bg='black',
        font=('JetBrains', 30, 'bold'),
        text='(',
        command=lambda: btn('(')
    )
    btnOpenbrackets.grid(row=5, column=2, columnspan=1)
    btnClosebrackets = Button(
        root,
        padx=25,
        bd=8,
        fg='orange',
        bg='black',
        font=('JetBrains', 30, 'bold'),
        text=')',
        command=lambda: btn(')')
    )
    btnClosebrackets.grid(row=5, column=3, columnspan=1)


if __name__ == '__main__':
    calculator()
    root.mainloop()
