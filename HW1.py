import requests 
from bs4 import BeautifulSoup
import pandas as pd 
import jieba
import nltk

url = "https://www.ptt.cc/bbs/nCoV2019/index.html"
for i in range(3):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    sel = soup.select("div.title a")
    u = soup.select("div.btn-group.btn-group-paging a")
    print(url)
    url = "https://www.ptt.cc" + u[1]["href"]

    for s in sel:
        print(s.text)
