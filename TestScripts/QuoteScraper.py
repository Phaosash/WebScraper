import requests
from bs4 import BeautifulSoup
import csv
import time

base_url = "https://quotes.toscrape.com/page/"
data = []

for page in range (1, 6):
    url = base_url + str(page)
    response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
quotes = soup.find_all("div", class_="quote")

for quote in quotes:
    text = quote.find("span", class_="text").text
    author = quote.find("small", class_="author").text

data.append([text, author])

time.sleep(1)

with open("./Data/quotes.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Quote", "Author"])
    writer.writerows(data)

print("Scraping finished.")