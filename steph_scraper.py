#most intuitive way
import pandas as pd
import requests
from bs4 import BeautifulSoup

res = requests.get("https://www.basketball-reference.com/players/c/curryst01.html")

soup = BeautifulSoup(res.content,'lxml')

table = soup.find_all('table')[0]

df = pd.read_html(str(table))[0]

ppg = df['PTS'].tolist()
print(ppg)
