import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# want to select a radio button
# 1
# radiobtn = driver.find_element(By.CSS_SELECTOR,"input[value='radio2']")
# radiobtn.click()
# assert radiobtn.is_selected(),"Radio button not selected"

radiobtn = driver.find_elements(By.NAME,"radioButton")
print(len(radiobtn))
for radio in radiobtn:
    if radio.get_attribute("value") == "radio3":
        radio.click()
        break

time.sleep(4)