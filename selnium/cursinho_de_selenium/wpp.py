from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='bot/selnium/cursinho_de_selenium/chromedriver')
driver.get('https://web.whatsapp.com/')
