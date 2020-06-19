from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import platform
import time
import getpass
import sys
import sys
import os
import random





#   para não pedir confirmação de uso de camera e microfone 
chrome_configurações = Options()
chrome_configurações.add_argument("--use-fake-ui-for-media-stream")

#   reiniciará o programa

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)


#   abre o navegador com as especificações para o visitante
def aluno_visitante(nome_visitante):
    iteracao = 5
    while iteracao < 6:
        try:
            campo = navegador.get("https://us.bbcollab.com/guest/d3c0bb8b107d4c9092488ff4f6383be7")
            print("[OK] - Ava iniciado com sucesso!")
            break
        except:
            print(f"[ERROR] - Aula não encontrada!- O programa será reiniciado em [{iteracao}].")
            time.sleep(iteracao)
            iteracao -= 1
            if iteracao == 0:
                restart_program()

    # preenche o campo nome
    iteracao = 1
    while iteracao > 0:
        try:
            campo = navegador.find_element_by_id("guest-name")
            campo.send_keys(nome_visitante)
        except:
            print(f"[ERROR] Campo nome não encontrado. Outra tentativa acontecerá em {iteracao}")
            time.sleep(iteracao)
            iteracao += 1
        else:
            print('[OK] - Nome digitado com sucesso.')
            iteracao = 0    
    
    #   clica no botão next
    try:
        campo = navegador.find_element_by_xpath('//*[@id="launch-html-guest"]')
        campo.click()
    except:
        print('[ERROR] - Não foi possivel clicar no botão "next"')
        raise
    else:
        print("[OK] - Clique no botão next.")

    #   clica para fechar as configurações de audio e video
    try:
        time.sleep(10)
        campo = navegador.find_element_by_xpath('//*[@id="techcheck-modal"]/button')
        campo.click()
    except:
        print('[ERROR] - Não foi possivel fechar a configuração de audio e video')
        raise
    else:
        print("[OK] - Configuração de audio e video fechada.")

    #   fecha o tutorial do collaborate
    try:
        time.sleep(10)
        campo = navegador.find_element_by_xpath('//*[@id="announcement-modal-page-wrap"]/button')
        campo.click()
    except:
        print('[ERROR] - Não foi possivel fechar o tutorial do ava.')
        raise
    else:
        print("[OK] - Tutorial do Collaborate fechado.")

    # clica na aba '<<'
    try:
        time.sleep(10)
        campo = navegador.find_element_by_xpath('//*[@id="side-panel-open"]')
        campo.click()
    except:
        print('[ERROR] - Não abrir a aba do chat.')
        raise
    else:
        print("[OK] - Aba lateral aberta.")

    # clica na aba todos
    try:
        time.sleep(10)
        campo = navegador.find_element_by_xpath('//*[@id="chat-channel-scroll-content"]/ul/li/ul/li')
        campo.click()
    except:
        print("[ERROR] - Não foi possivel clicar no campo 'TODOS'.")
    else:
        print("[OK] - Clicado em 'TODOS'.")


    #   Abre arquivo de mensagem
    arquivo = open('frases.txt', 'r')
    linhas = arquivo.read()

    for j in range(len(linhas)):
        frases = linhas.split('.')
    aux = []

    #   envia mensagens aleatorias
    for i in range(len(frases)):
        while (len(aux) < len(frases)):
            valor = random.choice(frases)
            while valor in aux:
                valor = random.choice(frases)
                time.sleep(3)

            # clicar no campo de mensagens e envia a mensagem
            while iteracao > 0:
                try:
                    time.sleep(10)
                    campo = navegador.find_element_by_id("message-input")
                    time.sleep(2)
                    campo.send_keys(valor)
                    campo.send_keys(Keys.ENTER)
                except:
                    print(f'[ERROR] - Não foi conseguido enviar a mensagem com sucesso {iteracao}')
                    iteracao += 1
                else:
                    print(valor)
                    aux += [valor]
                    print('[OK] - Mensagem enviada com sucesso')
                    iteracao = 0
            iteracao = 1

    # clica no quadro de participantes
    time.sleep(2)
    iteracao = 1
    while iteracao > 0:
        try:
            campo = navegador.find_element_by_xpath('//*[@id="panel-control-participants"]')
            campo.click()
        except:
            print(f'[ERROR] - Botão não encontrado, nova tentativa em: {iteracao}')
            time.sleep(iteracao)
            iteracao += 1
        else:
            print('[OK] - Clique no quadro de participantes.')
            iteracao = 0

    #   clica no campo chat
    time.sleep(2)
    iteracao = 1
    while iteracao > 0:
        try:
            campo = navegador.find_element_by_xpath('//*[@id="panel-control-activity"]')
            campo.click()

        except:
            print(f'[ERROR] - Campo chat não encontrado, nova tantativa em: {iteracao}')
            time.sleep(iteracao)
            iteracao += 1
        else:
            print('[OK] - Campo chat encontrado.')
            iteracao = 0

    #   clica no botao voltar
    time.sleep(2)
    iteracao = 1
    while iteracao > 0:
        try:
            campo = navegador.find_element_by_xpath('//*[@id="panel-back-button"]')
            campo.click()
        except:
            print(f'[ERROR] - Botão voltar não encontrado, nova tentativa em {iteracao}')
            time.sleep(iteracao)
            iteracao += 1
        else:
            print('[OK] - Botão voltar encontrado.')
            iteracao = 0    

    #   Abre o campo para pesquisar aluno
        try:
            campo = navegador.find_element_by_xpath('//*[@id="panel-chatchannelselector-content"]/header/div/div/div/input')
            campo.click()
            campo.send_keys('EDUARDO DE MORAIS LEVANDOVSKI')
            time.sleep(4)
            campo = navegador.find_element_by_xpath('//*[@id="chat-search-dropdown"]/li[2]/button/span')
            campo.click()
        except:
            print(f'[ERROR] - Aluno não foi encontrado')
            time.sleep(5)
            raise
        else:
            print('[OK] - Aluno encontrado com sucesso.')
            iteracao = 0
    
    # Envia a mensagem para o outro colega
        time.sleep(5)
        try:
            campo = navegador.find_element_by_id('message-input')
            time.sleep(2)
            campo.send_keys('Teste de Mensagem')
            campo.send_keys(Keys.ENTER)
            time.sleep(1)
            campo.send_keys('Até mais! Tenha uma boa noite!')
            campo.send_keys(Keys.ENTER)
        except:
            print(f'[ERROR] - Mensagem não enviada.')
            time.sleep(iteracao)
            iteracao += 1
        else:
            print('[OK] - Mensagem enviada.')


