from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import platform
import time

# para não pedir confirmação de uso de camera e microfone 
chrome_options = Options()
chrome_options.add_argument("--use-fake-ui-for-media-stream")


# Abrir o navegador com o driver correto
if platform.system() == 'Linux':
	browser = webdriver.Chrome(executable_path='./driver/chromedriver', options=chrome_options) # Linux
else:
	browser = webdriver.Chrome(executable_path='./driver/chromedriver.exe', options=chrome_options) # Windows

# abre o link do AVA para a sala desejada
browser.get("https://us.bbcollab.com/guest/d3c0bb8b107d4c9092488ff4f6383be7")

control = 1
while control > 0:
	try:
		nomeElem = browser.find_element_by_id("guest-name")
		nomeElem.send_keys("Joao da Silva Bot")
	except:
		print('[ERROR] Campo nome não encontrado. Outra tentativa acontecerá em %d' % (control))
		time.sleep(control)
		control += 1
	else:
		print('[OK] - Nome digitado com sucesso.')
		control = 0


# clica no botão next
nomeElem = browser.find_element_by_xpath('//*[@id="launch-html-guest"]')
nomeElem.click()

# fecha a configuração de audio e vídeo
time.sleep(10)
nomeElem = browser.find_element_by_xpath('//*[@id="techcheck-modal"]/button')
nomeElem.click()

# fecha o tutorial do AVA
time.sleep(10)
nomeElem = browser.find_element_by_xpath('//*[@id="announcement-modal-page-wrap"]/button')
nomeElem.click()


# clicar na aba
time.sleep(10)
nomeElem = browser.find_element_by_xpath('//*[@id="side-panel-open"]')
nomeElem.click()


# clicar em todos
time.sleep(10)
nomeElem = browser.find_element_by_xpath('//*[@id="chat-channel-scroll-content"]/ul/li/ul/li')
nomeElem.click()



# clicar no campo escrever a mensagem e enviar
time.sleep(10)
nomeElem = browser.find_element_by_id("message-input")
time.sleep(2)
nomeElem.send_keys('Professor já fez chamada?')
nomeElem.send_keys(Keys.ENTER)