from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='bot/selnium/cursinho_de_selenium/chromedriver')
driver.get('https://web.whatsapp.com/')

quant = int(input('digite a quantidade: '))
mensagem = input('Qual mensagem voce deseja enviar: ')
grupo = input('Nome do grupo')

for i in range(quant):
    print('QR CODE OK')
    grupo = driver.find_element_by_xpath(f"//span[@title='{grupo}']")#xpath do grupo
    grupo.click()
    inputtext = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')#xpath do input
    inputtext.send_keys(mensagem)
    botao = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]')#xpath do enviar
    botao.click()
    print(f"Foram enviados {i} mensagens")