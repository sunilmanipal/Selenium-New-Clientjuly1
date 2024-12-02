#Explicit Wait --> This is a wait, which we apply for a specific element, i want to check a specific element is present , visible
# so i can click or action on the element

# Implicit wait--> This is once applied in the program and this will be applicabale to all the elements

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
exwait = WebDriverWait(driver,40,poll_frequency=5,ignored_exceptions=[Exception])
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(3)
# ExplicitWait


# Here i am Login in by enetering the username and password
driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
driver.find_element(By.CSS_SELECTOR,".oxd-button").click()
#here i am clicking on PIM after Login
# driver.find_element(By.LINK_TEXT,"PIM").click()
# This explicit wait comes to us with a condition
pim_button = exwait.until(EC.visibility_of_element_located((By.LINK_TEXT,"PIM")))
pim_button.click()
# Browser Naviagtion Commands
# Back button in the browser
driver.back() #This will take you back to the dashboard
time.sleep(4)
# forward
driver.forward() # This will take you back to the PIM
time.sleep(4)
# If you are entering the data and you want to referesh you app
driver.refresh()
time.sleep(4)

#here i am logging out of the screen
clk = exwait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,".oxd-userdropdown-name")))
clk.click()
time.sleep(3)
driver.find_element(By.LINK_TEXT,"Logout").click()
time.sleep(3)