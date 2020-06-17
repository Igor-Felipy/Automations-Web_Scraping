from selenium import webdriver
from random import choice
PROXY = [
    "177.55.207.38:8080",
    "187.65.203.245:80",
    "200.219.152.226:3128",
    "201.28.39.6:3128",
    "200.222.211.54:8080"
]

opts = webdriver.ChromeOptions()
opts.add_argument(f'--proxy-server=http://{choice(PROXY)}')

chrome = webdriver.Chrome(executable_path='bot/selnium/cursinho_de_selenium/chromedriver', chrome_options=opts)
chrome.get("https://www.meuip.com.br/")