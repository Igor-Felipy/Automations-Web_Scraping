# -*- coding: utf-8 -*-
from selenium import webdriver
import time 

class WhatsappBot:
    def __init__(self):
        self.mensagem = "Essa mensagem é apenas um teste de automação em python, então por favor ignore essa menssagem!!"
        self.grupos = ["Projeto Integrado","4° Não foi com Varalda 👌"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'bot/chromedriver')

    def EnviarMensagem(self):
        #<span dir="auto" title="Projeto Integrado" class="_1wjpf _3NFp9 _3FXB1">Projeto Integrado</span>
        #<div tabindex="-1" class="_1Plpp">
        #<span data-icon="send" class="">

        self.driver.get('https://web.whatsapp.com/')
        time.sleep(30)
        for grupo in self.grupos:
            grupo = self.driver.find_element_by_xpath(f"//span[@title='{grupo}']")
            time.sleep(3)
            grupo.click()
            chat_box = self.driver.find_element_by_class_name('_1Plpp')
            time.sleep(3)
            chat_box.click()
            chat_box.send_keys(self.mensagem)
            botao_enviar = self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]')
            time.sleep(3)
            botao_enviar.click()
            time.sleep(5)


bot = WhatsappBot()
bot.EnviarMensagem