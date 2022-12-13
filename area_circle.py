from tkinter import *
root=Tk()
root.title('magnus')
root.geometry('500x400+0+0')

mylabel=Label(root,text='radius',font=20).grid(row=0,column=0)
radius=IntVar()
et1=Entry(root,width=30,font=20,textvariable=radius)
et1.grid(row=0,column=1)
mylabel=Label(root,text='area',font=20).grid(row=1,sticky=W)
et2=Entry(root,width=30,font=20)
et2.grid(row=1,column=1)

def calculate():
    r=radius.get()
    area=3.14*(r**2)
    et2.insert(0,round(area,2))

def ce():
    et1.delete(0,END)
    et2.delete(0,END)    

btn1=Button(root,text='calculate',command=calculate).grid(row=2,column=1)
btn2=Button(root,text='ce',command=ce).grid(row=3,column=1)



root.mainloop()