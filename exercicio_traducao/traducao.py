# limpar o console -----------------------------------------------------
import os
os.system('cls||clear')
print('\n')
# ----------------------------------------------------------------------
from googletrans import Translator
import googletrans
import json

encoding='utf-8'


nome_arquivo = "nome_do_arquivo.txt"
arquivo_texto = open(nome_arquivo)


texto_do_arquivo = arquivo_texto.read()

translator = Translator()
idioma_do_arquivo = translator.detect(texto_do_arquivo)


print(f"Nome do arquivo: {nome_arquivo}\nIdioma do arquivo: {idioma_do_arquivo}\n")


tabela_de_idiomas = (json.dumps(googletrans.LANGUAGES))
print(tabela_de_idiomas)
idioma_escolhido = str(input("Escolha um dos idiomas acima e digite a silga correspondente: "))


traducao_arquivo = translator.translate(texto_do_arquivo, dest=idioma_escolhido)

os.makedirs("./exercicio_traducao/nome_do_arquivo_traduzido.txt")



arquivo_texto.close()
arquivo_texto_traduzido.close()

