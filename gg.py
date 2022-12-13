from tkinter import *
import tkinter.messagebox
from tkinter.colorchooser import *
from tkinter.filedialog import *
root=Tk()
root.title('magnus')
root.geometry('500x400+0+0')

g=''

#ใส่ข้อความในหน้าจอ
# mylabel1=Label(root,text='a',fg='red',font=20,bg='yellow').pack()
# mylabel2=Label(root,text='b',fg='green',font=20).place(x=250,y=200)
# mylabel1=Label(root,text='a',fg='red',font=20,bg='yellow').grid(row=0,column=0)
# mylabel2=Label(root,text='b',fg='green',font=20).grid(row=0,column=1)
# mylabel3=Label(root,text='c',fg='blue',font=20).grid(row=2,column=0)
def showMessage():
    message=txt.get()
    Label(root,text=message,fg='red',font=20,bg='yellow').pack()
def openwindow():
    #สร้างหน้าต่างเพิ่ม
    root2=Tk()
    root2.title('รายงานผล')
    root2.geometry('300x200')
    Label(root2,text='asdf',fg='red',font=20,bg='yellow')    
def aboutprogram():
    tkinter.messagebox.showinfo('รายละเอียดโปรเเกรม','ผู้พัฒนาโปรเเกรม')    
def exitprogram():
    confirm=tkinter.messagebox.askquestion('ยืนยัน','คุณต้องการปิดโปรเเกรมหรือไม่ ?')
    if confirm =='yes':
        root.destroy()    
def selectcolor():
    color=askcolor()        
    Mylabel=Label(root,text='sadf',bg=color[1]).pack()
def selectfile():
    # fileopen=askopenfile()
    # mylaBel=Label(text=fileopen).pack()
    filename=askopenfilename()
    filecontent=open(filename,encoding='cp874')
    mylabel=Label(text=filecontent.read()).pack()


#ใส่ปุ่ม
btn1=Button(root,text='magnus',fg='black',bg='red',command=showMessage).pack()
btn2=Button(root,text='เปิดรายงาน',fg='black',bg='red',command=openwindow).pack()

#กล่องข้อความ
txt=StringVar()
mytext=Entry(root,textvariable=txt).pack()
k=txt.get()
#สร้างเมนู
myMenu=Menu()
root.config(menu=myMenu)


#เพิ่มเมนูย่อย
menuitem=Menu()
menuitem.add_command(label='New file',command=openwindow)#ใช้command
menuitem.add_command(label='Open file')
menuitem.add_command(label='Save')
menuitem.add_command(label='Save as')
menuitem.add_command(label='about',command=aboutprogram)
menuitem.add_command(label='Exit',command=exitprogram)



#เพิ่มเมนูหลัก
myMenu.add_cascade(label='Menu1',menu=menuitem)
myMenu.add_cascade(label='Menu2')
myMenu.add_cascade(label='Menu3')

#เลือกสี
btn3=Button(root,text='เลือกสี',command=selectcolor).pack()

#เลือกไฟล์
btn4=Button(root,text='เลือกไฟล์',command=selectfile).pack()

root.mainloop()
