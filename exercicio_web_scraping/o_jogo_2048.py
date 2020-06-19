'''
Objetivos:

1) Clicar no Try Again para continuar jogando.
2) Tentar outra técnica para conseguir uma pontuação maior.
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import randint

browser = webdriver.Chrome(executable_path='./chromedriver_linux64/chromedriver')
browser.get('https://gabrielecirulli.github.io/2048/')


corpo_pagina = browser.find_element_by_tag_name('body')

# teclas que o jogo aceita
direcoes = {0: Keys.UP, 1: Keys.RIGHT, 2: Keys.DOWN, 3: Keys.LEFT}


# seleciona o jogo clicando na tela para poder enviar as teclas
browser.find_element_by_class_name('grid-container').click()

# fica enviado teclas para o jogo
while True:
	try:
		print("Jogando....")
		corpo_pagina.send_keys(direcoes[randint(0,3)])
		browser.find_element_by_class_name("reset-button").click()
	except:
		prinreset-button("Nunca termina")