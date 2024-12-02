import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(2)
driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
driver.find_element(By.CSS_SELECTOR,".oxd-button").click()
time.sleep(3)
driver.find_element(By.LINK_TEXT,"PIM").click()
time.sleep(3)

driver.find_element(By.CSS_SELECTOR,"input[placeholder='Type for hints...']").send_keys("A")
time.sleep(4)

values = driver.find_elements(By.CSS_SELECTOR,"div[class='oxd-autocomplete-option'] span")
for value in values:
    if value.text == "Abdulrahman Ramadan Abdo":
        value.click()
        break
time.sleep(4)
# driver.find_element(By.CSS_SELECTOR,".oxd-input").send_keys("Admin")
# time.sleep(8)