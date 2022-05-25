from asyncio.windows_events import NULL
import os
from xml.etree.ElementPath import xpath_tokenizer
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import pandas as pd

# To find all clubs in a league


def findAllClubsInALeague(url, driver):
    url_to_scrap = url
    driver.get(url_to_scrap)
    content = driver.page_source
    soup = BeautifulSoup(content, features="lxml")
    # print(soup)

    clubs_data = soup.find('table', class_="items").find(
        'tbody').find_all('tr')

    # print(players_data[0])

    # Defining Arrays to store data
    club_nameArray = []
    club_linkArray = []
    club_squadArray = []
    club_ageArray = []
    club_foreignersArray = []
    club_marketValueArray = []
    club_totalMarketValueArray = []

    for club_data in clubs_data:
        # Extracting the data
        club_name = club_data.find(
            'td', class_="hauptlink no-border-links").a.text
        club_link = club_data.find(
            'td', class_="hauptlink no-border-links").a['href']
        combined_club_link = "https://www.transfermarkt.us" + str(club_link)
        # print(combined_club_link)

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
        club_linkArray.append(combined_club_link)
        club_squadArray.append(club_squad)
        club_ageArray.append(club_age)
        club_foreignersArray.append(club_foreigners)
        club_marketValueArray.append(club_marketValue)
        club_totalMarketValueArray.append(club_totalMarketValue)

    # print(club_totalMarketValue)
    # break
    data = {
        "clubsNames": club_nameArray,
        "clubLinkArray": club_linkArray,
        "clubSquad": club_squadArray,
        "clubAge": club_ageArray,
        "clubForeigners": club_foreignersArray,
        "clubMarketValue": club_marketValueArray,
        "clubTotalMarketValue": club_totalMarketValueArray
    }
    # Writing data finally to csv file
    df = pd.DataFrame(data)
    df.to_csv("check.csv", index=True)
    return club_linkArray

# To find all players in a club


def findAllPlayersInClub(url, driver):
    url_to_scrap = url
    driver.get(url_to_scrap)

    # go back to main frame
    driver.switch_to.default_content()

    # here's the trick, what you are looking for is inside a "shadow-root" DOM so to access it you need to execute the script and then use CSS selector, I don't think XPATH works here:
    element2 = WebDriverWait(driver, 50).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="main"]/div[6]/div[1]/div/div[3]/a[2]')))
    time.sleep(20)
    element2.click()
    print("Finally Got ", element2)

    # driver.refresh()

    content = driver.page_source

    soup = BeautifulSoup(content, features="lxml")
    # print(soup)

    players_data = soup.find('table', class_="items").find(
        'tbody').find_all('tr')

    # print(players_data[0])

    # Defining Arrays to store data
    player_nameArray = []
    player_contract_priceArray = []
    player_positionArray = []
    player_clubArray = []
    player_leagueArray = []
    player_countryArray = []
    player_contract_startArray = []
    player_contract_endArray = []
    player_date_of_birthArray = []
    indexArray = []

    count = 0
    for player_data in players_data:
        count = count + 1
        # Extracting the data
        player_name = player_data.find(
            'td', class_="hauptlink")
        player_contract_price = player_data.find(
            'td', class_="rechts hauptlink").text
        player_position = player_data.find_all(
                'td')[4].text
        player_SignedFrom = player_data.find_all('td', class_="zentriert")[6].a.img["alt"]
        player_club = soup.find('div', class_="dataName").h1.span.text
        player_league = soup.find('div', class_="dataZusatzDaten").span.a.text
        player_country = player_data.find_all('td', class_="zentriert")[2].img["title"]
        player_contract_start = player_data.find_all('td', class_="zentriert")[5].text
        # player_contract_end = player_data.find_all(
        #         'td', class_="rechts")[1].a.text
        # player_date_of_birth = player_data.find_all(
        #         'td', class_="rechts")[1].a.text

        print("\n\n\n\n\n\n\n\nPlayer_contract_start ===> ", player_contract_start)
        print("\n\n\n\n\n\n\n\n")
        break

        # Appending the values to the arrays
        # player_nameArray.append(player_name)
        # player_contract_priceArray.append(player_contract_price)
        # player_positionArray.append(player_position)
        # player_clubArray.append(player_club)
        # player_leagueArray.append(player_league)
        # player_countryArray.append(player_country)
        # player_contract_startArray.append(player_contract_start)
        # player_contract_endArray.append(player_contract_end)
        # player_date_of_birthArray.append(player_date_of_birth)
        # indexArray.append(count)

    # data = {
    #         "Column A": NULL,
    #         "Column B": NULL,
    #         "Serial No.": indexArray,
    #         "Column D": NULL,
    #         "Column E": NULL,
    #         "Player Name": player_nameArray,
    #         "Column G": NULL,
    #         "Column H": NULL,
    #         "Column I": NULL,
    #         "Contract Price(USD)": player_contract_priceArray,
    #         "Column K": NULL,
    #         "Column L":NULL,
    #         "Player Position":player_positionArray,
    #         "Club Name":player_clubArray,
    #         "League Name":player_leagueArray,
    #         "Column P":NULL,
    #         "Country":player_countryArray,
    #         "Club Contract Start Date":player_contract_startArray,
    #         "Club Contract End Date":player_contract_endArray,
    #         "Club %":NULL,
    #         "Club Starting No":NULL,
    #         "Date of birth of the player":player_date_of_birthArray
    # }
    # Writing data finally to csv file
    # df = pd.DataFrame(data)
    # df.to_csv(club + "." + "csv", index=False)
    # return player_nameArray


# To find all players in a club

def get_league_search_data(url, driver):
    url_to_scrap = url
    driver.get(url_to_scrap)
    content = driver.page_source

#     time.sleep(10)

    soup = BeautifulSoup(content, features="lxml")
    # print(soup)

#     time.sleep(10)

    club_data = soup.find('table', class_="items").find('tbody').find_all('tr')

    # print(club_data[0])
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
    # element = browser.find_element(By.XPATH, '//*[@id="schnellsuche"]/input[1]')
    # element.send_keys("J1 League")
    # time.sleep(15)

    # search_it_idiot = wait(browser, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="schnellsuche"]/input[2]')))
    # search_it_idiot.click()

    # Get the current url
    #current_url = browser.current_url
    # Function to get the url where the searched leaugue is present
    #league_url = get_league_search_data(current_url,browser)

    # Now Got the url and now getting into next round 2 to find the all clubs in that league.
    # Passing arguement league url to the function findAllClubsInALeague
    #league_names_array = findAllClubsInALeague(league_url,browser)

    #print("Got All the clubs url where I have to go now i will go : "+league_names_array)

    url_for_players_of_league = "https://www.transfermarkt.us/vissel-kobe/startseite/verein/3958/saison_id/2021/"

    findAllPlayersInClub(url_for_players_of_league, browser)

    time.sleep(25)


main()
