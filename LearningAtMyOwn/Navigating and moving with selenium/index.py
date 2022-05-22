from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import requests
import pandas as pd
import time

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
url_to_scrap = "https://www.transfermarkt.us/"
driver.get(url_to_scrap)

myDynamicElement = driver.find_element(By.ID("login")).span.text.click()
print(myDynamicElement)
# myDynamicElement.click()
time.sleep(5)

# link = driver.find_element(By.PARTIAL_LINK_TEXT, 'United States')
# link.click()

# try:
    # Will wait for 10 seconds
    # myDynamicElement = driver.find_element(By.TAG_NAME,"a")
    # print(len(myDynamicElement))
    # time.sleep(5)

    # element = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located(
    #         (By.ID, "sow-button-19310003"))
    # )
    # element.click()

    # driver.back()
    # driver.back()
    # driver.back()
    # driver.forward()
    # driver.forward()
# except:
#     print("Error occured")


# content = driver.page_source
# soup = BeautifulSoup(content, features="lxml")

# print(soup)
