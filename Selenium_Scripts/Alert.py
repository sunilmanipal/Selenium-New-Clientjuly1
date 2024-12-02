import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.find_element(By.ID,"alertbtn").click()
time.sleep(4)
# i want to handel the alert
alert = driver.switch_to.alert
# The error message can be captured
errormsg = alert.text
assert errormsg == "Hello , share this practice page and share your knowledge"
# But i never handeled and error
alert.accept() # To click on the ok button

driver.find_element(By.ID,"confirmbtn").click()
alert.dismiss() # if i want to click on the cancel button

# i am navigating to different application
driver.get("https://demoqa.com/alerts")
driver.find_element(By.ID,"promtButton").click()
newal = driver.switch_to.alert
newal.send_keys("I am sunil Nagaraj")
newal.accept()