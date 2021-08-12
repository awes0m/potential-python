from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path="C:\Development\chromedriver.exe"
driver=webdriver.Chrome(executable_path=chrome_driver_path)

web=driver.get("http://secure-retreat-92358.herokuapp.com/")
first_name=driver.find_element_by_name("fName")
last_name=driver.find_element_by_name("lName")
email=driver.find_element_by_name("email")
button=driver.find_element_by_xpath("/html/body/form/button")
first_name.send_keys("Som")
last_name.send_keys("dgod")
email.send_keys("somdevalmighty@gmail.com")
button.send_keys(Keys.ENTER)
driver.close()
