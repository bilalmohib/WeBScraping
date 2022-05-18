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

    clubs_data = soup.find('table',class_="items").find('tbody').find_all('tr')

    #print(players_data[0])

    # Defining Arrays to store data
    club_nameArray = []
    club_squadArray = []
    club_ageArray = []
    club_foreignersArray = []
    club_marketValueArray = []
    club_totalMarketValueArray = []

    for club_data in clubs_data:
        # Extracting the data
        club_name = club_data.find('td', class_="hauptlink no-border-links").a.text
        club_squad = club_data.find_all('td', class_="zentriert")[1].a.text
        club_age = club_data.find_all('td', class_="zentriert")[2].text
        # club_foreigners = movie.find('td', class_="hauptlink no-border-links").a.text
        # club_marketValue = movie.find('td', class_="hauptlink no-border-links").a.text
        # club_totalMarketValue = movie.find('td', class_="hauptlink no-border-links").a.text

        # Appending the values to the arrays
        # club_nameArray.append(club_name)
        # club_squadArray.append(club_squad)
        # club_ageArray.append(club_age)
        # club_foreignersArray.append(club_foreigners)   
        # club_marketValueArray.append(club_marketValue)
        # club_totalMarketValueArray.append(club_totalMarketValue)

        print(club_age)
        break


except Exception as e:
    print(e)
