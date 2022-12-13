from tkinter import *
root=Tk()
root.geometry('500x400')
txt=StringVar()
mytext=Entry(root,textvariable=txt).pack()
def magnus(txt):
    if txt=='magnus':
        Label(root,text='Yes').pack()
btn1=Button(root,text='search',command=lambda:magnus(txt.get())).pack()
root.mainloop()