from asyncio.windows_events import NULL
from itertools import count
from weakref import finalize
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests
import pandas as pd
import time

driver = webdriver.Chrome(executable_path='C:/ChromeDriver/chromedriver.exe')
url_to_scrap = "https://www.techwithtim.net/"
driver.get(url_to_scrap)

link = driver.find_element(By.LINK_TEXT, "Python Programming")
link.click()

try:
    # Will wait for 10 seconds
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.LINK_TEXT, "Beginner Python Tutorials"))
    )
    element.click()

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, "sow-button-19310003"))
    )
    element.click()
except:
    driver.quit()


# content = driver.page_source
# soup = BeautifulSoup(content, features="lxml")

# print(soup)
