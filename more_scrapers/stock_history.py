#scraping for table of historical data for stock of choice
import pandas as pd
import requests
from bs4 import BeautifulSoup

ticker = input("ticker symbol? ").lower()
res = requests.get("https://finance.yahoo.com/quote/"+ticker+"/history?p="+ticker)

soup = BeautifulSoup(res.content, "lxml")
table = soup.find_all("table")[0]

df = pd.read_html(str(table))[0]
print(df)
print()

dates = df['Date'].tolist()
closing_values = df['Close*'].tolist()
print(closing_values)
print()

#analysis
index = closing_values.index(max(closing_values))
print("The stock price of {} was at its highest on {} at a value of {}".format(ticker, dates[index], max(closing_values)))
