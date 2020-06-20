from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from time import sleep
import smtplib

url = "https://www.coronatracker.com/pt-br/"

driver = webdriver.Chrome('bot/scrapy/cursinho_web_scraping/chromedriver')
driver.get(url)
sleep(5)

cases = driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/span').text
rec = driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/span').text
death = driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/span').text


print(f'Casos confirmados: {cases} \nRecuperados: {rec} \nMortos: {death}')



def sendmail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('seu email', 'sua senha')

    subject = 'Corre que ficou ruim'
    body = 'CARA ACABOU DE ATINGIR: {} de casos confirmados, alem disso tambem {} morreram'.format(cases, death)
    msg = 'Subject: {} {}'.format(subject,body)
    server.sendmail(
        'seu email',
        'email de destino',
        msg
    )
    print('EMAIL ENVIADO COM URGENCIA')
    server.quit()



if cases >= "3.000.000":
    sendmail()
