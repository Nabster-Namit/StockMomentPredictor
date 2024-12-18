from PyQt5 import QtCore, QtGui, QtWidgets
import json
import pandas as pd
import numpy as np
from nltk.stem import WordNetLemmatizer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
import scrapy
import re
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import sys
from pathlib import Path, PureWindowsPath, PurePath, PurePosixPath
from NewsExtraction.NewsExtraction.items import NewsextractionItem
from nsepy import get_history
from datetime import time
import datetime
import os
import time

path = sys.path[0]


# class NewsSpider_tata(scrapy.Spider):
#     name = "tatamotorsnews"
#     start_urls = [
#         'https://www.business-standard.com/company/tata-motors-560/news/1',
#         'https://www.business-standard.com/company/tata-motors-560/news/2',
#         'https://www.business-standard.com/company/tata-motors-560/news/3',
#         'https://www.business-standard.com/company/tata-motors-560/news/4',
#         'https://www.business-standard.com/company/tata-motors-560/news/5',
#         'https://www.business-standard.com/company/tata-motors-560/news/6',
#         'https://www.business-standard.com/company/tata-motors-560/news/7',
#         'https://www.business-standard.com/company/tata-motors-560/news/8',
#         ]
#     def parse(self, response):
# #response.css looks for a particular class and selects it
#         for x in  response.css('div.company-news-listing-txt').getall():
#             # print(x)
#
#             # x = "<div class=\"company-news-listing-txt\">\r\n\t\t\t\t<h2><a href=\"/article/markets/market-live-markets-sensex-nifty-bse-nse-sgx-nifty-rbi-mpc-airtel-120120400135_1.html\" target=\"_blank\">Sensex gains 447 pts, ends at 45,080 as RBI revises FY21 GDP growth outlook</a></h2>\r\n\t\t\t\t<p>4.10 pm\t|\t4 Dec 2020\t|\t<a href=\"javascript:void(0);\">Business Standard</a></p>\r\n\t\t\t\t<p>All that happened in the markets today</p>\r\n\t\t\t</div>"
# #using re to clean html tags
#             x = re.sub("https*\S+", " ", x)
#             x = re.sub("<img src*\S+", " ", x)
#             x = re.sub("class*\S+", " ", x)
#             x = re.sub("height*\S+", " ", x)
#             x = re.sub("width*\S+", " ", x)
#             x = re.sub("alt*\S+", " ", x)
#             x = re.sub("style*\S+", " ", x)
#             x = re.sub("display*\S+", " ", x)
#             x = re.sub("Content\"*\S+", " ", x)
#             x = re.sub("mR5\"", " ", x)
#             x = re.sub("none;*\S+", " ", x)
#             x = re.sub("href=*\S+", " ", x)
#             x = re.sub(">", " ", x)
#             x = re.sub("target=\"*\S+", " ", x)
#             x = re.sub("<div", " ", x)
#             x = re.sub("</div", " ", x)
#             x = re.sub("<h2", " ", x)
#             x = re.sub("</h2", " ", x)
#             x = re.sub("</a", " ", x)
#             x = re.sub(" \r", " ", x)
#             x = re.sub(" \t", " ", x)
#             x = re.sub(" \n", " ", x)
#             x = re.sub("<a", " ", x)
#             x = re.sub("mR5\"", " ", x)
#             # above is new code
#             y = re.split("<p", x)
#             y[0] = re.sub(" \t\t\t\t", " ", y[0])
#             y[0] = re.sub("         ", "", y[0])
#             y[0] = re.sub("    ", "", y[0])
#             y[1] = re.sub("\sStandard  </p", " ", y[1])
#             y[1] = re.sub(" ", "", y[1])
#             y[1] = re.sub("....pm", " ", y[1])
#             y[1] = re.sub(".....pm", " ", y[1])
#             y[1] = re.sub(".....am", " ", y[1])
#             y[1] = re.sub("....am", " ", y[1])
#             y[1] = re.sub("\|", " ", y[1])
#             y[1] = re.sub(" \t", " ", y[1])
#             y[1] = re.sub(" \t", " ", y[1])
#             y[1] = re.sub("\t \t\t", " ", y[1])
#             y[1] = re.sub(" \t", " ", y[1])
#             y[1] = re.sub(" \t\t\t\t", " ", y[1])
#             y[1] = re.sub(" ", "", y[1])
#             y[1] = re.sub("\tTrustofIndia</p\t\t\t\t", "", y[1])
#             y[1] = y[1][-9:]
#             a = re.search("<img src=", y[0])
#             book = NewsextractionItem()
#             today = datetime.date.today()
#             checkdate = pd.to_datetime(y[1])
#             book['Date'] = y[1]
#             book['Headline'] = y[0]
#             # if str(checkdate)[0:10] == today :
#             #     book['date'] = y[1]
#             #     book['headline'] = y[0]
#
#             if a:
#                 pass
#             # print(x)
#             # print(y[0])
#             # print(" \n ", y[1])
#             else:
#                 yield book
#
# class NewsSpider_reliance(scrapy.Spider):
#     name = "reliancenews"
#     start_urls = [
#         'https://www.business-standard.com/company/reliance-industr-476/news/1',
#         'https://www.business-standard.com/company/reliance-industr-476/news/2',
#         'https://www.business-standard.com/company/reliance-industr-476/news/3',
#         'https://www.business-standard.com/company/reliance-industr-476/news/4',
#         'https://www.business-standard.com/company/reliance-industr-476/news/5',
#         'https://www.business-standard.com/company/reliance-industr-476/news/6',
#         'https://www.business-standard.com/company/reliance-industr-476/news/7',
#         'https://www.business-standard.com/company/reliance-industr-476/news/8',
#         'https://www.business-standard.com/company/reliance-industr-476/news/9',
#         'https://www.business-standard.com/company/reliance-industr-476/news/10',
#         'https://www.business-standard.com/company/reliance-industr-476/news/11',
#         'https://www.business-standard.com/company/reliance-industr-476/news/12',
#         'https://www.business-standard.com/company/reliance-industr-476/news/13',
#         'https://www.business-standard.com/company/reliance-industr-476/news/14',
#         'https://www.business-standard.com/company/reliance-industr-476/news/15',
#         'https://www.business-standard.com/company/reliance-industr-476/news/16',
#         'https://www.business-standard.com/company/reliance-industr-476/news/17',
#         'https://www.business-standard.com/company/reliance-industr-476/news/18'
#         ]
#     def parse(self, response):
# #response.css looks for a particular class and selects it
#         for x in  response.css('div.company-news-listing-txt').getall():
#             # print(x)
#
#             # x = "<div class=\"company-news-listing-txt\">\r\n\t\t\t\t<h2><a href=\"/article/markets/market-live-markets-sensex-nifty-bse-nse-sgx-nifty-rbi-mpc-airtel-120120400135_1.html\" target=\"_blank\">Sensex gains 447 pts, ends at 45,080 as RBI revises FY21 GDP growth outlook</a></h2>\r\n\t\t\t\t<p>4.10 pm\t|\t4 Dec 2020\t|\t<a href=\"javascript:void(0);\">Business Standard</a></p>\r\n\t\t\t\t<p>All that happened in the markets today</p>\r\n\t\t\t</div>"
# #using re to clean html tags
#             x = re.sub("https*\S+", " ", x)
#             x = re.sub("<img src*\S+", " ", x)
#             x = re.sub("class*\S+", " ", x)
#             x = re.sub("height*\S+", " ", x)
#             x = re.sub("width*\S+", " ", x)
#             x = re.sub("alt*\S+", " ", x)
#             x = re.sub("style*\S+", " ", x)
#             x = re.sub("display*\S+", " ", x)
#             x = re.sub("Content\"*\S+", " ", x)
#             x = re.sub("mR5\"", " ", x)
#             x = re.sub("none;*\S+", " ", x)
#             x = re.sub("href=*\S+", " ", x)
#             x = re.sub(">", " ", x)
#             x = re.sub("target=\"*\S+", " ", x)
#             x = re.sub("<div", " ", x)
#             x = re.sub("</div", " ", x)
#             x = re.sub("<h2", " ", x)
#             x = re.sub("</h2", " ", x)
#             x = re.sub("</a", " ", x)
#             x = re.sub(" \r", " ", x)
#             x = re.sub(" \t", " ", x)
#             x = re.sub(" \n", " ", x)
#             x = re.sub("<a", " ", x)
#             x = re.sub("mR5\"", " ", x)
#             # above is new code
#             y = re.split("<p", x)
#             y[0] = re.sub(" \t\t\t\t", " ", y[0])
#             y[0] = re.sub("         ", "", y[0])
#             y[0] = re.sub("    ", "", y[0])
#             y[1] = re.sub("\sStandard  </p", " ", y[1])
#             y[1] = re.sub(" ", "", y[1])
#             y[1] = re.sub("....pm", " ", y[1])
#             y[1] = re.sub(".....pm", " ", y[1])
#             y[1] = re.sub(".....am", " ", y[1])
#             y[1] = re.sub("....am", " ", y[1])
#             y[1] = re.sub("\|", " ", y[1])
#             y[1] = re.sub(" \t", " ", y[1])
#             y[1] = re.sub(" \t", " ", y[1])
#             y[1] = re.sub("\t \t\t", " ", y[1])
#             y[1] = re.sub(" \t", " ", y[1])
#             y[1] = re.sub(" \t\t\t\t", " ", y[1])
#             y[1] = re.sub(" ", "", y[1])
#             y[1] = re.sub("\tTrustofIndia</p\t\t\t\t", "", y[1])
#             y[1] = y[1][-9:]
#             a = re.search("<img src=", y[0])
#             book = NewsextractionItem()
#             today = datetime.date.today()
#             checkdate = pd.to_datetime(y[1])
#             book['Date'] = y[1]
#             book['Headline'] = y[0]
#             # if str(checkdate)[0:10] == today:
#             #     book['date'] = y[1]
#             #     book['headline'] = y[0]
#             if a:
#                 pass
#             # print(x)
#             # print(y[0])
#             # print(" \n ", y[1])
#             else:
#                 yield book
#
#
#
#
# #creating main spider
# class NewsSpider_sbi(scrapy.Spider):
#     name = "sbinews"
#     start_urls = [
#         'https://www.business-standard.com/company/st-bk-of-india-1375/news/1',
#         'https://www.business-standard.com/company/st-bk-of-india-1375/news/2',
#         'https://www.business-standard.com/company/st-bk-of-india-1375/news/3',
#         'https://www.business-standard.com/company/st-bk-of-india-1375/news/4',
#         'https://www.business-standard.com/company/st-bk-of-india-1375/news/5',
#         'https://www.business-standard.com/company/st-bk-of-india-1375/news/6',
#         'https://www.business-standard.com/company/st-bk-of-india-1375/news/7',
#         'https://www.business-standard.com/company/st-bk-of-india-1375/news/8',
#         'https://www.business-standard.com/company/st-bk-of-india-1375/news/9',
#         'https://www.business-standard.com/company/st-bk-of-india-1375/news/10',
#
#     ]
#     def parse(self, response):
# #response.css looks for a particular class and selects it
#         for x in  response.css('div.company-news-listing-txt').getall():
#             # print(x)
#
#             # x = "<div class=\"company-news-listing-txt\">\r\n\t\t\t\t<h2><a href=\"/article/markets/market-live-markets-sensex-nifty-bse-nse-sgx-nifty-rbi-mpc-airtel-120120400135_1.html\" target=\"_blank\">Sensex gains 447 pts, ends at 45,080 as RBI revises FY21 GDP growth outlook</a></h2>\r\n\t\t\t\t<p>4.10 pm\t|\t4 Dec 2020\t|\t<a href=\"javascript:void(0);\">Business Standard</a></p>\r\n\t\t\t\t<p>All that happened in the markets today</p>\r\n\t\t\t</div>"
# #using re to clean html tags
#             x = re.sub("https*\S+", " ", x)
#             x = re.sub("<img src*\S+", " ", x)
#             x = re.sub("class*\S+", " ", x)
#             x = re.sub("height*\S+", " ", x)
#             x = re.sub("width*\S+", " ", x)
#             x = re.sub("alt*\S+", " ", x)
#             x = re.sub("style*\S+", " ", x)
#             x = re.sub("display*\S+", " ", x)
#             x = re.sub("Content\"*\S+", " ", x)
#             x = re.sub("mR5\"", " ", x)
#             x = re.sub("none;*\S+", " ", x)
#             x = re.sub("href=*\S+", " ", x)
#             x = re.sub(">", " ", x)
#             x = re.sub("target=\"*\S+", " ", x)
#             x = re.sub("<div", " ", x)
#             x = re.sub("</div", " ", x)
#             x = re.sub("<h2", " ", x)
#             x = re.sub("</h2", " ", x)
#             x = re.sub("</a", " ", x)
#             x = re.sub(" \r", " ", x)
#             x = re.sub(" \t", " ", x)
#             x = re.sub(" \n", " ", x)
#             x = re.sub("<a", " ", x)
#             x = re.sub("mR5\"", " ", x)
#             # above is new code
#             y = re.split("<p", x)
#             y[0] = re.sub(" \t\t\t\t", " ", y[0])
#             y[0] = re.sub("         ", "", y[0])
#             y[0] = re.sub("    ", "", y[0])
#             y[1] = re.sub("\sStandard  </p", " ", y[1])
#             y[1] = re.sub(" ", "", y[1])
#             y[1] = re.sub("....pm", " ", y[1])
#             y[1] = re.sub(".....pm", " ", y[1])
#             y[1] = re.sub(".....am", " ", y[1])
#             y[1] = re.sub("....am", " ", y[1])
#             y[1] = re.sub("\|", " ", y[1])
#             y[1] = re.sub(" \t", " ", y[1])
#             y[1] = re.sub(" \t", " ", y[1])
#             y[1] = re.sub("\t \t\t", " ", y[1])
#             y[1] = re.sub(" \t", " ", y[1])
#             y[1] = re.sub(" \t\t\t\t", " ", y[1])
#             y[1] = re.sub(" ", "", y[1])
#             y[1] = re.sub("\tTrustofIndia</p\t\t\t\t", "", y[1])
#             y[1] = y[1][-9:]
#             a = re.search("<img src=", y[0])
#             book = NewsextractionItem()
#             today = datetime.date.today()
#             checkdate = pd.to_datetime(y[1])
#             book['Date'] = y[1]
#             book['Headline'] = y[0]
#             # if str(checkdate)[0:10] == today:
#             #     book['date'] = y[1]
#             #     book['headline'] = y[0]
#             if a:
#                 pass
#             # print(x)
#             # print(y[0])
#             # print(" \n ", y[1])
#             else:
#                 yield book
#
#
#
#
# #creating main spider
# class NewsSpider_tcs(scrapy.Spider):
#     name = "tcsnews"
#     start_urls = [
#         'https://www.business-standard.com/company/tcs-5400/news/1',
#         'https://www.business-standard.com/company/tcs-5400/news/2',
#         'https://www.business-standard.com/company/tcs-5400/news/3',
#         'https://www.business-standard.com/company/tcs-5400/news/4',
#         'https://www.business-standard.com/company/tcs-5400/news/5',
#         'https://www.business-standard.com/company/tcs-5400/news/6',
#         'https://www.business-standard.com/company/tcs-5400/news/7',
#         'https://www.business-standard.com/company/tcs-5400/news/8',
#         'https://www.business-standard.com/company/tcs-5400/news/9',
#         'https://www.business-standard.com/company/tcs-5400/news/10',
#         'https://www.business-standard.com/company/tcs-5400/news/11',
#
#     ]
#     def parse(self, response):
# #response.css looks for a particular class and selects it
#         for x in  response.css('div.company-news-listing-txt').getall():
#             # print(x)
#
#             # x = "<div class=\"company-news-listing-txt\">\r\n\t\t\t\t<h2><a href=\"/article/markets/market-live-markets-sensex-nifty-bse-nse-sgx-nifty-rbi-mpc-airtel-120120400135_1.html\" target=\"_blank\">Sensex gains 447 pts, ends at 45,080 as RBI revises FY21 GDP growth outlook</a></h2>\r\n\t\t\t\t<p>4.10 pm\t|\t4 Dec 2020\t|\t<a href=\"javascript:void(0);\">Business Standard</a></p>\r\n\t\t\t\t<p>All that happened in the markets today</p>\r\n\t\t\t</div>"
# #using re to clean html tags
#             x = re.sub("https*\S+", " ", x)
#             x = re.sub("<img src*\S+", " ", x)
#             x = re.sub("class*\S+", " ", x)
#             x = re.sub("height*\S+", " ", x)
#             x = re.sub("width*\S+", " ", x)
#             x = re.sub("alt*\S+", " ", x)
#             x = re.sub("style*\S+", " ", x)
#             x = re.sub("display*\S+", " ", x)
#             x = re.sub("Content\"*\S+", " ", x)
#             x = re.sub("mR5\"", " ", x)
#             x = re.sub("none;*\S+", " ", x)
#             x = re.sub("href=*\S+", " ", x)
#             x = re.sub(">", " ", x)
#             x = re.sub("target=\"*\S+", " ", x)
#             x = re.sub("<div", " ", x)
#             x = re.sub("</div", " ", x)
#             x = re.sub("<h2", " ", x)
#             x = re.sub("</h2", " ", x)
#             x = re.sub("</a", " ", x)
#             x = re.sub(" \r", " ", x)
#             x = re.sub(" \t", " ", x)
#             x = re.sub(" \n", " ", x)
#             x = re.sub("<a", " ", x)
#             x = re.sub("mR5\"", " ", x)
#             # above is new code
#             y = re.split("<p", x)
#             y[0] = re.sub(" \t\t\t\t", " ", y[0])
#             y[0] = re.sub("         ", "", y[0])
#             y[0] = re.sub("    ", "", y[0])
#             y[1] = re.sub("\sStandard  </p", " ", y[1])
#             y[1] = re.sub(" ", "", y[1])
#             y[1] = re.sub("....pm", " ", y[1])
#             y[1] = re.sub(".....pm", " ", y[1])
#             y[1] = re.sub(".....am", " ", y[1])
#             y[1] = re.sub("....am", " ", y[1])
#             y[1] = re.sub("\|", " ", y[1])
#             y[1] = re.sub(" \t", " ", y[1])
#             y[1] = re.sub(" \t", " ", y[1])
#             y[1] = re.sub("\t \t\t", " ", y[1])
#             y[1] = re.sub(" \t", " ", y[1])
#             y[1] = re.sub(" \t\t\t\t", " ", y[1])
#             y[1] = re.sub(" ", "", y[1])
#             y[1] = re.sub("\tTrustofIndia</p\t\t\t\t", "", y[1])
#             y[1] = y[1][-9:]
#             a = re.search("<img src=", y[0])
#             book = NewsextractionItem()
#             today = datetime.date.today()
#             checkdate = pd.to_datetime(y[1])
#             book['Date'] = y[1]
#             book['Headline'] = y[0]
#             # if str(checkdate)[0:10] == today:
#             #     book['date'] = y[1]
#             #     book['headline'] = y[0]
#             if a:
#                 pass
#             # print(x)
#             # print(y[0])
#             # print(" \n ", y[1])
#             else:
#                 yield book
#
#
#
# path = sys.path[0]
#
# # print(path)
# # p = Path('items.json')
# # p = Path(path, 'items.json')
# p = 'file:' + path + r'\tatamotorsnews.csv'
# p = r'%s' % p
# # print(p)
# # filepath = r'file:'+path+'items.json'
# # filepath = repr(filepath)
# storage_settings = get_project_settings()
# # print(str(storage_settings))
# storage_settings['FEED_FORMAT'] = 'csv'
# # storage_settings['LOG_LEVEL'] = 'INFO'
# storage_settings['FEED_URI'] = p
# # storage_settings['LOG_FILE'] = 'items.log'
#
# process = CrawlerProcess(storage_settings)
# process.crawl(NewsSpider_tata)
#
# path = sys.path[0]
# # print(path)
# # p = Path('items.json')
# # p = Path(path, 'items.json')
# p = 'file:' + path + '\\reliancenews.csv'
# p = r'%s' % p
# # print(p)
# # filepath = r'file:'+path+'items.json'
# # filepath = repr(filepath)
# storage_settings = get_project_settings()
# print(storage_settings)
# # print(str(storage_settings))
# storage_settings['FEED_FORMAT'] = 'csv'
# # storage_settings['LOG_LEVEL'] = 'INFO'
# storage_settings['FEED_URI'] = p
# # storage_settings['LOG_FILE'] = 'items.log'
# process = CrawlerProcess(storage_settings)
# process.crawl(NewsSpider_reliance)
#
#
# path = sys.path[0]
# # print(path)
# # p = Path('items.json')
# # p = Path(path, 'items.json')
# p = 'file:' + path + '\\sbinews.csv'
# p = r'%s' % p
# # print(p)
# # filepath = r'file:'+path+'items.json'
# # filepath = repr(filepath)
# storage_settings = get_project_settings()
# # print(str(storage_settings))
# storage_settings['FEED_FORMAT'] = 'csv'
# # storage_settings['LOG_LEVEL'] = 'INFO'
# storage_settings['FEED_URI'] = p
# # storage_settings['LOG_FILE'] = 'items.log'
# process = CrawlerProcess(storage_settings)
# process.crawl(NewsSpider_sbi)
#
#
# path = sys.path[0]
# # print(path)
# # p = Path('items.json')
# # p = Path(path, 'items.json')
# p = 'file:' + path + '\\tcsnews.csv'
# p = r'%s' % p
# # print(p)
# # filepath = r'file:'+path+'items.json'
# # filepath = repr(filepath)
# storage_settings = get_project_settings()
# # print(str(storage_settings))
# storage_settings['FEED_FORMAT'] = 'csv'
# # storage_settings['LOG_LEVEL'] = 'INFO'
# storage_settings['FEED_URI'] = p
# # storage_settings['LOG_FILE'] = 'items.log'
# process = CrawlerProcess(storage_settings)
# process.crawl(NewsSpider_tcs)
#
# process.start()

