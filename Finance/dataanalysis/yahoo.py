import pandas as pd
import pandas_datareader.data as web
import datetime


start = datetime.datetime(2017,1,1)
end = datetime.date.today()

apple = web.DataReader('F-F_Research_Data_factors','famafrench')  
type(apple)

