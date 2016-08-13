
import requests
from bs4 import BeautifulSoup
import pandas as pd 
import numpy as np 

link = 'https://greenido.wordpress.com/2009/12/22/work-like-a-pro-with-yahoo-finance-hidden-api/'
res = requests.get(link)
soup = BeautifulSoup(res.content, 'html.parser')
soup.findAll('table')

soup.findAll('table')[0].findAll('tr')[0].findAll('span')[0].text
soup.findAll('table')[0].findAll('tr')[0].findAll('strong')[0].text
f = []
name = []
for j in xrange(13):
    for i in xrange(3):
        name.append(soup.findAll('table')[0].findAll('tr')[j].findAll('span',style="font-family:times;")[i].text)
        f.append(soup.findAll('table')[0].findAll('tr')[j].findAll('strong')[i].text)
link_f = ''.join(f)
link_f = link_f.replace(' ','')
# u'aa2a5bb2b3b4b6cc1c3c6c8dd1d2ee1e7e8e9f6ghjkg1g3g4g5g6ii5j1j3j4j5j6k1'