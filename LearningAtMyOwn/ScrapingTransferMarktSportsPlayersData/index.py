from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import pandas as pd

try:
    # source = requests.get('https://www.transfermarkt.us/j1-league/startseite/wettbewerb/JAP1')
    # source.raise_for_status()
    # soup = BeautifulSoup(source.text, 'html.parser')

    driver = webdriver.Chrome(executable_path='C:/ChromeDriver/chromedriver.exe')
    driver.get("https://www.transfermarkt.us/j1-league/startseite/wettbewerb/JAP1")
    content = driver.page_source
    soup = BeautifulSoup(content,features="lxml")
    # print(soup)

    movies = soup.find('table',class_="items").find('tbody').find_all('tr')

    #print(movies[0])

    for movie in movies:
        name = movie.find('td', class_="hauptlink no-border-links").a.text
        print(name)
        break


except Exception as e:
    print(e)
