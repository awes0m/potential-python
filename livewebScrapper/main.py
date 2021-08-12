#!/usr/bin/env python3
import requests
from bs4 import *
import datetime

telegram_endpoint='https://api.telegram.org'
somdgod_stocks_bot='1729364718:AAFncIpc7Tcfve2DuUb3RgwsatXzH9GzmVE'
chat_id='-1001362548332'
url='https://news.ycombinator.com/'
a_no=0
article_text=[]
article_link=[]
final_news=f"Top 3 Headlines from {url} :\n\n"



response=requests.get(url=url)
live_web_page=response.text

soup=BeautifulSoup(live_web_page,"html.parser")
print(soup.title.getText())

article_tag=soup.find_all(name='a',class_='storylink')
article_upvote=[int(score.getText().split()[0]) for score in soup.find_all(name='span',class_='score')]

current_date =str(datetime.datetime.now())


for article in article_tag:
    text=article.getText()
    link=article.get('href')
    article_text.append(text)
    article_link.append(link)

sorted_articles=article_upvote
sorted_articles.sort(reverse=True)
print(sorted_articles)
top3=sorted_articles[:3]
for i in top3:
    article_index=article_upvote.index(i)
    news=f"Headline:-{article_text[article_index]}, Upvoted :{article_upvote[article_index]} \nLink:{article_link[article_index]}\n"
    final_news=final_news+news

bot_endpoint = f"{telegram_endpoint}/bot{somdgod_stocks_bot}/sendMessage"
stock_articles = {
    'chat_id': chat_id,
    'text': final_news,
}
response1 = requests.post(url=bot_endpoint, params=stock_articles)
print(response1.json())
