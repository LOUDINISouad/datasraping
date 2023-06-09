import requests
from bs4 import BeautifulSoup

url = 'https://www.woolworths.com.au/'

response = requests.get(url).text

soup = BeautifulSoup(response, 'html.parser')

price = soup.find_all('div', class_="product-tile-price")
print(price)

