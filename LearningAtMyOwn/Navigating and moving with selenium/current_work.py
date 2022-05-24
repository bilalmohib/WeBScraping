import os
from xml.etree.ElementPath import xpath_tokenizer
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from bs4 import BeautifulSoup
import requests
import pandas as pd

def findAllClubsInALeague(url,driver):
    url_to_scrap = url
    driver.get(url_to_scrap)
    content = driver.page_source
    soup = BeautifulSoup(content, features="lxml")
    # print(soup)

    clubs_data = soup.find('table', class_="items").find('tbody').find_all('tr')

    # print(players_data[0])

    # Defining Arrays to store data
    club_nameArray = []
    club_squadArray = []
    club_ageArray = []
    club_foreignersArray = []
    club_marketValueArray = []
    club_totalMarketValueArray = []

    for club_data in clubs_data:
        # Extracting the data
        club_name = club_data.find(
                'td', class_="hauptlink no-border-links").a.text
        club_squad = club_data.find_all('td', class_="zentriert")[1].a.text
        club_age = club_data.find_all('td', class_="zentriert")[2].text
        club_foreigners = club_data.find_all(
                'td', class_="zentriert")[3].text
        club_marketValue = club_data.find_all(
                'td', class_="rechts")[0].text
        club_totalMarketValue = club_data.find_all(
                'td', class_="rechts")[1].a.text

        # Appending the values to the arrays
        club_nameArray.append(club_name)
        club_squadArray.append(club_squad)
        club_ageArray.append(club_age)
        club_foreignersArray.append(club_foreigners)
        club_marketValueArray.append(club_marketValue)
        club_totalMarketValueArray.append(club_totalMarketValue)

    # print(club_totalMarketValue)
    # break
    data = {
            "clubsNames": club_nameArray,
            "clubSquad": club_squadArray,
            "clubAge": club_ageArray,
            "clubForeigners": club_foreignersArray,
            "clubMarketValue": club_marketValueArray,
            "clubTotalMarketValue": club_totalMarketValueArray
    }
    # Writing data finally to csv file
    df = pd.DataFrame(data)
    df.to_csv("check.csv", index=True)
    return club_nameArray

def get_league_search_data(url,driver):
    url_to_scrap = url
    driver.get(url_to_scrap)
    content = driver.page_source
    soup = BeautifulSoup(content, features="lxml")
    # print(soup)

    club_data = soup.find('table', class_="items").find('tbody').find_all('tr')

    #print(club_data[0])
    league_name = club_data[0].find_all(
                 'td')[1]
#     league_name.a.click()
#     print(league_name.a)
    anchor_tag = league_name.a
    link_to_move = anchor_tag['href']
    combined_url_where_to_move = "https://www.transfermarkt.us" + str(link_to_move)
    print("Found The Next URL Where I have to go: " + combined_url_where_to_move)
    return combined_url_where_to_move


    # Defining Arrays to store data
#     club_nameArray = []
#     club_squadArray = []
#     club_ageArray = []
#     club_foreignersArray = []
#     club_marketValueArray = []
#     club_totalMarketValueArray = []

#     for club_data in clubs_data:
#         # Extracting the data
#         club_name = club_data.find(
#                 'td', class_="hauptlink no-border-links").a.text
#         club_squad = club_data.find_all('td', class_="zentriert")[1].a.text
#         club_age = club_data.find_all('td', class_="zentriert")[2].text
#         club_foreigners = club_data.find_all(
#                 'td', class_="zentriert")[3].text
#         club_marketValue = club_data.find_all(
#                 'td', class_="rechts")[0].text
#         club_totalMarketValue = club_data.find_all(
#                 'td', class_="rechts")[1].a.text

#         # Appending the values to the arrays
#         club_nameArray.append(club_name)
#         club_squadArray.append(club_squad)
#         club_ageArray.append(club_age)
#         club_foreignersArray.append(club_foreigners)
#         club_marketValueArray.append(club_marketValue)
#         club_totalMarketValueArray.append(club_totalMarketValue)

#     # print(club_totalMarketValue)
#     # break
#     data = {
#             "clubsNames": club_nameArray,
#             "clubSquad": club_squadArray,
#             "clubAge": club_ageArray,
#             "clubForeigners": club_foreignersArray,
#             "clubMarketValue": club_marketValueArray,
#             "clubTotalMarketValue": club_totalMarketValueArray
#     }
#     # Writing data finally to csv file
#     df = pd.DataFrame(data)
#     df.to_csv(url + "." + "csv", index=False)
#     return club_nameArray

def main():
    os.environ['PATH'] += r"C:/ChromeDriver"
    browser = webdriver.Chrome()
    browser.get("https://www.transfermarkt.us/")
    element = browser.find_element(By.XPATH, '//*[@id="schnellsuche"]/input[1]')
    element.send_keys("J1 League")
    time.sleep(15)

    search_it_idiot = wait(browser, 40).until(EC.presence_of_element_located((By.XPATH, '//*[@id="schnellsuche"]/input[2]')))
    search_it_idiot.click()

    # Get the current url 
    current_url = browser.current_url
    # Function to get the url where the searched leaugue is present 
    league_url = get_league_search_data(current_url,browser)
    
    # Now Got the url and now getting into next round 2 to find the all clubs in that league.
    # Passing arguement league url to the function findAllClubsInALeague
    findAllClubsInALeague(league_url,browser)

    time.sleep(25)

main()