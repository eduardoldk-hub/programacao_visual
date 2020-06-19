from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import platform
import time
import getpass
import sys
import os

# reinicia programa ---------------------------------------
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)


#   aprensentação do console    ----------------------------------------------
print("""

------------------ SEJA BEM VINDO A PROVA DO SEGUNDO BIMESTRE ----------------------------------------------------------------------------------------------------------

                        [_]___[_]__[_]___[_]
                        [__#__][__I_]__I__#]
                        [_I_#_I__#[__]__#__]
                            [_]_#_]__I_#_]    (Aprovação)
                            [I_|/ _W_ \|#]     /
                            [#_||{(")} -------/
                            [_I||{/~\}||_]
                            [__]|/\_/\||#]
                            [_I__I#___]__]
            (Eduardo)       [__I_#_I___#_]
            /               [#__I____]__I]
       .-. /                [__I_#__I__[_]
     __|=|__                [_#_[__#_]__#]
    (_/`-`\_)               [__#_I__[#_I_]
    //\___/\\               [_I__]__#_I__]
    <>/   \<>               [#__I__#_]__I]
     \|_._|/                [_I#__I___I_#]    .:.
      <_I_>                 [#__I__]_#___]   -=o=-
       |||                  [_I__I#__]___]    ':'
      /_|_\               \\[__]#___][__#]//, \|/
 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

""")

"""
----Descrição das Funcionalidades feitas pelo scritp----
- Logar no Ava com a sua conta
- Entrar na sala de aula da materia de Programação Visual
- Entrar na aula desejada
- Enviar mensagens aleatorias no chat
- Enviar uma mensagem a um colega em seu chat privado da sala de aula

"""



#   Não pedirá confirmação de acesso ao microfone e a camera.
chrome_configurações = Options()
chrome_configurações.add_argument("--use-fake-ui-for-media-stream")


#   Solicita o usuario e a senha do AVA
usuario_ava = str(input("Digite seu login do AVA: "))
#Senha não irá aparecer pois está camuflada
senha_ava = getpass.getpass("Digite sua senha do AVA: ")


#   ----------------------- Abre o navegador com o drive correto-----------------------
try:
    if platform.system() == 'Linux':
        navegador = webdriver.Chrome(executable_path='./chromedriver_linux64/chromedriver', options=chrome_configurações)
        print("\n[OK] - Chrome iniciado no sistema: Linux")
    else:
        navegador = webdriver.Chrome(executable_path='./chromedriver_linux64/chromedriver.exe', options=chrome_configurações)
        print("[OK] - Chrome iniciado no sistema: Windows")
except:
    print("[Erro] - Chrome não foi inciado!")


#   ----------------------- Abre o AVA -----------------------
try:
    navegador.get("https://www.univel.br/ava")
    print("[OK] - Ava iniciado com sucesso!")
except:
    print("[ERROR] - Ava não foi iniciado no Chrome! - Verifique sua conexão com a internet.")



iteracao = 5
while iteracao < 5:
	try:
		campo_login = navegador.find_element_by_xpath("//*[@id='formAva']/form/div[1]/input")
		campo_login.send_keys(usuario_ava)
		campo_senha = navegador.find_element_by_xpath("//*[@id='formAva']/form/div[2]/input")
		campo_senha.send_keys(senha_ava)
        clique = navegador.find_element_by_xpath("//*[@id='formAva']/form/div[4]/input")
	except:
		print('[ERROR] - Senha ou login foram digitados incorretamente!. Outra tentativa acontecerá em %d' % (iteracao))
		iteracao -= 1
		print('[OK] - Login e Senha digitados com sucesso!')
		iteracao = 5





#   ----------------------- clica na materia de Programação Visual -----------------------
time.sleep(5)
iteracao = 1
while iteracao > 0:
    try:
        clique = navegador.find_element_by_xpath('//*[@id="snap-pm-courses-current-cards"]/div[4]/div/h3/a')
        clique.click()
        print("[OK] - Abrindo materia de Programação Visual") 
    except:
        print(f"[ERRO] - Não foi possivel abrir a materia de Programação Visual! Outra tentativa em [{iteracao}]")
        time.sleep(iteracao)
        iteracao += 1
    else:
        iteracao = 0


       
#   ----------------------- clica na Aula Teste - Bots Selenium. -----------------------
time.sleep(5)
try:
    clique = navegador.find_element_by_xpath('//*[@id="module-72084"]/div/div/div[2]/h3/a/p')
    clique.click()
    print("[OK] - Abrindo a sala de aula 'Aula Teste - Bots Selenium'")
except:
    print("[ERRO] - Não foi possivel abrir a sala de aula.")


#   ----------------------- clica em 'participar da sessão' -----------------------
time.sleep(4)
iteracao = 1
while iteracao > 0:
	try:
		clique = navegador.find_element_by_xpath('//*[@id="maininfo"]/div/a')
		clique.click()
	except:
		print(f"[ERRO] - Não foi possivel abrir a sessão dessa sala de aula. Outra tentativa ocorrerá em [{iteracao}]")
		time.sleep(iteracao)
		iteracao += 1
	else:
		print("[OK] - Abrindo a sessão")
		iteracao = 0


#   ----------------------- fecha a janela de configuração de audio e video -----------------------
time.sleep(30)
iteracao = 1
while iteracao > 0:
    try:
        clique = navegador.find_element_by_xpath('//*[@id="techcheck-modal"]/button')
        clique.click()
        print("[OK] - Fechando janela de configuração do microfone e camera")
    except:
        print(f"[ERRO] - Não foi possivel fechar a janela de configuração de microfone e camera. Outra tentativa ocorrerá em [{iteracao}]")
        time.sleep(iteracao)
        iteracao += 1
    else:
        iteracao = 0



#   ----------------------- clica na aba do chat -----------------------
time.sleep(10)
clique = navegador.find_element_by_xpath('//*[@id="side-panel-open"]')
clique.click()

#   ----------------------- clica no chat de TODOS os participantes.-----------------------
time.sleep(10)
clique = navegador.find_element_by_xpath('//*[@id="channel-item-ac691d96-9a40-4b1a-9eee-c16c98b88305"]/span')
clique.click()


# ----------------------- clica no local de escrever mensagem e envia ----------------------- 
time.sleep(10)
clique = navegador.find_elements_by_id("menssage-input")
time.sleep()
clique.send_keys("Boa noite?")
