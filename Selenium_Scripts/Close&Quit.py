import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(40)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()
time.sleep(5)
url = driver.current_url
print(url)
# I have two things
driver.close() # this is used when you want to close the active screen which is Login page

# Two tabs an di want to close botht the tabs then i use
# driver.quit() # This will close all the tabs and windows which is opened through the instance of driver