#scrapes basketball reference for Steph Curry's year-by-year points/game stats
import pandas as pd
import requests
from bs4 import BeautifulSoup

res = requests.get("https://www.basketball-reference.com/players/c/curryst01.html")

soup = BeautifulSoup(res.content,'lxml')

#index is 1 due to new addition to their website
table = soup.find_all('table')[1]

df = pd.read_html(str(table))[0]

ppg = df['PTS'].tolist()
print(ppg)
