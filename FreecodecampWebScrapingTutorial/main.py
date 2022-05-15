# Web Scraping Tutorial From FreeCodeCamp

# Importing bs4 from BeautifulSoup
from bs4 import BeautifulSoup

# Reading Html file
with open('index.html','r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content,'lxml')
    print(soup.prettify())