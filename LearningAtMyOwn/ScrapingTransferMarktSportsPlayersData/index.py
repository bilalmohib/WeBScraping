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


def clear_console():
    os.system('cls')

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
    df.to_csv("AllClubsInLeague.csv", index=True)
    return club_linkArray

# To find all players in a club


def findAllPlayersInClub(urlArray, driver):

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

    for url in urlArray:
        print("Scraping Data From This Url right now: "+url)
        url_to_scrap = url
        driver.get(url_to_scrap)

        # go back to main frame
        driver.switch_to.default_content()

        # time.sleep(30)
        # Switching To Detailed View
        element2 = WebDriverWait(driver, 100).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="main"]/div[6]/div[1]/div/div[3]/a[2]')))
        # time.sleep(30)
        element2.click()
        print("Finally Got ", element2)

        # driver.refresh()

        content = driver.page_source

        soup = BeautifulSoup(content, features="lxml")
        # print(soup)

        # To find the correct data I have to find even and odd both and concatenate them other wise breakup occurs and false data comes in
        players_data_odd = soup.find('table', class_="items").find(
            'tbody').find_all('tr', class_="odd")
        players_data_even = soup.find('table', class_="items").find(
            'tbody').find_all('tr', class_="even")

        players_data = players_data_odd + players_data_even

        print("\n\n\n\n\n")

        print(players_data)

        print("\n\n\n -------------- Players Data Length is equal to : " +
              str(len(players_data)) + "   ------------")

        for player_data in players_data:
            count = count + 1
            # Extracting the data
            player_name = player_data.find(
                'td', class_="hauptlink").a.text
            # Removing left and right extra spaces
            player_name = player_name.strip()
            player_contract_price = player_data.find(
                'td', class_="rechts hauptlink").text
            player_contract_price = player_contract_price.strip()
            player_position = player_data.find_all(
                'td')[4].text
            player_position = player_position.strip()
            #player_SignedFrom = player_data.find_all('td', class_="zentriert")[6].a.img["alt"]
            player_club = soup.find('div', class_="dataName").h1.span.text
            player_club = player_club.strip()
            player_league = soup.find(
                'div', class_="dataZusatzDaten").span.a.text
            player_league = player_league.strip()
            player_country = player_data.find_all(
                'td', class_="zentriert")[2].img["title"]
            player_country = player_country.strip()
            player_contract_start = player_data.find_all(
                'td', class_="zentriert")[5].text
            player_contract_start = player_contract_start.strip()
            player_contract_end = player_data.find_all(
                'td', class_="zentriert")[7].text
            player_contract_end = player_contract_end.strip()
            player_date_of_birth = player_data.find_all(
                'td', class_="zentriert")[1].text
            player_date_of_birth = player_date_of_birth.strip()

            # print("\nPlayer name ===> ", player_name)
            # print("\n\n\n\n\n\n\n\n")

            # Appending the values to the arrays
            player_nameArray.append(player_name)
            player_contract_priceArray.append(player_contract_price)
            player_positionArray.append(player_position)
            player_clubArray.append(player_club)
            player_leagueArray.append(player_league)
            player_countryArray.append(player_country)
            player_contract_startArray.append(player_contract_start)
            player_contract_endArray.append(player_contract_end)
            player_date_of_birthArray.append(player_date_of_birth)
            indexArray.append(count)

    print("Player Name Array : ", player_nameArray)

    data = {
        "Column A": NULL,
        "Column B": NULL,
        "Serial No.": indexArray,
        "Column D": NULL,
        "Column E": NULL,
        "Player Name": player_nameArray,
        "Column G": NULL,
        "Column H": NULL,
        "Column I": NULL,
        "Contract Price(USD)": player_contract_priceArray,
        "Column K": NULL,
        "Column L": NULL,
        "Player Position": player_positionArray,
        "Club Name": player_clubArray,
        "League Name": player_leagueArray,
        "Column P": NULL,
        "Country": player_countryArray,
        "Club Contract Start Date": player_contract_startArray,
        "Club Contract End Date": player_contract_endArray,
        "Club %": NULL,
        "Club Starting No": NULL,
        "Date of birth of the player": player_date_of_birthArray
    }
    # Writing data finally to csv file
    df = pd.DataFrame(data)
    df.to_csv("AllPlayers" + "." + "csv", index=False)
    return player_nameArray


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
    combined_url_where_to_move = "https://www.transfermarkt.us" + \
        str(link_to_move)
    print("Found The Next URL Where I have to go: " + combined_url_where_to_move)
    return combined_url_where_to_move


def main():
    os.environ['PATH'] += r"C:/ChromeDriver"
    browser = webdriver.Chrome()
    browser.get("https://www.transfermarkt.us/")

    # Finding the search bar
    element = browser.find_element(
        By.XPATH, '//*[@id="schnellsuche"]/input[1]')
    # Getting the user input
    clear_console()
    league_name = input(
        "Please enter the leaugue name(strictly same name no spelling mistakes please): ")
    element.send_keys(league_name)
    # time.sleep(15)

    search_the_league = WebDriverWait(browser, 70).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="schnellsuche"]/input[2]')))
    search_the_league.click()

    # Get the current url
    current_url = browser.current_url
    # Function to get the url where the searched leaugue is present
    league_url = get_league_search_data(current_url, browser)

    # Now Got the url and now getting into next round 2 to find the all clubs in that league.
    # And now Passing arguement league url to the function findAllClubsInALeague
    all_clubs_in_league_url_array = findAllClubsInALeague(league_url, browser)

    #print("Got All the clubs url where I have to go now i will go : ")
    # print(all_clubs_in_league_url_array)

    # url_for_players_of_league = "https://www.transfermarkt.us/vissel-kobe/startseite/verein/3958/saison_id/2021/"

    findAllPlayersInClub(all_clubs_in_league_url_array, browser)

    # time.sleep(25)

main()
