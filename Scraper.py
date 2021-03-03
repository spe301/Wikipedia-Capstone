import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

def GetText(url):
   '''Scrapes a wikikedia article'''
   source = urlopen(url).read()
   soup = BeautifulSoup(source, 'lxml')
   text = soup.findAll('p')
   article = ''
   for i in range(len(text)):
       segment = text[i].text
       article += segment.replace('\n', '').replace('\'', '').replace(')', '')
   article = article.lower()
   clean = re.sub("([\(\[]).*?([\)\]])", '', article)
   clean2 = re.sub(r'\[(^)*\]', '', clean)
   return clean

n = 10000
articles = []
Human = []
AI = []
for i in range(n):
    articles.append(GetText('https://en.wikipedia.org/wiki/Special:Random')) 
    Human.append(1)
    AI.append(0)
    print(i) #just to keep track of progress
    
df = pd.DataFrame(articles)
df.columns = ['Text']
df['Human'] = Human
df['AI'] = AI

df.to_csv(r'C:\Users\aacjp\Wikipedia-Capstone\Data\Human2.csv')