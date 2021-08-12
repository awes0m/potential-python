from bs4 import *
website="index.html"
with open(f"{website}",encoding='utf8') as file:
    contents= file.read()
soup= BeautifulSoup(contents,"html.parser")
tittle=soup.find(name='title')
print(tittle.string)
headings=soup.find_all(name='h1')
for _ in headings:
    print(_.getText())
# all_anchor=soup.findAll(name='a')
# for _ in all_anchor:
#     print(_.get("href"))
company_url=soup.select_one(selector='p a')
print(company_url.get('href'))
