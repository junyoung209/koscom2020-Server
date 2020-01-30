import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import time

from fbprophet import Prophet
from selenium.webdriver.common.action_chains import ActionChains
pd.core.common.is_list_like = pd.api.types.is_list_like
from pandas_datareader.data import DataReader
from datetime import date # Date & time functionality
# from pandas_datareader.google.daily import GoogleDailyReader
from pandas_datareader._utils import RemoteDataError
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/mangal.ttf").get_name()
rc('font', family=font_name)

from fbprophet.diagnostics import cross_validation

def save_img(stock_code):
    start = date(2017, 1, 2)  # Default: Jan 1, 2010
    end = date(2019, 1, 29)  # Default: today
    # ticker = stock_code+'.KS'
    ticker = stock_code+'.KS'

    data_source = 'yahoo'
    bias = 0
    end_price = 0
    try:
        try:
            stock_data = DataReader(ticker, data_source, start, end)
        except :
            return 0, 0
        stock_data = stock_data['2017-01-02': '2019-01-29']
        df = pd.DataFrame({'ds': stock_data.index, 'y': stock_data['Adj Close']}).reset_index()
        df = df.drop('Date', axis=1)    

        start = date(2017, 1, 2)  # Default: Jan 1, 2010
        end = date(2020, 1, 29)  # Default: today
        stock_data_current = DataReader(ticker, data_source, start, end)
        stock_data_current = stock_data_current['2017-01-02' : '2020-01-29']
        df_ = pd.DataFrame({'ds': stock_data_current.index, 'y': stock_data_current['Adj Close']}).reset_index()
        df_ = df_.drop('Date', axis=1)   

        m = Prophet(weekly_seasonality=False, yearly_seasonality=True)
        m_ = Prophet(weekly_seasonality=False, yearly_seasonality=True)
        flag = 1
        try :
            m.fit(df)
            m_.fit(df_)
        except :
            flag = 0
            pass

        if flag :
            future = m.make_future_dataframe(periods=365)
            future_ = m_.make_future_dataframe(periods=365)
            # 미래의 어느 시점까지 예측을 할 것인지
            forecast = m.predict(future)
            forecast_ = m_.predict(future_)
            print(forecast)

            fig = m.plot(forecast)
            fig_ = m_.plot(forecast_)
            #plt.savefig('./outputs/' + stock_code + '_past'+'.png')

            plt.axvline(x=forecast['ds'][500], color = 'green', linestyle='--')
            plt.plot(forecast_['ds'], forecast_['yhat'], label = 'current')
            plt.plot(forecast['ds'], forecast['yhat'], color = 'red', label = 'past')
            plt.legend()

            plt.savefig('./outputs/' + stock_code +'.png')

            y0 = y1 = 0.0
            for i in range(len(forecast)):
                if(forecast['ds'][i].strftime('%y-%m-%d') == '17-01-02'):
                    y0 = forecast['yhat'][i]
                if(forecast['ds'][i].strftime('%y-%m-%d') == '19-01-28'):
                    end_price = df['y'][i]
                    print(i)
                if(forecast['ds'][i].strftime('%y-%m-%d') == '20-01-28'):
                    y1 = forecast['yhat'][i]

            if  y1 > y0 :
                if (y1 - y0) / y0 > 0.1 :
                    bias = 1    # up
            else :
                if (y0 - y1) / y0 > 0.1 : 
                    bias = 2    # down
    except RemoteDataError:
        pass
    
    return bias, end_price

