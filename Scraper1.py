import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(response.text, 'html.parser')
response = requests.get('https://www.woolworths.com.au/')

if response.status_code == 200:
    table = soup.findAll("table",attrs={"class":"infobox_v2 noarchive"})
    prices = soup.find_all('span', class_='price-dollars')  
  