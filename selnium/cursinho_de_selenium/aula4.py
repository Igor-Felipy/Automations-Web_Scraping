from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import random

listaua = [
    'Mozilla / 5.0 CK = {} (Windows NT 6.1; WOW64; Trident / 7.0; rv: 11.0) like Gecko',
    'Mozilla / 5.0 (Windows NT 10.0; Win64; x64) AppleWebKit / 537.36 (KHTML, like Gecko) Chrome / 74.0.3729.169 Safari / 537.36',
    'Mozilla / 5.0 (Windows NT 10.0; WOW64) AppleWebKit / 537.36 (KHTML, like Gecko) Chrome / 72.0.3626.121 Safari / 537.36',
    'Mozilla / 5.0 (Windows NT 10.0; Win64; x64) AppleWebKit / 537.36 (KHTML, like Gecko) Chrome / 74.0.3729.157 Safari / 537.36',
    'Mozilla / 4.0 (compatível; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)',
    'Mozilla / 4.0 (compatível; MSIE 6.0; Windows NT 5.1; SV1)',
    'Mozilla / 5.0 (Windows NT 10.0; Win64; x64) AppleWebKit / 537.36 (KHTML, like Gecko) Chrome / 60.0.3112.113 Safari / 537.36',
    'Mozilla / 5.0 (Windows NT 6.1; WOW64; Trident / 7.0; rv: 11.0) like Gecko',
    'Mozilla / 5.0 (X11; Linux x86_64) AppleWebKit / 537.36 (KHTML, like Gecko) Chrome / 44.0.2403.157 Safari / 537.36',
    'Mozilla / 5.0 (X11; Ubuntu; Linux i686; rv: 24.0) Gecko / 20100101 Firefox / 24.0',
    'Apache / 2.4.34 (Ubuntu) OpenSSL / 1.1.1 (conexão fictícia interna)',
    'Thunderstorm/1.0 (Linux)',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a1) Gecko/20070308 Minefield/3.0a1',
    'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Thunderbird/45.8.0',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; en-en) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/534.59.10 (KHTML, like Gecko) Version/5.1.9 Safari/534.59.10',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0',
    'Mozilla / 5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit / 605.1.15 (KHTML, like Gecko)',
    'Mozilla / 5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit / 605.1.15 (KHTML, like Gecko)',
    'Mozilla / 5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit / 605.1.15 (KHTML, like Gecko)',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/603.3.8 (KHTML, like Gecko)'
]

while True:
    try:    
        UA = random.choice(listaua)
        opts = Options()
        opts.add_argument('user-agent=' + UA)

        url = 'https://www.ferendum.com/pt/PID426480PSD1532455333'

        driver = webdriver.Chrome(executable_path='bot/selnium/cursinho_de_selenium/chromedriver',chrome_options=opts)
        driver.get(url)

        digitanome = driver.find_element_by_xpath('/html/body/spamtrap/main/div[3]/div/div/form/div[1]/table/tbody[1]/tr[1]/td[3]/input')
        digitanome.click()
        digitanome.send_keys('Camila')

        escolheopc = driver.find_element_by_xpath('/html/body/spamtrap/main/div[3]/div/div/form/div[1]/table/tbody[1]/tr[2]/td[3]/input')
        escolheopc.click()

        botao = driver.find_element_by_xpath('/html/body/spamtrap/main/div[3]/div/div/form/div[1]/table/tbody[2]/tr[1]/td[3]/input')
        botao.click()
    except:
        continue
