# When we go with testing we have to test for broken Lonks
import time

import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(40)
driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()

# i have to click on all the link and check is all the links are working
alllinks = driver.find_elements(By.TAG_NAME,"a")

for link in alllinks:
    url = link.get_attribute("href")
    # i want to go to this sepcific URL to check is this url giving me the response if the respons eis 200
    res = requests.head(url)
    if res.status_code>=400:
        print(url,"this is broken link")
    else:
        print(url,"Thisis valid link")
# print("Total number of links ")