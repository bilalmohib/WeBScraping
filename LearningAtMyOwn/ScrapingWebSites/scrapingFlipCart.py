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
driver.get("https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniqBStoreParam1=val1&wid=11.productCard.PMU_V2")

content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('a'):
  content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('a',href=True, attrs={'class':'_1fQZEK'}):
    name=a.find('div', attrs={'class':'_4rR01T'})
    price=a.find('div', attrs={'class':'_30jeq3 _1_WHN1'})
    rating=a.find('div', attrs={'class':'_3LWZlK'})
    products.append(name.text)
    prices.append(price.text)
    ratings.append(rating.text) 

df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings}) 
df.to_csv('products.csv', index=False, encoding='utf-8')