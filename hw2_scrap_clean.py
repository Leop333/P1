#final
import os
os.chdir("D:\\Study\\CL\\pyth")
import requests as rq
from bs4 import BeautifulSoup
import pandas as pd

#1 daily
ved_url="https://www.vedomosti.ru"  
url_d = ved_url+"/ecology"
page_d = rq.get(url_d) 
print(page_d) 
soup_d = BeautifulSoup(page_d.text, features="html.parser")

#get all daily issues urls
urls_daily = []
for ln1 in soup_d.find_all('a'):
  if 'ecology' in ln1.get('href') and 'release' in ln1.get('href') not in urls_daily :
    urls_daily.append(ln1.get('href'))
urls_daily



# loop for issue links  
type(urls_daily)
urls_issue = []
for ln2 in range(len(urls_daily)):
  page_i = rq.get(ved_url+urls_daily[ln2])
  soup_i = BeautifulSoup(page_i.text,features="html.parser")
  for ln3 in soup_i.find_all('a'):
    if ln3.get('href') != None and  'articles' in ln3.get('href') and 'ecology' in ln3.get('href') : 
        urls_issue.append(ln3.get('href'))

#check
len(urls_issue)


#clean function from net
def rm_html_tg(text):
    import re
    clean = re.compile('<.*?>') 
    return re.sub(clean, '', text)


#make news-df
predf={}

for ln3 in range(len(urls_issue)):
  url_n= ved_url+urls_issue[ln3]
  page_n = rq.get(url_n)
  soup_n= BeautifulSoup(page_n.text,features="html.parser")
  date_n= soup_n.find_all('time',{'class':'article-meta__date'})[0].attrs['datetime']
  title_n=soup_n.find_all('meta', {'property' : 'og:title'})[0].attrs['content']
  text_n= rm_html_tg(str(soup_n.find_all('p', {'class':'box-paragraph__text'})))
  predf[ln3+1] = [title_n,text_n,url_n, date_n]

eco_news_corp = pd.DataFrame.from_dict(predf, orient="columns").T
eco_news_corp =eco_news_corp.rename(columns={0:"title", 1:"text", 2:"link", 3:"date"})

# store in xls
eco_news_corp.to_excel('econews.xlsx')

