import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.implicitly_wait(40)
# URL
url = driver.current_url
print(url)

# fetch the title of the page
title = driver.title
print(title)

driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
driver.find_element(By.CSS_SELECTOR,".oxd-button").click()
#here i am clicking on PIM after Login
driver.find_element(By.LINK_TEXT,"PIM").click()
# i want to validate i am in PIM link
url1 = driver.current_url
assert url1.__contains__("pim"),"URL does notcontain PIM"

# i want to find out howmany links are there in the webpage
alllinks = driver.find_elements(By.TAG_NAME,"a")
# how many links
print(len(alllinks))
# fetch the names of the links
for link in alllinks:
    print(link.get_attribute("href"))
    print(link.text)

#here i am logging out of the screen
driver.find_element(By.CSS_SELECTOR,".oxd-userdropdown-name").click()
driver.find_element(By.LINK_TEXT,"Logout").click()