#   função para logar no ava-----------------------------------------------------------------------
def logar_ava(usuario, senha, data):
    iteracao = 5
    while iteracao < 6:
        try:
            navegador.get("https://www.univel.br/ava")
            print("[OK] - Ava iniciado com sucesso!")
            break
        except:
            print(f"[ERROR] - Ava não foi iniciado no Chrome!- O programa será reiniciado em [{iteracao}].")
            time.sleep(iteracao)
            iteracao -= 1
            if iteracao == 0:
                restart_program()
    
    #   Digita no campo login e senha
    iteracao = 1
    while iteracao > 0:
        try:
            campo_login = navegador.find_element_by_xpath("//*[@id='formAva']/form/div[1]/input")
            campo_login.send_keys(usuario)
            
            campo_senha = navegador.find_element_by_xpath("//*[@id='formAva']/form/div[2]/input")
            campo_senha.send_keys(senha)
        except:
            print('[ERROR] - Campo de Login ou senha não encontrados!. Outra tentativa acontecerá em %d' % (iteracao))
            time.sleep(iteracao)
            iteracao += 1
        else:
            print('[OK] - Login e Senha digitados com sucesso!')
            iteracao = 0
    
    #   Clica no botão login
    try:
        clique = navegador.find_element_by_xpath("//*[@id='formAva']/form/div[4]/input")
        clique.click()
    except:
        status = str(input("[ERROR] - Login não foi efetuado com sucesso! Deseja iniciar o programa novamente? [s/n]"))
        if status == 's':
            navegador.refresh()
            time.sleep(10)
            restart_program()
        else:
            print("[FATAL ERROR] - O programa morreu! Infelizmente caso você não digite sua senha corretamente, o programa não irá para frente!")
            raise
    else:
        print("[OK] - Login efetuado com sucesso!")
    
    #   clica na materia de programação visual
    time.sleep(5)
    iteracao = 1
    while iteracao > 0:
        try:
            clique = navegador.find_element_by_xpath('//*[@id="snap-pm-courses-current-cards"]/div[4]/div/h3/a')
            clique.click()
            print("[OK] - Abrindo materia de Programação Visual") 
        except:
            print(f"[ERROR] - Não foi possivel abrir a materia de Programação Visual! Outra tentativa em [{iteracao}]")
            time.sleep(iteracao)
            iteracao += 1
        else:
            iteracao = 0

    #   abre a aula
    time.sleep(5)
    try:
        clique = navegador.find_element_by_partial_link_text(data)
        clique.click()
        time.sleep(5)
    except:
        print(f"[ERROR] - Não foi possivel clicar na aula do dia[{data}].")
    else:
        print(f"[OK] - Abrindo a Aula do dia {data}.")

    #clica na sessão
    try:
        navegador.find_element_by_xpath("//div/a[@class='mod-link' and contains(@href, '%s')]").click()
    except:
        print("[ERROR] - Não foi possivel entrar na sessão da aula.")
    else:
        print("[OK] - Clique na sessão da aula.")

    # clica em 'participar da sessão'
    time.sleep(4)
    try:
        clique = navegador.find_element_by_xpath('//*[@id="maininfo"]/div/a')
        clique.click()
    except:
        print("[ERROR] - Nenhuma sessão ao vivo encontrada.")
        time.sleep(10)
        try:
            clique = navegador.find_element_by_xpath('//*[@id="region-main"]/div[1]/div[2]/ul/li/a[1]')
            clique.click()
            print("[OK] - Abrindo sessão de aula gravada.")
        except:
            print("[ERROR] - Não existe nenhuma aula para essa sessão.")
            print("[FATAL ERROR] - O programa irá reiniciar em 6 segundos.")
            time.sleep(6)
            navegador.close()
            restart_program()
    else:
        print("[OK] - Abrindo a sessão de aula.")

    # fecha a janela de configuração de audio e video.
    time.sleep(30)
    iteracao = 1
    while iteracao > 0:
        try:
            clique = navegador.find_element_by_xpath('//*[@id="techcheck-modal"]/button')
            clique.click()
            print("[OK] - Fechando janela de configuração do microfone e camera")
        except:
            print(f"[ERROR] - Não foi possivel fechar a janela de configuração de microfone e camera. Outra tentativa ocorrerá em [{iteracao}]")
            time.sleep(iteracao)
            iteracao += 1
        else:
            iteracao = 0
        
