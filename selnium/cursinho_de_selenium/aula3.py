#modificando o user agent
#site com user agents = https://developers.whatismybrowser.com/useragents/explore/

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

opts = Options()
opts.add_argument('user-agent=Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1')

url = "https://site112.com/qual-o-meu-user-agent"

driver = webdriver.Chrome(executable_path='bot/selnium/cursinho_de_selenium/chromedriver', chrome_options=opts)
driver.get(url)