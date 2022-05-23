import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait

os.environ['PATH'] += r"C:/ChromeDriver"
browser = webdriver.Chrome()
browser.get("https://www.transfermarkt.us/")
element = browser.find_element(By.XPATH, '//*[@id="schnellsuche"]/input[1]')
element.send_keys("J1 League")
time.sleep(5)

# element2 = browser.find_element(By.XPATH, '//*[@id="main"]/header/div[3]/tm-quick-select-bar//div/tm-quick-select[1]/div/div[1]/strong/text()')
# element2.click()

button = wait(browser, 10).until(EC.presence_of_element_located(
    (By.XPATH, '//*[@id="schnellsuche"]/input[2]')))
button.click()

# element2 = browser.find_element(By.XPATH, '//*[@id="schnellsuche"]/input[2]')
# element2.click()

####################In Use###################################
# button = wait(browser, 10).until(EC.presence_of_element_located(
#     (By.XPATH, '//*[@id="schnellsuche"]/input[2]')))
# button.click()
# time.sleep(5)
# print(browser.current_url)
####################In Use###################################

# button2 = wait(browser, 10).until(EC.presence_of_element_located(
#     (By.XPATH, '//*[@id="yw0"]/table/tbody/tr[1]/td[2]/a')))
# button2.click()
# time.sleep(5)
# element3 = browser.find_element(
#     By.XPATH, '//*[@id="main"]/header/div[3]/tm-quick-select-bar//div/tm-quick-select[1]/div/div/strong')
# element3.click()

# browser.back()
# browser.forward()
# browser.back()
# browser.back()
# Reached start again
# print(element)
time.sleep(10)
# browser.close()
