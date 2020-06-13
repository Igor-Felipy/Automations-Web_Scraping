from selenium import webdriver
from time import sleep
google = webdriver.Chrome('bot/chromedriver')
google.get('http://google.com.br')

search = google.find_element_by_xpath("[@id=\"tsf\"]/div[2]/div[1]/div[1]/div/div[2]/input")
sleep(1)
search.click()
sleep(1)
search.send_keys('testando pesquiza')
sleep(1)
search.submit()