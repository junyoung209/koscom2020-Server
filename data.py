import sql as sql_db
import os
import csv

def getdata(idx):
    data = []

    with open('KOSPI200.csv', 'r', encoding='euc-kr') as f:
        reader = csv.reader(f)

        for row in reader:
            temp1 = row[0]

            for i in range(len(row[0]), 6):
                temp1 = '0' + temp1
            row[0] = temp1
            path = './outputs/{0}.png'.format(row[0])

            if os.path.isfile(path):
                ee=sql_db.sql_select2('favorite',idx,row[0])
                if len(ee)==1:
                    if row[3]=='1':
                        temp = {'stock_code': '{0}'.format(row[0]), 'stock_name': '{0}'.format(row[1]),'stock_sector': '{0}'.format(row[2]),'delta':'상승세','price':'{0}'.format(row[4]),'date':'{0}'.format(row[5]),'favorite':'1'}
                    elif row[3]=='2':
                        temp = {'stock_code': '{0}'.format(row[0]), 'stock_name': '{0}'.format(row[1]),
                                'stock_sector': '{0}'.format(row[2]), 'delta': '하락세', 'price': '{0}'.format(row[4]),
                                'date': '{0}'.format(row[5]), 'favorite': '1'}
                    else:
                        temp = {'stock_code': '{0}'.format(row[0]), 'stock_name': '{0}'.format(row[1]),
                                'stock_sector': '{0}'.format(row[2]), 'delta': '-', 'price': '{0}'.format(row[4]),
                                'date': '{0}'.format(row[5]), 'favorite': '1'}
                # ,'weight':'','tag1':'','tag2':''}
                else:
                    if row[3] == '1':
                        temp = {'stock_code': '{0}'.format(row[0]), 'stock_name': '{0}'.format(row[1]),
                                'stock_sector': '{0}'.format(row[2]), 'delta': '상승세', 'price': '{0}'.format(row[4]),
                                'date': '{0}'.format(row[5]), 'favorite': '0'}
                    elif row[3] == '2':
                        temp = {'stock_code': '{0}'.format(row[0]), 'stock_name': '{0}'.format(row[1]),
                                'stock_sector': '{0}'.format(row[2]), 'delta': '하락세', 'price': '{0}'.format(row[4]),
                                'date': '{0}'.format(row[5]), 'favorite': '0'}
                    else:
                        temp = {'stock_code': '{0}'.format(row[0]), 'stock_name': '{0}'.format(row[1]),
                                'stock_sector': '{0}'.format(row[2]), 'delta': '-', 'price': '{0}'.format(row[4]),
                                'date': '{0}'.format(row[5]), 'favorite': '0'}

                data.append(temp)
    return data