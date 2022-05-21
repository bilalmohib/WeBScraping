from asyncio.windows_events import NULL
from itertools import count
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import pandas as pd

try:
    # source = requests.get('https://www.transfermarkt.us/j1-league/startseite/wettbewerb/JAP1')
    # source.raise_for_status()
    # soup = BeautifulSoup(source.text, 'html.parser')

    def findAllClubsInALeague(league):
        driver = webdriver.Chrome(
            executable_path='C:/ChromeDriver/chromedriver.exe')
        url_to_scrap = "https://www.transfermarkt.us/" + \
            league + "/startseite/wettbewerb/JAP1"
        driver.get(url_to_scrap)
        content = driver.page_source
        soup = BeautifulSoup(content, features="lxml")
        # print(soup)

        clubs_data = soup.find('table', class_="items").find(
            'tbody').find_all('tr')

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
        df.to_csv(league + "." + "csv", index=False)
        return club_nameArray

    def findAllPlayersInClub(club):
        driver = webdriver.Chrome(
            executable_path='C:/ChromeDriver/chromedriver.exe')
        url_to_scrap = "https://www.transfermarkt.us/" + \
            club + "/kader/verein/3958/saison_id/2021/plus/1"
        driver.get(url_to_scrap)
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
            player_name = club_data.find(
                'td', class_="hauptlink no-border-links").a.text
            player_contract_price = club_data.find_all(
                'td', class_="zentriert")[1].a.text
            player_position = club_data.find_all(
                'td', class_="zentriert")[2].text
            player_club = club_data.find_all('td', class_="zentriert")[3].text
            player_league = club_data.find_all('td', class_="rechts")[0].text
            player_country = club_data.find_all(
                'td', class_="rechts")[1].a.text
            player_contract_start = club_data.find_all(
                'td', class_="rechts")[1].a.text
            player_contract_end = club_data.find_all(
                'td', class_="rechts")[1].a.text
            player_date_of_birth = club_data.find_all(
                'td', class_="rechts")[1].a.text


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

            # print(club_totalMarketValue)
            # break
        data = {
            "Column A": NULL,
            "Column B": NULL,
            "Serial No.": club_ageArray,
            "Column D": NULL,
            "Column E": NULL,
            "Player Name": club_totalMarketValueArray,
            "Column G": club_totalMarketValueArray,
            "Column H": club_foreignersArray,
            "Column I": club_marketValueArray,
            "Contract Price(USD)": club_totalMarketValueArray,
            "Column K": club_totalMarketValueArray,
            "Column L":NULL,
            "Player Position":club_totalMarketValueArray,
            "Club Name":club_totalMarketValueArray,
            "League Name":club_totalMarketValueArray,
            "Column P":club_totalMarketValueArray,
            "Country":country,
            "Club Contract Start Date":safdsda,
            "Club Contract End Date":asdf,
            "Club %":sdaf,
            "Club Starting No":sdafsda,
            "Date of birth of the player":daset
        }
        # Writing data finally to csv file
        df = pd.DataFrame(data)
        df.to_csv(club + "." + "csv", index=False)
        return player_nameArray

    # Main function Starts here

    def main():
        print("Starting Web Scraper")
        league_data = findAllClubsInALeague("j1-league")

        players_data = findAllPlayersInClub("vissel-kobe")

        # print(league_data)
        for league_names in league_data:
            print(league_names)

    main()

except Exception as e:
    print(e)
