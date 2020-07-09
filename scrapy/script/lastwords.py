from requests import get
from bs4 import BeautifulSoup

url = "http://www.planecrashinfo.com/lastwords.htm"

html = get(url)

soup = BeautifulSoup(html.content, 'html.parser')

data = soup.find_all('tr')

for word in data:
    td = word.find('td').next_element.next_element.next_element.next_element.next_element
    td2 = soup.find("//*[@id=\"AutoNumber1\"]/tbody/tr[57]/td[5]/font/font")
    print(td2)