import FF as sample


import pandas as pd
import json
import requests
import csv

import os
# url = 'https://sandbox-apigw.koscom.co.kr/v2/market/stocks/kospi/lists?apikey=l7xx6d1170cf582f47989e72d402d832a210'
# data = requests.get(url).json()
# a=list(data['isuLists'])
# stock=[]
# for i in range(len(a)):
#     temp=[]
#     temp.append(a[i]['isuSrtCd'])
#     temp.append(a[i]['isuKorNm'])
#     stock.append(temp)
# print(len(stock))
#
#
#

stock_list=[]
f=open('KOSPI200.csv','r')
reader=csv.reader(f)
for row in reader:
    temp=row[0]
    for i in range(len(row[0]),6):
        temp='0'+temp
    row[0]=temp
    stock_list.append(row)

f_result = open('KOSPI200_result.csv', 'w', encoding = 'euc-kr', newline = '')
writer = csv.writer(f_result)
for i in range(1):#in range(len(stock_list)):
    direction, end_price = sample.save_img(stock_list[i][0])
    writer.writerow([stock_list[i][0], stock_list[i][1], direction, end_price])
f_result.close()
