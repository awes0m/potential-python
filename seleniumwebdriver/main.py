from selenium import webdriver

chrome_driver_path="C:\Development\chromedriver.exe"
driver=webdriver.Chrome(executable_path=chrome_driver_path)

web=driver.get("https://www.python.org/")
event_times=driver.find_elements_by_css_selector(".event-widget time")
event_names=driver.find_elements_by_css_selector(".event-widget li a")
event = {_: {
        "time":event_times[_].text,
        "name":event_names[_].text,
    } for _ in range(len(event_times))}
print(event)
driver.close()