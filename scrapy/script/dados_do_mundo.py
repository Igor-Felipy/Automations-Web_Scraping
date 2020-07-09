from selenium import webdriver
from time import sleep
url = 'https://www.worldometers.info/pt/'

driver = webdriver.Chrome('bot/scrapy/script/chromedriver')
driver.get(url)
sleep(3)
population = driver.find_element_by_xpath('//*[@id="tablemore"]/tbody/tr[2]/td[1]/div/span').text
born_this_year = driver.find_element_by_xpath('//*[@id="tablemore"]/tbody/tr[3]/td[1]/div/span').text
born_today = driver.find_element_by_xpath('//*[@id="tablemore"]/tbody/tr[5]/td[1]/div/span').text
death_this_year = driver.find_element_by_xpath('//*[@id="tablemore"]/tbody/tr[7]/td[1]/div/span').text
death_today = driver.find_element_by_xpath('//*[@id="tablemore"]/tbody/tr[8]/td[1]/div/span').text
expansion_pop = driver.find_element_by_xpath('//*[@id="tablemore"]/tbody/tr[9]/td[1]/div/span').text
sleep(2)
print("População Atual: " + population)
print("Nascidos esse ano: " + born_this_year)
print("Nascidos hoje: " + born_today)
print("Mortos esse ano: " + death_this_year)
print("mortos hoje: " + death_today)
print("crescimento da população esse ano: " + expansion_pop)