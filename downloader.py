import requests
from bs4 import BeautifulSoup

url = 'https://pin.it/7FMDwRS'

r = requests.get(url)
# print(r)

soup = BeautifulSoup(r.text, "html.parser")
# print(soup)

container = soup.select_one("mainContainer")


print(container)