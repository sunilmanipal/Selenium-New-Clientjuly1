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
iframe = driver.find_element(By.TAG_NAME,"iframe")
driver.switch_to.frame(iframe)
driver.find_element(By.LINK_TEXT,"Job Support").click()
time.sleep(4)
driver.switch_to.default_content()