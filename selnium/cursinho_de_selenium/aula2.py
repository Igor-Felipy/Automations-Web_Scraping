from selenium import webdriver
from selenium.webdriver.common.keys import Keys
url = 'https://google.com'

driver = webdriver.Chrome('bot/selnium/cursinho_de_selenium/chromedriver')
driver.get(url)

caixa = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
caixa.click()
caixa.send_keys('teste \n')