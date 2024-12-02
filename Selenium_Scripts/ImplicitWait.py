import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# There are two types of wait in selenium
# 1) Implicitwait --> This is a wait applied once in the program , and this will be applicabale to All the lines in the program
driver.implicitly_wait(40) # When ever an element is not found , this will come in to picture and wait till the element is present
# time.sleep(3) # wait for about 3 sec no matter waht it will wait for 3 sec
# Here i am Login in by enetering the username and password
driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
driver.find_element(By.CSS_SELECTOR,".oxd-button").click()
#here i am clicking on PIM after Login
driver.find_element(By.LINK_TEXT,"PIM").click()
#here i am logging out of the screen
driver.find_element(By.CSS_SELECTOR,".oxd-userdropdown-name").click()
driver.find_element(By.LINK_TEXT,"Logout").click()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# There are two types of wait in selenium
# 1) Implicitwait --> This is a wait applied once in the program , and this will be applicabale to All the lines in the program
driver.implicitly_wait(40) # When ever an element is not found , this will come in to picture and wait till the element is present
# time.sleep(3) # wait for about 3 sec no matter waht it will wait for 3 sec
# Here i am Login in by enetering the username and password
driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
driver.find_element(By.CSS_SELECTOR,".oxd-button").click()
#here i am clicking on PIM after Login
driver.find_element(By.LINK_TEXT,"PIM").click()
#here i am logging out of the screen
driver.find_element(By.CSS_SELECTOR,".oxd-userdropdown-name").click()
driver.find_element(By.LINK_TEXT,"Logout").click()