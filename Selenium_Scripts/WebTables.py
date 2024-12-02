import time

import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(40)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
colum2values = driver.find_elements(By.XPATH,"//*[@name='courses']/tbody/tr/td[2]")
# print(colum2values)

for i in colum2values:
    if i.text.__contains__("Python"):
        price =i.find_element(By.XPATH,"./following-sibling::td")
        print(price.text)