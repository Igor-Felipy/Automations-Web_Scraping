#Clicando em coisas

from selenium import webdriver

url = "https://www.ferendum.com/pt/PID410151PSD575674591"

driver = webdriver.Chrome('bot/selnium/cursinho_de_selenium/chromedriver')
driver.get(url)

escolheopc = driver.find_element_by_xpath('/html/body/spamtrap/main/div[3]/div/div/table/tbody/tr[3]/td[1]/input')
escolheopc.click()

env = driver.find_element_by_xpath('/html/body/spamtrap/main/div[3]/div/div/table/tbody/tr[6]/td[2]/input')
env.click()
#outra opção para encontrar alguma  coisa é procurar pela classe com o comando find_element_by_class_name()
