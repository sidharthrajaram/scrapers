#using find_all to dig deeper into html structure
import requests
from bs4 import BeautifulSoup

res = requests.get("https://www.basketball-reference.com/players/j/jamesle01.html")

soup = BeautifulSoup(res.content,'lxml')

#index is 1 due to new addition to their website
table = soup.find_all('table')[1]

row = table.find_all('tr')[1]
# print(row)

s1_stats = []

for data in row.find_all('td'):
    s1_stats.append(data.text)

print(s1_stats)