# Web Scraping Tutorial From FreeCodeCamp

# Importing bs4 from BeautifulSoup
from bs4 import BeautifulSoup

# Reading Html file
with open('index.html','r', encoding="utf8") as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content,'lxml')
    # print(soup.prettify())
    tags = soup.find('div')
    # List all the h1 tags using findAll
    tags = soup.findAll('p')
    print(tags)