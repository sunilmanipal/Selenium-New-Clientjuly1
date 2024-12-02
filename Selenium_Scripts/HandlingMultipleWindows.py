import time

import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(40)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
# When i click on this it will open a new window for me
driver.find_element(By.ID,"openwindow").click()
# time.sleep(5)
# window_handles --> this will capture all the windows (child window , parent )

windows = driver.window_handles
print(windows)
# This will capture the parent window only --> it will not capture any of your child window
# driver.current_window_handle
# all the features
# One of the way of doing things
driver.switch_to.window(windows[0])
print(driver.title)
print(driver.current_url)
# Child Window
driver.switch_to.window(windows[1])
print(driver.title)
print(driver.current_url)
driver.close()
time.sleep(4)

for window in windows:
    driver.switch_to.window(window)
    if driver.title == "QAClick Academy - A Testing Academy to Learn, Earn and Shine":
        assert driver.title == "QAClick Academy - A Testing Academy to Learn, Earn and Shine"
        driver.find_element(By.LINK_TEXT,"Courses").click()
        time.sleep(4)
        driver.close()
    else:
        print(driver.title)
