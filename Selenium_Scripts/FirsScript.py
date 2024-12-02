# Step 1:To open the browser
# Step 2 : How to Navigate to the web page
import time

from selenium import webdriver
# from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.firefox.service import Service
# from selenium.webdriver.firefox.service import Service

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
# from webdriver_manager.firefox import FirefoxDriverManager
# Selenium --> two version
# 3 and 4 --> we also using version 4
# is a package/module/library which contains the all the methods to work with the browsers
# WHich will open a new instance of browser //it will open a new instance
# selenium version 4 --> webdrivermanager --> which will help me to automatically download the chrome driver for the latest version
# Selenium 3 --> we used to sownload and provide the path for the chrome driver , when my chrome gets updated i dont find the chrome driver version
# i didn like this headache, give the path so i used something called webdriver manager

# serviceobj = Service(executable_path='path')
# driver = webdriver.Chrome(service=serviceobj)
# driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
# driver = webdriver.firefox(service=Service(FirefoxDriverManager().install()))
# API(Commands) each command does a specific action
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# if i want to open any specific URL
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(3)
# Step 3: To enter the username
driver.find_element(By.NAME,"username").send_keys("Admin")
time.sleep(3)
# driver.find_element(By.CSS_SELECTOR,"input[class='oxd-input oxd-input--active'][placeholder='Password']").send_keys("admin123")

driver.find_element(By.NAME,"password").send_keys("admin123")
time.sleep(3)
# i Recommend CSS over Xpath the resaon is CSS is much lighter and much faster in identify the element
button = driver.find_element(By.CSS_SELECTOR,".oxd-button")
if button.is_enabled():
    print("button is enabled")
    button.click()
else:
    print("button is disabled")

time.sleep(3)
confirm = driver.find_element(By.TAG_NAME,"h6")
ExcptedResult = "Dashboard"
AcuatlResult = confirm.text
# when i want to compare expected and actual i use assert
assert ExcptedResult == AcuatlResult

# Validated i am in the right page
# i want to Logout
driver.find_element(By.CSS_SELECTOR,".oxd-userdropdown-name").click()
menu = driver.find_elements(By.CSS_SELECTOR,".oxd-userdropdown-link")
print("The number of links are : ", len(menu))
time.sleep(3)
# menu[3].click()
# driver.find_element(By.LINK_TEXT,"Logout").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"Log").click()
time.sleep(3)


