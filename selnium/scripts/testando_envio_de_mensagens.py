from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

url = 'https://web.whatsapp.com/'

msg = 'msg de teste de automação, por favor ignore!'

driver = webdriver.Chrome('bot/selnium/scripts/chromedriver')
driver.get(url)
sleep(8)

name = 'Mãe'
grupo = driver.find_element_by_xpath(f"//span[@title='{name}']")
grupo.click()
sleep(1)

texto = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
texto.click()
sleep(1)
texto.send_keys(msg)
sleep(1)

enviar = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]')
enviar.click()