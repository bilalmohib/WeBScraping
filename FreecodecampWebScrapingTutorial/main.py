# Web Scraping Tutorial From FreeCodeCamp

# Importing bs4 from BeautifulSoup
from bs4 import BeautifulSoup

# Reading Html file
with open('check.html','r', encoding="utf8") as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content,'lxml')
    # print(soup.prettify())
    tags = soup.findAll('li')
    # List all the h1 tags using findAll
    # tags = soup.findAll('p')
    print(len(tags))
    list_countries = []
    for tag in tags:
        list_countries.append(tag.span.text)
        # print(tag.span.text)
    print(list_countries)