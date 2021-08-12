from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path="C:\Development\chromedriver.exe"
driver=webdriver.Chrome(executable_path=chrome_driver_path)

web=driver.get("https://en.wikipedia.org/wiki/Main_Page")
article_no=driver.find_element_by_css_selector("#articlecount > a")
# print(article_no.text)
search_bar=driver.find_element_by_name("search")
search_bar.send_keys("Python")
search_bar.send_keys(Keys.ENTER)
# driver.close()