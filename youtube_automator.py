from selenium import webdriver
import time
a = 'flow fla flu'
driver = webdriver.Chrome(executable_path=r'./chromedriver')
driver.get('https://www.youtube.com/')
#//*[@id="search"] barra de pesquisa
#//*[@id="search-icon-legacy"] botao de pesquisa
#//*[@id="video-title"]/yt-formatted-string primeiro video
time.sleep(5)
barra = driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]')
barra.click()
time.sleep(3)

barra.send_keys(a)

pesquisar = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
pesquisar.click()