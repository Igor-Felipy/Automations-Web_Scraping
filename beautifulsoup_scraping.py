from bs4 import BeautifulSoup
import requests

url = 'https://www.python.org/'
r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

#print(soup) retorna todo o html

soup.find('div', class_ = 'small-widget') #retorna uma div inteira

soup.find('div',attrs={'class':'small-widget'}) #tambem retorna uma div inteira

soup.find('div', class_ = 'small-widget').h2 #retorna uma tag dentro da div

soup.find('div', class_ = 'small-widget').h2.text #retorna só o texto do elemento

soup.find('div', class_ = 'small-widget').h2.next_element #retorna o proximo elemento dentro da tag

soup.find('div', class_ = 'small-widget').h2.next_sibling.next_sibling #retorna o proximo elemento da hierarquia

