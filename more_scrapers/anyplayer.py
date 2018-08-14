#scrapes for year-by-year points/game stats for player of choice
import pandas as pd
import requests
from bs4 import BeautifulSoup

#this isn't the best way to do it. You should use Google custom search engine API to get links for each player.
player_name = input("Full name of player? ").lower()
ln_fi = player_name.find(' ')+1 #index of first initial of last name
first = player_name[:2]
last = player_name[ln_fi:ln_fi+5]

link = "https://www.basketball-reference.com/players/"+player_name[ln_fi]+"/"+last+first+"01.html"

res = requests.get(link)

soup = BeautifulSoup(res.content,'lxml')

table = soup.find_all('table')[0]

df = pd.read_html(str(table))[0]

ppg = df['PTS'].tolist()
print(ppg)