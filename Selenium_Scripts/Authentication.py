import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(40)
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
driver.maximize_window()

value = driver.find_element(By.XPATH,"//p").text
assert value =="Congratulations! You must have the proper credentials.","This is not same"
time.sleep(3)