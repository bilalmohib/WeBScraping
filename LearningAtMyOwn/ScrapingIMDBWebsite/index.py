from bs4 import BeautifulSoup
import requests

try:
    source = requests.get('https://www.imdb.com/chart/top')
    source.raise_for_status()

    soup = BeautifulSoup(source.text,'html.parser')

    movies = soup.find('tbody',class_="lister-list").find_all('tr')

    for movie in movies:
        name = movie.find('td',class_="titleColumn")
    # print(movies[0].find('td',class_="titleColumn").text)

except Exception as e:
    print(e)