from bs4 import BeautifulSoup
import requests
import pandas as pd

try:
    source = requests.get('https://www.imdb.com/chart/top')
    source.raise_for_status()

    soup = BeautifulSoup(source.text, 'html.parser')

    movies = soup.find('tbody', class_="lister-list").find_all('tr')

    # Defining the arrays to store the data
    nameArray = []
    rankArray = []
    yearArray = []
    ratingArray = []

    for movie in movies:
        name = movie.find('td', class_="titleColumn").a.text
        nameArray.append(name)
        rank = movie.find('td', class_="titleColumn").get_text(strip=True).split('.')[0]
        rankArray.append(rank)
        year = movie.find('td', class_="titleColumn").span.text.strip('()')
        yearArray.append(year)
        rating = movie.find('td', class_="ratingColumn imdbRating").strong.text
        ratingArray.append(rating)
        # print(rating)

    print("Rating Array : ", ratingArray)

    # Writing data finally to csv file
    df = pd.DataFrame(
        {
            "Rank": rankArray,
            "Name": nameArray,
            "Year": yearArray,
            "Rating": ratingArray
        }
    )
    df.to_csv("IMDBData.csv", index=True)


except Exception as e:
    print(e)
