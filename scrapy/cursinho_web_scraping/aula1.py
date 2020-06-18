import requests
from bs4 import BeautifulSoup

url = ('https://multicanais.com/tvonline/')

r = requests.get(url)
html_content = r.text
soup = BeautifulSoup(html_content, 'html.parser')
lista_title = soup.find_all('title')
for lista_dados in lista_title:
    print('Nome Do Site: ')
    print(lista_dados.next_element)
    print('='*55)