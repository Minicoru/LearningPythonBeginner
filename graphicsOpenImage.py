from tkinter import *

root = Tk()
root.title('Showing image')

photo = PhotoImage(file='Image.png')
myLabel = Label(root, image=photo)
myLabel.pack()

root.mainloop()