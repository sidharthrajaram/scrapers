#shows usefulness of browser inspect element
import pandas as pd
import requests
from bs4 import BeautifulSoup

ticker = input("ticker symbol? ").lower()
res = requests.get("https://finance.yahoo.com/quote/"+ticker)
soup = BeautifulSoup(res.content,'lxml')

price = soup.find_all("span", {"class": "Trsdu(0.3s) Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(b)"})[0]
print(price.text)