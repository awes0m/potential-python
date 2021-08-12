#!/usr/bin/env python3
import requests
from bs4 import *
import datetime

html.scriptsOn body#styleguide-v2.fixed div#wrapper div#root.redesign div#pagecontent.pagecontent div#content-2-wide div#main div.article.listo div.lister.list.detail.sub-list div.lister-list div.lister-item.mode-detail div.lister-item-content h3.lister-item-header a

telegram_endpoint='https://api.telegram.org'
somdgod_stocks_bot='1729364718:AAFncIpc7Tcfve2DuUb3RgwsatXzH9GzmVE'
chat_id='-1001362548332'
url='https://www.imdb.com/list/ls042288708/'

#selector=div.lister-item:nth-child(1) > div:nth-child(2) > h3:nth-child(1) > a:nth-child(2)
a_no=0
article_text=[]
article_link=[]
final_news=f"Top 3 Headlines from {url} :\n\n"



response=requests.get(url=url)
live_web_page=response.text

soup=BeautifulSoup(live_web_page,"html.parser")
mainTitle=soup.title.getText()
#print (mainTitle)
#print(live_web_page)

with open(f"imdblist scrapper/{mainTitle}.txt", "w+") as file1:
    # Writing data to a file
    file1.write(mainTitle)
    file1.writelines(live_web_page)



