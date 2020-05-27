import os
os.system('cls||clear')
print('\n')
# ----------------------------------------------------------------------

import requests, bs4

res = requests.get("https://www.climatempo.com.br/previsao-do-tempo/amanha/cidade/268/cascavel-pr")

page = bs4.BeautifulSoup(res.text, 'html.parser')
termometro1 = page.select('.max-temp')
termometro2 = page.select('.min-temp')


temperatura_max = termometro1[0].getText()
temperatura_min = termometro2[0].getText()

print(f"Temperatura maxima: {temperatura_max}\nTemperatura Minima: {temperatura_min}")

