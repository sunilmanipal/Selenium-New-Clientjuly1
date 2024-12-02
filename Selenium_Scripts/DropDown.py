import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# how to select a value from the dropdown
# dd = Select(driver.find_element(By.ID,"dropdown-class-example"))
# dd.select_by_visible_text("Option1")
# time.sleep(2)
# dd.select_by_value("option2")
# time.sleep(2)
# dd.select_by_index(3)
# time.sleep(2)
#
# # i want to check that what ever i have selected is present in the element
# actual = dd.first_selected_option
# actualres = actual.text
# time.sleep(2)
#
# Expected = "Option3"
# # this has to tell me my selected option is selected or not
# assert Expected == actualres,"The selected option is different from expected"
#
# # I have a dropdown and i want to fetch all the values present in the drop down
# ddvalues = dd.options
# print(len(ddvalues))
#
# for value in ddvalues:
#     print(value.text)
# # The below code is selecting multiple values in the dropdown
# for value in ddvalues:
#     if value.text == "Option1" or value.text == "Option2":
#         value.click()
#         time.sleep(2)
#
# time.sleep(2)

# If my application does not have select tagname then what? how to work
option = driver.find_elements(By.XPATH,"//*[@id='dropdown-class-example']/option")
print(len(option))

for value in option:
    print(value.text)

for value in option:
    if value.text == "Option1":
        value.click()
        time.sleep(2)
        break