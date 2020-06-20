from selenium import webdriver

url = 'http://www.practiceselenium.com/welcome.html'

driver = webdriver.Chrome('bot/scrapy/cursinho_web_scraping/chromedriver')

driver.get(url)

button = driver.find_element_by_xpath('//*[@id="wsb-button-00000000-0000-0000-0000-000450914890"]/span')
button.click()

titulo1 = driver.find_element_by_xpath('//*[@id="wsb-element-00000000-0000-0000-0000-000453230000"]/div/p').text
texto1 = driver.find_element_by_xpath('//*[@id="wsb-element-00000000-0000-0000-0000-000451934628"]/div/pre').text

titulo2 = driver.find_element_by_xpath('//*[@id="wsb-element-00000000-0000-0000-0000-000453231072"]/div/p').text
texto2 = driver.find_element_by_xpath('//*[@id="wsb-element-00000000-0000-0000-0000-000451941184"]/div/pre').text

titulo3 = driver.find_element_by_xpath('//*[@id="wsb-element-00000000-0000-0000-0000-000453231735"]/div/p').text
texto3 = driver.find_element_by_xpath('//*[@id="wsb-element-00000000-0000-0000-0000-000451944022"]/div/pre').text

print(f'1- {titulo1}')
print(f'2- {titulo2}')
print(f'3- {titulo3}')

menuopc = int(input('Qual opção desejada: '))
if menuopc == 1:
    print(f'===DESCRIÇÃO DO PRODUTO {titulo1}')
    print(texto1)
elif menuopc == 2:
    print(f'===DESCRIÇÃO DO PRODUTO {titulo2}')
    print(texto2)
elif menuopc == 3:
    print(f'===DESCRIÇÃO DO PRODUTO {titulo3}')
    print(texto3)
else:
    print('Digite uma opção valida')