from os import link
import requests, webbrowser,bs4

search=str(input("enter search terms --"))
res= requests.get(f"https://www.google.com/search?q={search}")
res.raise_for_status()

soup=bs4.BeautifulSoup(res.text,"html.parser")
linkElements=soup.select('.r a')
LinksToOpen=min(5,len(linkElements))
for i in range(LinksToOpen):
    webbrowser.open("https://www.google.com",+linkElements[i].get('href'))