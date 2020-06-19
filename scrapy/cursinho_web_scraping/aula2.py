from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from time import sleep
url = "https://www.coronatracker.com/pt-br/"

driver = webdriver.Chrome('bot/scrapy/cursinho_web_scraping/chromedriver')
driver.get(url)
sleep(5)

cases = driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/span').text
rec = driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/span').text
death = driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/span').text


print(f'Casos confirmados: {cases} \nRecuperados: {rec} \nMortos: {death}')