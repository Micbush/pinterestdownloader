import requests
from bs4 import BeautifulSoup as soup

url = ''

r = requests.get(url).content

page_soup = soup(r, 'html.parser')
print(page_soup)

# soup = BeautifulSoup(r.text, "html.parser")
# # print(soup)

# container = soup.select_one("id_searchword")


# print(container)