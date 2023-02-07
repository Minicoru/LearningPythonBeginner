from tkinter import *

root = Tk()
root.title('Calculator')


def calculator():
    # ====================================
    display = Entry(
        root,
        font=('JetBrains', 30, 'bold'),
        fg='white',
        bg='black',
        justify=RIGHT,
        bd=10
    )
    display.grid(columnspan=4)
    # ====================================
    btn7 = Button(
        root,
        padx=22,
        bd=8,
        fg='grey',
        font=('JetBrains', 30, 'bold'),
        text='7'
    )
    btn7.grid(row=1, column=0, columnspan=1)
    btn8 = Button(
        root,
        padx=22,
        bd=8,
        fg='grey',
        font=('JetBrains', 30, 'bold'),
        text='8'
    )
    btn8.grid(row=1, column=1, columnspan=1)
    btn9 = Button(
        root,
        padx=22,
        bd=8,
        fg='grey',
        font=('JetBrains', 30, 'bold'),
        text='9'
    )
    btn9.grid(row=1, column=2, columnspan=1)
    btnClear = Button(
        root,
        padx=22,
        bd=8,
        fg='purple',
        bg='black',
        font=('JetBrains', 30, 'bold'),
        text='C'
    )
    btnClear.grid(row=1, column=3, columnspan=1)
    # ====================================
    btn4 = Button(
        root,
        padx=22,
        bd=8,
        fg='grey',
        font=('JetBrains', 30, 'bold'),
        text='4'
    )
    btn4.grid(row=2, column=0, columnspan=1)
    btn5 = Button(
        root,
        padx=22,
        bd=8,
        fg='grey',
        font=('JetBrains', 30, 'bold'),
        text='5'
    )
    btn5.grid(row=2, column=1, columnspan=1)
    btn6 = Button(
        root,
        padx=22,
        bd=8,
        fg='grey',
        font=('JetBrains', 30, 'bold'),
        text='6'
    )
    btn6.grid(row=2, column=2, columnspan=1)
    btnPlus = Button(
        root,
        padx=22,
        bd=8,
        fg='orange',
        bg='black',
        font=('JetBrains', 30, 'bold'),
        text='+'
    )
    btnPlus.grid(row=2, column=3, columnspan=1)
    # ====================================
    btn1 = Button(
        root,
        padx=22,
        bd=8,
        fg='grey',
        font=('JetBrains', 30, 'bold'),
        text='1'
    )
    btn1.grid(row=3, column=0, columnspan=1)
    btn2 = Button(
        root,
        padx=22,
        bd=8,
        fg='grey',
        font=('JetBrains', 30, 'bold'),
        text='2'
    )
    btn2.grid(row=3, column=1, columnspan=1)
    btn3 = Button(
        root,
        padx=22,
        bd=8,
        fg='grey',
        font=('JetBrains', 30, 'bold'),
        text='3'
    )
    btn3.grid(row=3, column=2, columnspan=1)
    btnMinus = Button(
        root,
        padx=27,
        bd=8,
        fg='orange',
        bg='black',
        font=('JetBrains', 30, 'bold'),
        text='-'
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
        text='.'
    )
    btnDot.grid(row=4, column=0, columnspan=1)
    btn0 = Button(
        root,
        padx=22,
        bd=8,
        fg='grey',
        font=('JetBrains', 30, 'bold'),
        text='0'
    )
    btn0.grid(row=4, column=1, columnspan=1)
    btnDiv = Button(
        root,
        padx=26,
        bd=8,
        fg='orange',
        bg='black',
        font=('JetBrains', 30, 'bold'),
        text='/'
    )
    btnDiv.grid(row=4, column=2, columnspan=1)
    btnMult = Button(
        root,
        padx=20,
        bd=8,
        fg='orange',
        bg='black',
        font=('JetBrains', 30, 'bold'),
        text='X'
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
        text='='
    )
    btnEqu.grid(row=5, column=0, columnspan=2)
    btnOpenbrackets = Button(
        root,
        padx=25,
        bd=8,
        fg='orange',
        bg='black',
        font=('JetBrains', 30, 'bold'),
        text='('
    )
    btnOpenbrackets.grid(row=5, column=2, columnspan=1)
    btnClosebrackets = Button(
        root,
        padx=25,
        bd=8,
        fg='orange',
        bg='black',
        font=('JetBrains', 30, 'bold'),
        text=')'
    )
    btnClosebrackets.grid(row=5, column=3, columnspan=1)


if __name__ == '__main__':
    calculator()
    root.mainloop()
