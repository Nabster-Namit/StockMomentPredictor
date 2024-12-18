import nsepy

import datetime
import pandas as pd
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




data = pd.read_csv(
    r'C:\Users\namit\PycharmProjects\StockMarket\venv\NewsExtraction\NewsExtraction\spiders\reliancenews.csv')
data.drop_duplicates(subset='Headline', inplace=True)
data['Date'] = pd.to_datetime(data.Date)
data.sort_values(by='Date', inplace=True)
data.reset_index(drop=True, inplace=True)
data = data.groupby('Date')['Headline'].apply(''.join).reset_index()
stock_data = pd.read_csv(r'C:\Users\namit\PycharmProjects\StockMarket\Stockdata_RELIANCE.csv')
data.set_index('Date', inplace=True)
stock_data.set_index('Date', inplace=True)
data = pd.merge(data, stock_data, right_index=True, left_index=True, how='inner')

new_words = {'falls': -9, 'drops': -9, 'rise': 9, 'increases': 9, 'gain': 9, 'hiked': -9, 'dips': -9, 'declines': -9,
             'decline': -9, 'hikes': -9, 'jumps': 9, 'lose': -9, 'profit': 9, 'loss': -9, 'shreds': -9, 'sell': -9,
             'buy': 9,
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
# self.lineEdit_prediction.setText(data['Sentiment'][-1])

data['Headline'] = data['Headline'].str.lower()

##removing apostrophe
data['Headline'].replace("'s", "", regex=True, inplace=True)

##removing punctuations and special characters
data['Headline'].replace("[^a-zA-Z]", " ", regex=True, inplace=True)

##Lemmatization
lemmatizer = WordNetLemmatizer()
data['Headline'] = data['Headline'].apply(lambda x: ' '.join([lemmatizer.lemmatize(word) for word in str(x).split()]))

vectorizer = TfidfVectorizer()
x = vectorizer.fit_transform(data['Headline'])

df1 = pd.DataFrame(x.toarray(), columns=vectorizer.get_feature_names())
#
# self.lineEdit_date.setText(str(data.index[-1].date()))
# self.lineEdit_openprice.setText(str(data['Open'][-1]))
# self.lineEdit_dayshigh.setText(str(data['High'][-1]))
# self.lineEdit_dayslow.setText(str(data['Low'][-1]))
# self.lineEdit_closeprice.setText(str(data['Close'][-1]))
# self.lineEdit_volume.setText(str(data['Volume'][-1]))

data.drop(
    ['Headline', 'Compound', '%Deliverble', 'Symbol', 'High', 'Low', 'Open', 'Deliverable Volume', 'Volume', 'VWAP',
     'Turnover', 'Trades', 'Last', 'Prev Close', 'Symbol', 'Series'], inplace=True, axis=1)
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
print(accuracy)