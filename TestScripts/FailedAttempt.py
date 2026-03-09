import requests
from bs4 import BeautifulSoup

def Scrape ():
    url = 'https://example.com'

    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    print(soup)

if __name__ == '__main__':
    Scrape()