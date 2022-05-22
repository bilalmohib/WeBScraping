import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

os.environ['PATH'] += r"C:/ChromeDriver"
browser = webdriver.Chrome()
browser.get("https://www.transfermarkt.us/")
element = browser.find_element(By.XPATH, '//*[@id="schnellsuche"]/input[1]')
element.send_keys("J1 League")
element2 = browser.find_element(By.XPATH, '//*[@id="schnellsuche"]/input[2]')
element2.click()
# element3 = browser.find_element(
#     By.XPATH, '//*[@id="content"]/div/div/table/tbody/tr/td[3]/a')
# element3.click()

# browser.back()
# browser.forward()
# browser.back()
# browser.back()
#Reached start again
# print(element)
time.sleep(10)
# browser.close()
