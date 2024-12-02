import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# i want to select the checkboxes
# driver.find_element(By.ID,"checkBoxOption1").click()
# driver.find_element(By.CSS_SELECTOR,"#checkBoxOption1").click()
# driver.find_element(By.XPATH,"//*[@id=“checkBoxOption1”]").click()
# time.sleep(3)
# i want to check all the checkboxes
# driver.find_elements(By.CSS_SELECTOR,"input[type='checkbox']")
chckbx = driver.find_elements(By.XPATH,"//*[@type='checkbox' and contains(@id, 'checkBoxOption')]")

# i clicked on all the checkboxes
# for checkbox in chckbx:
#     checkbox.click()

# 2 way
# for i in range(len(chckbx)):
#     chckbx[i].click()
# time.sleep(3)

# Let's say i want to select any two checkboxes

checkvalue = ['option1','option3']
for checkbox in chckbx:
    if checkbox.get_attribute("value") in checkvalue:
        checkbox.click()

time.sleep(3)
# i want to know what the belowlines will do
for checkbox in chckbx:
    if checkbox.is_selected():
        checkbox.click()