from bs4 import BeautifulSoup
import requests
import csv

csv_file = open('fornecedores.csv','w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['id','empresa','telefone','site','email'])

url = 'http://www.abimad.com.br/associados/pesquisar/id_produto=/uf=#menu-top'

r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

#print(soup) teste de funcionalidade do request

soup.find('figure')

empresa = soup.find('figure').h5.text

telefone = soup.find('figure').find('i', class_ = 'fa-phone').next_element.next_element.text

print(telefone)

site = soup.find('figure').find('i', class_ = 'fa-link').next_element.next_element.text

print(site)

email = soup.find('figure').find('i', class_ = 'fa-at').next_element.next_element.text

print(email)

todos_elementos = soup.find_all('figure')
id = 0
for elemento in todos_elementos:
    empresa = elemento.h5.text
    telefone = elemento.find('i', class_ = 'fa-phone').next_element.next_element.text
    site = elemento.find('i', class_ = 'fa-link').next_element.next_element.text
    email = elemento.find('i', class_ = 'fa-at').next_element.next_element.text

    print('='*20)
    print(f'Empresa: {empresa}')
    print(f'Telefone: {telefone}')
    print(f'Site: {site}')
    print(f'E-mail: {email}')
    print('='*20)
    csv_writer.writerow([id, empresa, telefone, site, email])

    id+=1
csv_file.close()

