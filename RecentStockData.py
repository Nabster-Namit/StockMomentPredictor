from nsepy import get_history
from datetime import time
import pandas as pd
import matplotlib.pyplot as plt
import datetime


# defining function to collect stock data
def StockData(stockname):
    today = datetime.date.today()

# using datetime to declare dates with regard to number of days
#     duration = 560
#     start = today+datetime.timedelta(-duration)
    stock_data = get_history(symbol=stockname, start=today, end=today)
    print(stock_data.head())
    # stock_data = stock_data[['Close']]
    stock_data.to_csv('Stockdata_Recent.csv' )
    df = pd.read_csv('Stockdata_Recent' +stockname + '.csv')
    stockdata = df[['Date','Close']]
    return stockdata
StockData('TATAMOTORS')
# print(datetime.date.today()+datetime.timedelta(-200))