time.sleep(3)
# defining function to collect stock data
def StockData(stockname):
    os.chdir(path)
    today = datetime.date.today()

# using datetime to declare dates with regard to number of days
    duration = 560
    start = today+datetime.timedelta(-duration)
    stock_data = get_history(symbol=stockname, start=start, end=today)
    stock_data.to_csv('Stockdata_' +stockname +'.csv' )
    df = pd.read_csv('Stockdata_'+stockname+'.csv')
    stockdata = df[['Date','Close','Open','Low','High','Volume']]
    return stockdata
StockData('SBIN')
StockData('RELIANCE')
StockData('TATAMOTORS')
StockData('TCS')


class Ui_StockPredictor(object):
    def setupUi(self, StockPredictor):
        StockPredictor.setObjectName("StockPredictor")
        StockPredictor.resize(1628, 719)
        StockPredictor.setWindowTitle("Stock Market")
        StockPredictor.setStyleSheet("background: url(C:/Users/namit/Desktop/TNP IT Project/thumbnail.jpg)")
        self.centralwidget = QtWidgets.QWidget(StockPredictor)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.sbi_button = QtWidgets.QPushButton(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.sbi_button.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.sbi_button.setFont(font)
        self.sbi_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sbi_button.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.sbi_button.setStyleSheet("\n""background: url(C:/Users/namit/Desktop/TNP IT Project/widgetback.png)")
        self.sbi_button.setObjectName("sbi_button")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.sbi_button)
        self.sbi_button.clicked.connect(self.sbi_data)


        self.reliance_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.reliance_button.setFont(font)
        self.reliance_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.reliance_button.setStyleSheet("background: url(C:/Users/namit/Desktop/TNP IT Project/widgetback.png)")
        self.reliance_button.setObjectName("reliance_button")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.reliance_button)
        self.reliance_button.clicked.connect(self.reliance_data)


        self.tata_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tata_button.setFont(font)
        self.tata_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tata_button.setStyleSheet("background: url(C:/Users/namit/Desktop/TNP IT Project/widgetback.png)")
        self.tata_button.setObjectName("tata_button")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.tata_button)
        self.tata_button.clicked.connect(self.tata_data)



        self.tcs_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tcs_button.setFont(font)
        self.tcs_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tcs_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tcs_button.setStyleSheet("background: url(C:/Users/namit/Desktop/TNP IT Project/widgetback.png)")
        self.tcs_button.setObjectName("tcs_button")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.tcs_button)
        self.tcs_button.clicked.connect(self.tcs_data)



        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_8.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Sen")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background: url(C:/Users/namit/Desktop/TNP IT Project/widgettextback.jpg)")
        self.label_8.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.label = QtWidgets.QLabel(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Sen")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background: url(C:/Users/namit/Desktop/TNP IT Project/widgettextback.jpg)")
        self.label.setFrameShape(QtWidgets.QFrame.Panel)
        self.label.setObjectName("label")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit_volume = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_volume.setStyleSheet("background: url(C:/Users/namit/Desktop/TNP IT Project/overview.jpg)")
        self.lineEdit_volume.setObjectName("lineEdit_volume")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.lineEdit_volume)
        self.lineEdit_openprice = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_openprice.setStyleSheet("background: url(C:/Users/namit/Desktop/TNP IT Project/overview.jpg)")
        self.lineEdit_openprice.setObjectName("lineEdit_openprice")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.lineEdit_openprice)
        self.close_edit = QtWidgets.QLabel(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.close_edit.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Sen")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.close_edit.setFont(font)
        self.close_edit.setStyleSheet("background: url(C:/Users/namit/Desktop/TNP IT Project/widgettextback.jpg)")
        self.close_edit.setFrameShape(QtWidgets.QFrame.Panel)
        self.close_edit.setObjectName("close_edit")
        self.formLayout.setWidget(15, QtWidgets.QFormLayout.LabelRole, self.close_edit)
        self.lineEdit_closeprice = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_closeprice.setStyleSheet("background: url(C:/Users/namit/Desktop/TNP IT Project/overview.jpg)")
        self.lineEdit_closeprice.setObjectName("lineEdit_closeprice")
        self.formLayout.setWidget(15, QtWidgets.QFormLayout.FieldRole, self.lineEdit_closeprice)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_5.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Sen")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background: url(C:/Users/namit/Desktop/TNP IT Project/widgettextback.jpg)")
        self.label_5.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(17, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lineEdit_dayshigh = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_dayshigh.setStyleSheet("background: url(C:/Users/namit/Desktop/TNP IT Project/overview.jpg)")
        self.lineEdit_dayshigh.setObjectName("lineEdit_dayshigh")
        self.formLayout.setWidget(17, QtWidgets.QFormLayout.FieldRole, self.lineEdit_dayshigh)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_3.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Sen")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background: url(C:/Users/namit/Desktop/TNP IT Project/widgettextback.jpg)")
        self.label_3.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(19, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_dayslow = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_dayslow.setStyleSheet("background: url(C:/Users/namit/Desktop/TNP IT Project/overview.jpg)")
        self.lineEdit_dayslow.setObjectName("lineEdit_dayslow")
        self.formLayout.setWidget(19, QtWidgets.QFormLayout.FieldRole, self.lineEdit_dayslow)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_6.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Sen")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background: url(C:/Users/namit/Desktop/TNP IT Project/widgettextback.jpg)")
        self.label_6.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(21, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.lineEdit_prediction = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_prediction.setStyleSheet("background: url(C:/Users/namit/Desktop/TNP IT Project/overview.jpg)")
        self.lineEdit_prediction.setObjectName("lineEdit_prediction")
        self.formLayout.setWidget(21, QtWidgets.QFormLayout.FieldRole, self.lineEdit_prediction)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_4.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Sen")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background: url(C:/Users/namit/Desktop/TNP IT Project/widgettextback.jpg)")
        self.label_4.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(23, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_accuracy = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_accuracy.setStyleSheet("background: url(C:/Users/namit/Desktop/TNP IT Project/overview.jpg)")
        self.lineEdit_accuracy.setObjectName("lineEdit_accuracy")
        self.formLayout.setWidget(23, QtWidgets.QFormLayout.FieldRole, self.lineEdit_accuracy)
        self.lineEdit_date = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_date.setMinimumSize(QtCore.QSize(100, 0))
        self.lineEdit_date.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_date.setStyleSheet("background: url(C:/Users/namit/Desktop/TNP IT Project/overview.jpg)")
        self.lineEdit_date.setObjectName("lineEdit_date")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.lineEdit_date)
        self.open_edit = QtWidgets.QLabel(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.open_edit.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Sen")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.open_edit.setFont(font)
        self.open_edit.setStyleSheet("background: url(C:/Users/namit/Desktop/TNP IT Project/widgettextback.jpg)")
        self.open_edit.setFrameShape(QtWidgets.QFrame.Panel)
        self.open_edit.setObjectName("open_edit")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.LabelRole, self.open_edit)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.label_7.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Poiret One")
        font.setPointSize(72)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background: url(C:/Users/namit/Desktop/TNP IT Project/widgettextback.jpg)")
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_7)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(111, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_2.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Sigmar One")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background: url(C:/Users/namit/Desktop/TNP IT Project/widgettextback.jpg)")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.label_2)
        StockPredictor.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(StockPredictor)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1628, 26))
        self.menubar.setObjectName("menubar")
        StockPredictor.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(StockPredictor)
        self.statusbar.setObjectName("statusbar")
        StockPredictor.setStatusBar(self.statusbar)


        self.retranslateUi(StockPredictor)
        QtCore.QMetaObject.connectSlotsByName(StockPredictor)




    def retranslateUi(self, StockPredictor):
        _translate = QtCore.QCoreApplication.translate
        StockPredictor.setWindowTitle(_translate("StockPredictor", "Stock Predictor"))
        self.sbi_button.setToolTip(_translate("StockPredictor", "<html><head/><body><p>SBI</p></body></html>"))
        self.sbi_button.setWhatsThis(_translate("StockPredictor", "<html><head/><body><p align=\"center\">SBI</p></body></html>"))
        self.sbi_button.setText(_translate("StockPredictor", "SBI"))
        self.reliance_button.setText(_translate("StockPredictor", "RELIANCE"))
        self.tata_button.setText(_translate("StockPredictor", "TATA MOTORS"))
        self.tcs_button.setText(_translate("StockPredictor", "TCS"))
        self.label_8.setText(_translate("StockPredictor", "Date:"))
        self.label.setText(_translate("StockPredictor", "Volume:"))
        self.close_edit.setText(_translate("StockPredictor", "Close:"))
        self.label_5.setText(_translate("StockPredictor", "Day\'s High:"))
        self.label_3.setText(_translate("StockPredictor", "Day\'s Low:"))
        self.label_6.setText(_translate("StockPredictor", "Prediction:"))
        self.label_4.setText(_translate("StockPredictor", "Accuracy:"))
        self.open_edit.setText(_translate("StockPredictor", "Open:"))
        self.label_7.setText(_translate("StockPredictor", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600; color:#aaffff;\">Listed Stocks</span></p></body></html>"))
        self.label_2.setText(_translate("StockPredictor", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Overview</span></p></body></html>"))

    def sbi_data(self):
        p_news = path + r'\sbinews.csv'
        p_news = r'%s' % p_news
        p_data = path + r'\Stockdata_SBIN.csv'
        p_data = r'%s' %p_data
        data1 = pd.read_csv(p_news)
        data = data1.drop_duplicates(subset='Headline', inplace=True)
        data.to_csv(p_news)
        data['Date'] = pd.to_datetime(data.Date)
        data.sort_values(by='Date', inplace=True)
        data.reset_index(drop=True, inplace=True)
        data = data.groupby('Date')['Headline'].apply(''.join).reset_index()
        stock_data = pd.read_csv(p_data)
        data.set_index('Date', inplace=True)
        stock_data.set_index('Date', inplace=True)
        data = pd.merge(data, stock_data, right_index=True, left_index=True, how='inner')

        new_words = {'falls': -9, 'drops': -9, 'rise': 9, 'increases': 9, 'gain': 9, 'hiked': -9, 'dips': -9,
                     'declines': -9,
                     'decline': -9, 'hikes': -9, 'jumps': 9, 'lose': -9, 'profit': 9, 'loss': -9, 'shreds': -9,
                     'sell': -9, 'buy': 9,
                     'recession': -9, 'rupee weakens': -9, 'record low': -9, 'record high': 9, 'sensex up': 9,
                     'sensex gains': 9,
                     'nifty down': -9, 'sensex down': -9, 'sensex drops': -9, 'nifty up': 9, 'sensex slumps': -9,
                     'recovers': 9, 'low': -9, 'strong debut': 9, 'setback': -9, 'slips': -9, 'climbs': 9, 'above': 9,
                     'to invest': 9}

        compound = []
        SIA = 0

        for i in range(0, len(data)):
            sia = SentimentIntensityAnalyzer()
            sia.lexicon.update(new_words)
            sentiment = sia.polarity_scores(data['Headline'][i])
            SIA = sentiment
            compound.append(SIA['compound'])

        data['Compound'] = compound
        sentiment = []
        for i in range(0, len(data)):
            if data['Compound'][i] > 0:
                sentiment.append('Positive')
            elif data['Compound'][i] < 0:
                sentiment.append('Negative')
            else:
                sentiment.append('Neutral')

        data['Sentiment'] = sentiment
        self.lineEdit_prediction.setText(data['Sentiment'][-1])

        data['Headline'] = data['Headline'].str.lower()

        ##removing apostrophe
        data['Headline'].replace("'s", "", regex=True, inplace=True)

        ##removing punctuations and special characters
        data['Headline'].replace("[^a-zA-Z]", " ", regex=True, inplace=True)

        ##Lemmatization
        lemmatizer = WordNetLemmatizer()
        data['Headline'] = data['Headline'].apply(
            lambda x: ' '.join([lemmatizer.lemmatize(word) for word in str(x).split()]))

        vectorizer = TfidfVectorizer()
        x = vectorizer.fit_transform(data['Headline'])

        df1 = pd.DataFrame(x.toarray(), columns=vectorizer.get_feature_names())

        self.lineEdit_date.setText(str(data.index[-1].date()))
        self.lineEdit_openprice.setText(str(data['Open'][-1]))
        self.lineEdit_dayshigh.setText(str(data['High'][-1]))
        self.lineEdit_dayslow.setText(str(data['Low'][-1]))
        self.lineEdit_closeprice.setText(str(data['Close'][-1]))
        self.lineEdit_volume.setText(str(data['Volume'][-1]))

        data.drop(
            ['Headline', 'Compound', '%Deliverble', 'Symbol', 'High', 'Low', 'Open', 'Deliverable Volume', 'Volume',
             'VWAP', 'Turnover', 'Trades', 'Last', 'Prev Close', 'Symbol', 'Series'], inplace=True, axis=1)
        data.reset_index(drop=True, inplace=True)
        print(data.head())

        scaler = MinMaxScaler()
        scaled = scaler.fit_transform(data[['Close']])

        data_scaled = pd.DataFrame(scaled, columns=['Close'])
        df_1 = df1.join(data_scaled)

        encoder = LabelEncoder()
        encode = encoder.fit_transform(data['Sentiment'])

        y = pd.DataFrame(encode, columns=['sentiment'])

        X_train, X_test, y_train, y_test = train_test_split(df_1, y['sentiment'], test_size=0.2, random_state=0)

        gnb = GaussianNB()
        gnb.fit(X_train, y_train)

        predict = gnb.predict(X_test)

        accuracy = accuracy_score(predict, y_test)
        self.lineEdit_accuracy.setText(str(accuracy))

    def reliance_data(self):
        p_news = path + r'\reliancenews.csv'
        p_news = r'%s' % p_news
        p_data = path + r'\Stockdata_RELIANCE.csv'
        p_data = r'%s' % p_data
        data = pd.read_csv(p_news)
        data.drop_duplicates(subset='Headline', inplace=True)
        data['Date'] = pd.to_datetime(data.Date)
        data.sort_values(by='Date', inplace=True)
        data.reset_index(drop=True, inplace=True)
        data = data.groupby('Date')['Headline'].apply(''.join).reset_index()
        stock_data = pd.read_csv(p_data)
        data.set_index('Date', inplace=True)
        stock_data.set_index('Date', inplace=True)
        data = pd.merge(data, stock_data, right_index=True, left_index=True, how='inner')

        new_words = {'falls': -9, 'drops': -9, 'rise': 9, 'increases': 9, 'gain': 9, 'hiked': -9, 'dips': -9,
                     'declines': -9,
                     'decline': -9, 'hikes': -9, 'jumps': 9, 'lose': -9, 'profit': 9, 'loss': -9, 'shreds': -9,
                     'sell': -9, 'buy': 9,
                     'recession': -9, 'rupee weakens': -9, 'record low': -9, 'record high': 9, 'sensex up': 9,
                     'sensex gains': 9,
                     'nifty down': -9, 'sensex down': -9, 'sensex drops': -9, 'nifty up': 9, 'sensex slumps': -9,
                     'recovers': 9, 'low': -9, 'strong debut': 9, 'setback': -9, 'slips': -9, 'climbs': 9, 'above': 9,
                     'to invest': 9}

        compound = []
        SIA = 0

        for i in range(0, len(data)):
            sia = SentimentIntensityAnalyzer()
            sia.lexicon.update(new_words)
            sentiment = sia.polarity_scores(data['Headline'][i])
            SIA = sentiment
            compound.append(SIA['compound'])

        data['Compound'] = compound
        sentiment = []
        for i in range(0, len(data)):
            if data['Compound'][i] > 0:
                sentiment.append('Positive')
            elif data['Compound'][i] < 0:
                sentiment.append('Negative')
            else:
                sentiment.append('Neutral')

        data['Sentiment'] = sentiment
        self.lineEdit_prediction.setText(data['Sentiment'][-1])

        data['Headline'] = data['Headline'].str.lower()

        ##removing apostrophe
        data['Headline'].replace("'s", "", regex=True, inplace=True)

        ##removing punctuations and special characters
        data['Headline'].replace("[^a-zA-Z]", " ", regex=True, inplace=True)

        ##Lemmatization
        lemmatizer = WordNetLemmatizer()
        data['Headline'] = data['Headline'].apply(
            lambda x: ' '.join([lemmatizer.lemmatize(word) for word in str(x).split()]))

        vectorizer = TfidfVectorizer()
        x = vectorizer.fit_transform(data['Headline'])

        df1 = pd.DataFrame(x.toarray(), columns=vectorizer.get_feature_names())

        self.lineEdit_date.setText(str(data.index[-1].date()))
        self.lineEdit_openprice.setText(str(data['Open'][-1]))
        self.lineEdit_dayshigh.setText(str(data['High'][-1]))
        self.lineEdit_dayslow.setText(str(data['Low'][-1]))
        self.lineEdit_closeprice.setText(str(data['Close'][-1]))
        self.lineEdit_volume.setText(str(data['Volume'][-1]))

        data.drop(
            ['Headline', 'Compound', '%Deliverble', 'Symbol', 'High', 'Low', 'Open', 'Deliverable Volume', 'Volume',
             'VWAP', 'Turnover', 'Trades', 'Last', 'Prev Close', 'Symbol', 'Series'], inplace=True, axis=1)
        data.reset_index(drop=True, inplace=True)
        print(data.head())

        scaler = MinMaxScaler()
        scaled = scaler.fit_transform(data[['Close']])

        data_scaled = pd.DataFrame(scaled, columns=['Close'])
        df_1 = df1.join(data_scaled)

        encoder = LabelEncoder()
        encode = encoder.fit_transform(data['Sentiment'])

        y = pd.DataFrame(encode, columns=['sentiment'])

        X_train, X_test, y_train, y_test = train_test_split(df_1, y['sentiment'], test_size=0.2, random_state=0)

        gnb = GaussianNB()
        gnb.fit(X_train, y_train)

        predict = gnb.predict(X_test)

        accuracy = accuracy_score(predict, y_test)
        self.lineEdit_accuracy.setText(str(accuracy))

    def tata_data(self):
        p_news = path + r'\tatamotorsnews.csv'
        p_news = r'%s' % p_news
        p_data = path + r'\Stockdata_TATAMOTORS.csv'
        p_data = r'%s' % p_data
        data = pd.read_csv(p_news)
        data.drop_duplicates(subset='Headline', inplace=True)
        data['Date'] = pd.to_datetime(data.Date)
        data.sort_values(by='Date', inplace=True)
        data.reset_index(drop=True, inplace=True)
        data = data.groupby('Date')['Headline'].apply(''.join).reset_index()
        stock_data = pd.read_csv(p_data)
        data.set_index('Date', inplace=True)
        stock_data.set_index('Date', inplace=True)
        data = pd.merge(data, stock_data, right_index=True, left_index=True, how='inner')

        new_words = {'falls': -9, 'drops': -9, 'rise': 9, 'increases': 9, 'gain': 9, 'hiked': -9, 'dips': -9,
                     'declines': -9,
                     'decline': -9, 'hikes': -9, 'jumps': 9, 'lose': -9, 'profit': 9, 'loss': -9, 'shreds': -9,
                     'sell': -9, 'buy': 9,
                     'recession': -9, 'rupee weakens': -9, 'record low': -9, 'record high': 9, 'sensex up': 9,
                     'sensex gains': 9,
                     'nifty down': -9, 'sensex down': -9, 'sensex drops': -9, 'nifty up': 9, 'sensex slumps': -9,
                     'recovers': 9, 'low': -9, 'strong debut': 9, 'setback': -9, 'slips': -9, 'climbs': 9, 'above': 9,
                     'to invest': 9}

        compound = []
        SIA = 0

        for i in range(0, len(data)):
            sia = SentimentIntensityAnalyzer()
            sia.lexicon.update(new_words)
            sentiment = sia.polarity_scores(data['Headline'][i])
            SIA = sentiment
            compound.append(SIA['compound'])

        data['Compound'] = compound
        sentiment = []
        for i in range(0, len(data)):
            if data['Compound'][i] > 0:
                sentiment.append('Positive')
            elif data['Compound'][i] < 0:
                sentiment.append('Negative')
            else:
                sentiment.append('Neutral')

        data['Sentiment'] = sentiment
        self.lineEdit_prediction.setText(data['Sentiment'][-1])

        data['Headline'] = data['Headline'].str.lower()

        ##removing apostrophe
        data['Headline'].replace("'s", "", regex=True, inplace=True)

        ##removing punctuations and special characters
        data['Headline'].replace("[^a-zA-Z]", " ", regex=True, inplace=True)

        ##Lemmatization
        lemmatizer = WordNetLemmatizer()
        data['Headline'] = data['Headline'].apply(
            lambda x: ' '.join([lemmatizer.lemmatize(word) for word in str(x).split()]))

        vectorizer = TfidfVectorizer()
        x = vectorizer.fit_transform(data['Headline'])

        df1 = pd.DataFrame(x.toarray(), columns=vectorizer.get_feature_names())

        self.lineEdit_date.setText(str(data.index[-1].date()))
        self.lineEdit_openprice.setText(str(data['Open'][-1]))
        self.lineEdit_dayshigh.setText(str(data['High'][-1]))
        self.lineEdit_dayslow.setText(str(data['Low'][-1]))
        self.lineEdit_closeprice.setText(str(data['Close'][-1]))
        self.lineEdit_volume.setText(str(data['Volume'][-1]))

        data.drop(
            ['Headline', 'Compound', '%Deliverble', 'Symbol', 'High', 'Low', 'Open', 'Deliverable Volume', 'Volume',
             'VWAP', 'Turnover', 'Trades', 'Last', 'Prev Close', 'Symbol', 'Series'], inplace=True, axis=1)
        data.reset_index(drop=True, inplace=True)
        print(data.head())

        scaler = MinMaxScaler()
        scaled = scaler.fit_transform(data[['Close']])

        data_scaled = pd.DataFrame(scaled, columns=['Close'])
        df_1 = df1.join(data_scaled)

        encoder = LabelEncoder()
        encode = encoder.fit_transform(data['Sentiment'])

        y = pd.DataFrame(encode, columns=['sentiment'])

        X_train, X_test, y_train, y_test = train_test_split(df_1, y['sentiment'], test_size=0.2, random_state=0)

        gnb = GaussianNB()
        gnb.fit(X_train, y_train)

        predict = gnb.predict(X_test)

        accuracy = accuracy_score(predict, y_test)
        self.lineEdit_accuracy.setText(str(accuracy))

    def tcs_data(self):
        p = path + r'\tcsnews.csv'
        p = r'%s' % p
        data = pd.read_csv(
            r'C:\Users\namit\PycharmProjects\StockMarket\venv\NewsExtraction\NewsExtraction\spiders\tcsnews.csv')
        data.drop_duplicates(subset='Headline', inplace=True)
        data.drop_duplicates(subset='Headline', inplace=True)
        data['Date'] = pd.to_datetime(data.Date)
        data.sort_values(by='Date', inplace=True)
        data.reset_index(drop=True, inplace=True)
        data = data.groupby('Date')['Headline'].apply(''.join).reset_index()
        stock_data = pd.read_csv(r'C:\Users\namit\PycharmProjects\StockMarket\Stockdata_TCS.csv')
        data.set_index('Date', inplace=True)
        stock_data.set_index('Date', inplace=True)
        data = pd.merge(data, stock_data, right_index=True, left_index=True, how='inner')

        new_words = {'falls': -9, 'drops': -9, 'rise': 9, 'increases': 9, 'gain': 9, 'hiked': -9, 'dips': -9,
                     'declines': -9,
                     'decline': -9, 'hikes': -9, 'jumps': 9, 'lose': -9, 'profit': 9, 'loss': -9, 'shreds': -9,
                     'sell': -9, 'buy': 9,
                     'recession': -9, 'rupee weakens': -9, 'record low': -9, 'record high': 9, 'sensex up': 9,
                     'sensex gains': 9,
                     'nifty down': -9, 'sensex down': -9, 'sensex drops': -9, 'nifty up': 9, 'sensex slumps': -9,
                     'recovers': 9, 'low': -9, 'strong debut': 9, 'setback': -9, 'slips': -9, 'climbs': 9, 'above': 9,
                     'to invest': 9}

        compound = []
        SIA = 0

        for i in range(0, len(data)):
            sia = SentimentIntensityAnalyzer()
            sia.lexicon.update(new_words)
            sentiment = sia.polarity_scores(data['Headline'][i])
            SIA = sentiment
            compound.append(SIA['compound'])

        data['Compound'] = compound
        sentiment = []
        for i in range(0, len(data)):
            if data['Compound'][i] > 0:
                sentiment.append('Positive')
            elif data['Compound'][i] < 0:
                sentiment.append('Negative')
            else:
                sentiment.append('Neutral')

        data['Sentiment'] = sentiment
        self.lineEdit_prediction.setText(data['Sentiment'][-1])

        data['Headline'] = data['Headline'].str.lower()

        ##removing apostrophe
        data['Headline'].replace("'s", "", regex=True, inplace=True)

        ##removing punctuations and special characters
        data['Headline'].replace("[^a-zA-Z]", " ", regex=True, inplace=True)

        ##Lemmatization
        lemmatizer = WordNetLemmatizer()
        data['Headline'] = data['Headline'].apply(
            lambda x: ' '.join([lemmatizer.lemmatize(word) for word in str(x).split()]))

        vectorizer = TfidfVectorizer()
        x = vectorizer.fit_transform(data['Headline'])

        df1 = pd.DataFrame(x.toarray(), columns=vectorizer.get_feature_names())

        self.lineEdit_date.setText(str(data.index[-1].date()))
        self.lineEdit_openprice.setText(str(data['Open'][-1]))
        self.lineEdit_dayshigh.setText(str(data['High'][-1]))
        self.lineEdit_dayslow.setText(str(data['Low'][-1]))
        self.lineEdit_closeprice.setText(str(data['Close'][-1]))
        self.lineEdit_volume.setText(str(data['Volume'][-1]))
        data.drop(
            ['Headline', 'Compound', '%Deliverble', 'Symbol', 'High', 'Low', 'Open', 'Deliverable Volume', 'Volume',
             'VWAP', 'Turnover', 'Trades', 'Last', 'Prev Close', 'Symbol', 'Series'], inplace=True, axis=1)
        data.reset_index(drop=True, inplace=True)

        scaler = MinMaxScaler()
        scaled = scaler.fit_transform(data[['Close']])

        data_scaled = pd.DataFrame(scaled, columns=['Close'])
        df_1 = df1.join(data_scaled)

        encoder = LabelEncoder()
        encode = encoder.fit_transform(data['Sentiment'])

        y = pd.DataFrame(encode, columns=['sentiment'])

        X_train, X_test, y_train, y_test = train_test_split(df_1, y['sentiment'], test_size=0.2, random_state=0)

        gnb = GaussianNB()
        gnb.fit(X_train, y_train)

        predict = gnb.predict(X_test)

        accuracy = accuracy_score(predict, y_test)
        self.lineEdit_accuracy.setText(str(accuracy))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StockPredictor = QtWidgets.QMainWindow()
    ui = Ui_StockPredictor()
    ui.setupUi(StockPredictor)
    StockPredictor.show()
    sys.exit(app.exec_())

