from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.chrome.options import Options

a = 'flow fla flu'

opts = Options()
opts.add_argument('user-agent=Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1')

driver = webdriver.Chrome(executable_path='bot/selnium/scripts/chromedriver', chrome_options=opts)
driver.get('https://www.youtube.com/')
#//*[@id="search"] barra de pesquisa
#//*[@id="search-icon-legacy"] botao de pesquisa
#//*[@id="video-title"]/yt-formatted-string primeiro video
sleep(5)
barra = driver.find_element_by_xpath('//*[@id="header-bar"]/header/div/button/c3-icon')
sleep(1)
barra.click()
sleep(1)
barra.send_keys(a)
sleep(3)
pesquisar = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
pesquisar.click()