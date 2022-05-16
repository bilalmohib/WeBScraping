from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

# link = "https://accounts.google.com"
# driver = webdriver.Chrome(executable_path='/C:/ChromeDriver')
# driver.get(link)
driver = webdriver.Chrome('C:/ChromeDriver/chromedriver.exe')

products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
driver.get("https://www.flipkart.com/vertiv-liebert-iton-cx-600-va-1-x-7-ah-battery-536106003004-ups/p/itm7f735fe85d46f?pid=UPSG6WQ8VHFQHTFS&lid=LSTUPSG6WQ8VHFQHTFSSGLTXF&marketplace=FLIPKART&store=6bo&srno=b_1_1&otracker=browse&fm=organic&iid=en_tGtuNInrsqhqsunSmTl6mumZKsE4UPTp2namOfrkz0Hfs6cX3gtKdasVqn2nBsfjLIaZ%2F4%2BlgvqgttabyMN2SA%3D%3D&ppt=browse&ppn=browse&ssid=o6eu7bitb40000001652781987767")

content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('div'):
  content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('div',href=True, attrs={'class':'_1AtVbE col-12-12'}):
    name=a.find('span', attrs={'class':'B_NuCI'})
    price=a.find('div', attrs={'class':'_30jeq3 _16Jk6d'})
    rating=a.find('div', attrs={'class':'_3LWZlK'})
    products.append(name.text)
    prices.append(price.text)
    ratings.append(rating.text) 

df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings}) 
df.to_csv('newProduct.csv', index=False, encoding='utf-8')