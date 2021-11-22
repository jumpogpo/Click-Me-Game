from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Click Me Game')
root.geometry('300x200')

Amount = 0

def ClickButtonFunction():
    global Amount
    Amount += 1
    ClickAmount.configure(text='Score: ' + str("{:,}".format(Amount)))

ClickButton = Button(root, text='Click Me!', fg='Black', bg='White', command=ClickButtonFunction, font=50)
ClickAmount = Label(root, text='Score: 0', fg='Black', font=10)

ClickButton.place(x=109, y=50)
ClickAmount.place(x=90, y=110)

root.resizable(False, False)
root.wm_attributes("-transparentcolor", 'grey')
root.mainloop()