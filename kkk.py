import numpy as np
import pandas_datareader as web
import matplotlib.pyplot as plt
from tkinter import *
import tkinter.messagebox
from tkinter import ttk

class magnus:
    def __init__(self):
        root=Tk()
        root.title('Finance')
        self.root=root
    def normal(self,a1,a2,a3,b1,b2,b3,p1):
        try:
            start_date=a3.get()+'-'+a2.get()+'-'+a1.get()
            end_date=b3.get()+'-'+b2.get()+'-'+b1.get()
            print(start_date)
            print(end_date)
            df=web.DataReader(p1.get(),data_source='yahoo',start=start_date,end=end_date)

            print('magnus')
            ShortEMA=df.Close.ewm(span=5,adjust=False).mean()
            MiddleEMA=df.Close.ewm(span=21,adjust=False).mean()
            LongEMA=df.Close.ewm(span=63,adjust=False).mean()

            df['ShortEMA']=ShortEMA
            df['MiddleEMA']=MiddleEMA
            df['LongEMA']=LongEMA

           
            return df
        except:
            tkinter.messagebox.showerror('Remind','Error')
            exit(-1)
        
    def show_graph(self,a1,a2,a3,b1,b2,b3,p1):
        df=self.normal(a1,a2,a3,b1,b2,b3,p1)
        plt.style.use('fivethirtyeight')
        plt.figure(figsize=(12.2,4.5))
        plt.title('Close Price',fontsize=18)
        plt.plot(df['Close'])
        plt.xlabel('Date',fontsize=18)
        plt.ylabel('Close Price',fontsize=18)
        plt.show()
        
    def show_graph_EMA(self,a1,a2,a3,b1,b2,b3,p1):
        df=self.normal(a1,a2,a3,b1,b2,b3,p1)
        
        plt.figure(figsize=(15,6))
        plt.title('Close Price',fontsize=18)
        plt.plot(df['Close'],label='Close Price',color='black',alpha=0.6)
        plt.plot(df['ShortEMA'],label='Short/Fast EMA',color='yellow',linestyle='dashed',alpha=0.7)
        plt.plot(df['MiddleEMA'],label='Middle/Medium EMA',color='orange',linestyle='dashed',alpha=0.7)
        plt.plot(df['LongEMA'],label='Long/Slow EMA',color='brown',linestyle='dashed',alpha=0.7)
        plt.xlabel('Date',fontsize=18)
        plt.ylabel('Close Price',fontsize=18)
        plt.legend(loc='best')
        plt.show()

      
    def buy_sell(self,a1,a2,a3,b1,b2,b3,p1):
        df=self.normal(a1,a2,a3,b1,b2,b3,p1)
        buy_list=[]
        sell_list=[]
        flag_short=False
        flag_long=False

        for i in range(0,len(df)):
            if df['MiddleEMA'][i]<df['LongEMA'][i] and df['ShortEMA'][i]<df['MiddleEMA'][i] and flag_long==False and flag_short==False:
                buy_list.append(df['Close'][i])
                sell_list.append(np.nan)
                flag_short=True
            elif flag_short==True and df['ShortEMA'][i]>df['MiddleEMA'][i]:
                sell_list.append(df['Close'][i])
                buy_list.append(np.nan)
                flag_short=False
            elif df['MiddleEMA'][i]>df['LongEMA'][i] and df['ShortEMA'][i]>df['MiddleEMA'][i] and flag_long== False:
                buy_list.append(df['Close'][i])
                sell_list.append(np.nan)
                flag_long=True
            elif flag_long==True and df['ShortEMA'][i]<df['MiddleEMA'][i]:
                sell_list.append(df['Close'][i])
                buy_list.append(np.nan)
                flag_long=False
            else:
                buy_list.append(np.nan)
                sell_list.append(np.nan)
                  


        df['Buy']=sell_list
        df['Sell']=buy_list
        
      
        print(df.index)
        plt.figure(figsize=(15,6))
        plt.title('Buy and Sell Plot',fontsize=18)
        plt.plot(df['Close'],label='Close Price',color='black',alpha=0.4)
        plt.plot(df['ShortEMA'],label='Short/Fast EMA',color='yellow',linestyle='dashed',alpha=0.5)
        plt.plot(df['MiddleEMA'],label='Middle/Medium EMA',color='orange',linestyle='dashed',alpha=0.5)
        plt.plot(df['LongEMA'],label='Long/Slow EMA',color='brown',linestyle='dashed',alpha=0.5)
        plt.scatter(df.index,df['Buy'],color='green',marker='^',s=(12*12),alpha=1)
        plt.scatter(df.index,df['Sell'],color='red',marker='v',s=(12*12),alpha=1)
        plt.xlabel('Date',fontsize=18)
        plt.ylabel('Close Price',fontsize=18)
        plt.legend(loc='best')
        plt.show()

    def gui(self):
        day=[i for i in range(1,32)]
        month=[i for i in range(1,13)]
        year=[i for i in range(1990,2023)]
        Label(self.root,text='Start Date').grid(row=0,column=0,sticky=W)
        day_s=StringVar(value='day')
        a1=ttk.Combobox(self.root,width=10,textvariable=day_s)
        a1['values']=tuple(day)
        a1.grid(row=0,column=1)
        month_s=StringVar(value='month')
        a2=ttk.Combobox(self.root,width=10,textvariable=month_s)
        a2['values']=tuple(month)
        a2.grid(row=0,column=2)
        year_s=StringVar(value='year')
        a3=ttk.Combobox(self.root,width=10,textvariable=year_s)
        a3['values']=tuple(year)
        a3.grid(row=0,column=3)

        Label(self.root,text='End Date').grid(row=1,column=0,sticky=W)
        day_e=StringVar(value='day')
        b1=ttk.Combobox(self.root,width=10,textvariable=day_e)
        b1['values']=day
        b1.grid(row=1,column=1)
        month_e=StringVar(value='month')
        b2=ttk.Combobox(self.root,width=10,textvariable=month_e)
        b2['values']=month
        b2.grid(row=1,column=2)
        year_e=StringVar(value='year')
        b3=ttk.Combobox(self.root,width=10,textvariable=year_e)
        b3['values']=year
        b3.grid(row=1,column=3)

        Label(self.root,text='Product').grid(row=2,column=0,sticky=W)
        p1=StringVar()        
        Entry(self.root,textvariable=p1,width=10,bg='yellow').grid(row=2,column=1)
        
        btn1=Button(self.root,text='Show graph',bg='blue',command=lambda:self.show_graph(a1,a2,a3,b1,b2,b3,p1)).grid(row=3,column=0)
        btn2=Button(self.root,text='Show graph EMA',bg='red',command=lambda:self.show_graph_EMA(a1,a2,a3,b1,b2,b3,p1)).grid(row=3,column=1)
        btn3=Button(self.root,text='Point buy sell',bg='green',command=lambda:self.buy_sell(a1,a2,a3,b1,b2,b3,p1)).grid(row=3,column=2)
        self.root.mainloop()

a=magnus()
a.gui()






