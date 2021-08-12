from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path="C:\Development\chromedriver.exe"
driver=webdriver.Chrome(executable_path=chrome_driver_path)

web=driver.get("https://orteil.dashnet.org/cookieclicker/")
cookie=driver.find_element_by_xpath("//*[@id='bigCookie']")
for i in range(2000):
    cookie.click()