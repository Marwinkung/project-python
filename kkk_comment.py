
# plt.style.use('fivethirtyeight')

# start_date='2021-11-05'
# end_date='2022-11-05'

# a=input('enter product: ').upper()

# df=web.DataReader(a,data_source='yahoo',start=start_date,end=end_date)
# print(df)

# plt.figure(figsize=(12.2,4.5))
# plt.title('Close Price',fontsize=18)
# plt.plot(df['Close'])
# plt.xlabel('Date',fontsize=18)
# plt.ylabel('Close Price',fontsize=18)
# plt.show()

# ShortEMA=df.Close.ewm(span=5,adjust=False).mean()
# MiddleEMA=df.Close.ewm(span=21,adjust=False).mean()
# LongEMA=df.Close.ewm(span=63,adjust=False).mean()

# plt.figure(figsize=(15,6))
# plt.title('Close Price',fontsize=18)
# plt.plot(df['Close'],label='Close Price',color='black',alpha=0.6)
# plt.plot(ShortEMA,label='Short/Fast EMA',color='yellow',linestyle='dashed',alpha=0.7)
# plt.plot(MiddleEMA,label='Middle/Medium EMA',color='orange',linestyle='dashed',alpha=0.7)
# plt.plot(LongEMA,label='Long/Slow EMA',color='brown',linestyle='dashed',alpha=0.7)
# plt.xlabel('Date',fontsize=18)
# plt.ylabel('Close Price',fontsize=18)
# plt.legend(loc='best')
# plt.show()

# df['ShortEMA']=ShortEMA
# df['MiddleEMA']=MiddleEMA
# df['LongEMA']=LongEMA
# print(df)

# def buy_sell_function(data):
#     buy_list=[]
#     sell_list=[]
#     flag_short=False
#     flag_long=False

#     for i in range(0,len(data)):
#         if data['MiddleEMA'][i]<data['LongEMA'][i] and data['ShortEMA'][i]<data['MiddleEMA'][i] and flag_long==False and flag_short==False:
#             buy_list.append(data['Close'][i])
#             sell_list.append(np.nan)
#             flag_short=True
#         elif flag_short==True and data['ShortEMA'][i]>data['MiddleEMA'][i]:
#             sell_list.append(data['Close'][i])
#             buy_list.append(np.nan)
#             flag_short=False
#         elif data['MiddleEMA'][i]>data['LongEMA'][i] and data['ShortEMA'][i]>data['MiddleEMA'][i] and flag_long== False:
#             buy_list.append(data['Close'][i])
#             sell_list.append(np.nan)
#             flag_long=True
#         elif flag_long==True and data['ShortEMA'][i]<data['MiddleEMA'][i]:
#             sell_list.append(data['Close'][i])
#             buy_list.append(np.nan)
#             flag_long=False
#         else:
#             buy_list.append(np.nan)
#             sell_list.append(np.nan)
#     return (buy_list,sell_list)             


# df['Buy']=buy_sell_function(df)[1]
# df['Sell']=buy_sell_function(df)[0]

# plt.figure(figsize=(15,6))
# plt.title('Buy and Sell Plot',fontsize=18)
# plt.plot(df['Close'],label='Close Price',color='black',alpha=0.4)
# plt.plot(ShortEMA,label='Short/Fast EMA',color='yellow',linestyle='dashed',alpha=0.5)
# plt.plot(MiddleEMA,label='Middle/Medium EMA',color='orange',linestyle='dashed',alpha=0.5)
# plt.plot(LongEMA,label='Long/Slow EMA',color='brown',linestyle='dashed',alpha=0.5)
# plt.scatter(df.index,df['Buy'],color='green',marker='^',s=(12*12),alpha=1)
# plt.scatter(df.index,df['Sell'],color='red',marker='v',s=(12*12),alpha=1)
# plt.xlabel('Date',fontsize=18)
# plt.ylabel('Close Price',fontsize=18)
# plt.legend(loc='best')
# plt.show()
