from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
url = 'http://www.practiceselenium.com/welcome.html'

driver = webdriver.Chrome('bot/scrapy/cursinho_web_scraping/chromedriver')

driver.get(url)
sleep(3)

button1 = driver.find_element_by_xpath('//*[@id="wsb-button-00000000-0000-0000-0000-000450914890"]/span')
button1.click()
sleep(1)

button2 = driver.find_element_by_xpath('//*[@id="wsb-button-00000000-0000-0000-0000-000451955160"]')
button2.click()
sleep(1)

email = driver.find_element_by_xpath('//*[@id="email"]')
email.send_keys('teste@email.com')
sleep(1)

name = driver.find_element_by_xpath('//*[@id="name"]')
name.send_keys('igor felipy')
sleep(1)

address = driver.find_element_by_xpath('//*[@id="address"]')
address.send_keys('rua 10')
sleep(1)

kind_card = driver.find_element_by_xpath('//*[@id="card_type"]/option[3]')
kind_card.click()
sleep(1)

card_number = driver.find_element_by_xpath('//*[@id="card_number"]')
card_number.send_keys('00000000000')
sleep(1)

titular_name = driver.find_element_by_xpath('//*[@id="cardholder_name"]')
titular_name.send_keys('igor felipy')
sleep(1)

CVV = driver.find_element_by_xpath('//*[@id="verification_code"]')
CVV.send_keys('123')
sleep(1)

finish = driver.find_element_by_xpath('//*[@id="wsb-element-00000000-0000-0000-0000-000452010925"]/div/div/form/div/button')
finish.click()