# Eduardo de Morais Levandovski.
# limpar o console -----------------------------------------------------
import os
os.system('cls||clear')
print('\n')
# ----------------------------------------------------------------------
from googletrans import Translator
import googletrans
import json

encoding='utf-8'


#Abrindo o arquivo de texto escrito.
nome_arquivo = "nome_do_arquivo.txt"
arquivo_texto = open(nome_arquivo)


texto_do_arquivo = arquivo_texto.read()

translator = Translator()

#Idioma em que se econtra o texto.
idioma_do_arquivo = translator.detect(texto_do_arquivo)
print(f"Nome do arquivo: {nome_arquivo}\nIdioma do arquivo: {idioma_do_arquivo}\n")


#Menu com possiveis idiomas.
print(json.dumps(googletrans.LANGUAGES, indent=4))

#Solicitação que o usuario escolha uma linguagem.
idioma_escolhido = str(input("Escolha um dos idiomas acima e digite a silga correspondente: "))

#Tradução do arquivo para a linguagem escolhida.
traduzindo_arquivo = str(translator.translate(texto_do_arquivo, dest=idioma_escolhido))

#Criando o arquivo caso não exista.
try:
    os.makedirs("./exercicio_traducao/nome_do_arquivo_traduzido.txt")
except:
    nome_do_arquivo_traduzido = open("nome_do_arquivo_traduzido.txt", "w")

#Salvando o arquivo traduzido no arquivo criado.
nome_do_arquivo_traduzido.write(traduzindo_arquivo)


arquivo_texto.close()
nome_do_arquivo_traduzido.close()

