from bs4 import BeautifulSoup
import requests

url = 'https://www.worldometers.info/pt/'
r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

soup.find('tr')

print(soup.find('td', class_= 'title').next_sibling.next_sibling)