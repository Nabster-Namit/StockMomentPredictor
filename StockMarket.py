from nsepy import get_history
from datetime import time
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import sys
import os
print('namit')

# defining function to collect stock data
def StockData(stockname):
    today = datetime.date.today()

    # using datetime to declare dates with regard to number of days
    duration = 560
    start = today + datetime.timedelta(-duration)
    stock_data = get_history(symbol=stockname, start=start, end=today)
    stock_data.to_csv('Stockdata_' + stockname + '.csv')
    df = pd.read_csv('Stockdata_' + stockname + '.csv')
    stockdata = df[['Date', 'Close', 'Open', 'Low', 'High', 'Volume']]
    print(df.head())
    return stockdata
StockData('SBIN')
StockData('RELIANCE')
StockData('TATAMOTORS')
StockData('TCS')
# p = path + r'\reliancenews.csv'
# p = r'%s' % p
path = sys.path[0]
print(path)


