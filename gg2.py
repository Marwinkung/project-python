from tkinter import *
import tkinter.messagebox
import pandas as p
from tkinter import ttk

root=Tk()
root.title('magnus')
root.geometry('500x400+0+0')


# def showchoice1():
#     choice=language.get()
#     if choice==1:
#         tkinter.messagebox.showinfo('เเจ้งเตือน','a')
#     elif choice==2:
#         tkinter.messagebox.showinfo('เเจ้งเตือน','b')  
#     elif choice==3:
#         tkinter.messagebox.showinfo('เเจ้งเตือน','c')     
#     else:
#         tkinter.messagebox.showinfo('เเจ้งเตือน','d')     
            
# language=IntVar()
# Radiobutton(text='Python',variable=language,value=1,command=showchoice1).grid(row=0,column=0)
# Radiobutton(text='Java',variable=language,value=2,command=showchoice1).grid(row=0,column=1)
# Radiobutton(text='PHP',variable=language,value=3,command=showchoice1).grid(row=0,column=2)
# Radiobutton(text='C#',variable=language,value=4,command=showchoice1).grid(row=0,column=3)

# def showchoice1():
#     choice1=language1.get()
#     choice2=language2.get()
#     choice3=language3.get()
#     choice4=language4.get()
#     if choice1==1:
#         Label(root,text='เลือก python').pack(anchor=W)
#     if choice2==1:
#         Label(root,text='เลือก Java').pack(anchor=W)
#     if choice3==1:
#         Label(root,text='เลือก PHP').pack(anchor=W)
#     if choice4==1:
#         Label(root,text='เลือก C#').pack(anchor=W)        




# language1=IntVar()
# Checkbutton(text='Python',variable=language1).pack(anchor=W)
# language2=IntVar()
# Checkbutton(text='Java',variable=language2).pack(anchor=W)
# language3=IntVar()
# Checkbutton(text='PHP',variable=language3).pack(anchor=W)
# language4=IntVar()
# Checkbutton(text='C#',variable=language4).pack(anchor=W)

# btn1=Button(root,text='เลือก',command=showchoice1).pack(anchor=W)
# def delete():
#     et1.delete(0,END)
#     et2.delete(0,END)
#     et3.delete(0,END)




# Label(text='ชื่อ').grid(row=0)
# Label(text='นามสกุล').grid(row=1)
# Label(text='อายุ').grid(row=2)

# et1=Entry(font=30)
# et1.grid(row=0,column=1)
# et1.insert(0,'magnus')
# et2=Entry()
# et2.grid(row=1,column=1)
# et2.insert(0,'carlsen')
# et3=Entry()
# et3.grid(row=2,column=1)
# et3.insert(0,'30')

# btn2=Button(text='ล้างข้อมูล',command=delete).grid(row=3,column=2)

# root.mainloop()

Label(text='จังหวัด',font=20).grid(row=0,column=0)
choice=StringVar(value='เลือกจังหวัดของคุณ')
combo=ttk.Combobox(textvariable=choice)
combo['values']=('กรุงเทพ','เชียงใหม่','กระบี่')
combo.grid(row=0,column=1)

def selectCity():
    Label(text='คุณเลือก '+choice.get()).grid(row=2,column=0)
btn=Button(text='ส่งข้อมูล',command=selectCity)
btn.grid(row=1,column=1)
root.mainloop()    