#   apresentação
print('''
         ____ __                %%%%%
          { --.\  |          .) Prova %
           '-._\\ | (\___   %)%% Do %(%%%
               `\\|{/ ^ _)-%(% Segundo %%%
           .'^^^^^^^  /`    %% Bimestre %'
          //\   ) ,  /       '%%%%(%%%%'
    ,  _.'/  `\<-- \<           %%%%%%
     `^^^`     ^^   ^^            
''')

"""
----Descrição das Funcionalidades feitas pelo scritp----
- Logar no Ava com a sua conta
- Entrar na sala de aula da materia de Programação Visual
- Entrar na aula desejada
- Enviar mensagens aleatorias no chat
- Enviar uma mensagem a um colega em seu chat privado da sala de aula

"""


#   Digitar se quer entrar como visitante o ou login de aluno.
tipo_aula = str(input("Deseja entrar como? [egresso/visitante]: "))

# se entrar como visitante
if tipo_aula == 'visitante':
    visitante = str(input("Olá visitante! Digite seu nome: "))
    try:
        if platform.system() == 'Linux':
            navegador = webdriver.Chrome(executable_path='./chromedriver_linux64/chromedriver', options=chrome_configurações)
            print("\n[OK] - Chrome iniciado no sistema: Linux")
        else:
            navegador = webdriver.Chrome(executable_path='./chromedriver_linux64/chromedriver.exe', options=chrome_configurações)
            print("[OK] - Chrome iniciado no sistema: Windows")
    except:
        print("[ERROR] - Chrome não foi inciado!")
        raise("[FATAL ERROR] - reinicie o programa!")
    aluno_visitante(visitante)

#   se entrar como aluno
elif tipo_aula == 'egresso':
    #   Solicita o usuario e a senha do AVA 
    usuario_ava = str(input("Digite seu login do AVA: "))

    #   Senha não irá aparecer pois está camuflada
    senha_ava = getpass.getpass("Digite sua senha do AVA: ")

    #   numero da aula que quer entrar
    data_aula = str(input("Digite o dia e o mes da aula que quer acessar [00/00]: "))

    #   inicia o google
    try:
        if platform.system() == 'Linux':
            navegador = webdriver.Chrome(executable_path='./chromedriver_linux64/chromedriver', options=chrome_configurações)
            print("\n[OK] - Chrome iniciado no sistema: Linux")
        else:
            navegador = webdriver.Chrome(executable_path='./chromedriver_linux64/chromedriver.exe', options=chrome_configurações)
            print("[OK] - Chrome iniciado no sistema: Windows")
    except:
        print("[ERROR] - Chrome não foi inciado!")
        raise("[FATAL ERROR] - reinicie o programa!")
    
    logar_ava(usuario_ava, senha_ava, data_aula)

#   caso não logue com aluno e com visitante.    
else:
    entrada = str(input(f'[ERROR] - "{tipo_aula}" - Não é um tipo de entrada aceitavel, voce deve digitar apenas, egresso caso tenha login no AVA\n ou visitante caso não tenha login no AVA, deseja tentar novamente? [s/n]'))
    if entrada == 's':
        print("[RELOADING] - O programa irá reiniciar, conte 5 segundos.")
        time.sleep(5)
        restart_program()
    else:
        print("[GOOD BAY] - Até um proximo código.")




