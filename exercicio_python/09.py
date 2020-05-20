# Consegui fazer sozinho :)
# 09) Utilizando listas faça um programa que faça 5 perguntas para uma pessoa 
# sobre um crime. As perguntas são:
# a) "Telefonou para a vítima?"
# b) "Esteve no local do crime?"
# c) "Mora perto da vítima?"
# d) "Devia para a vítima?"
# e) "Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a participação da 
# pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve 
# ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como
# "Assassino". Caso contrário, ele será classificado como "Inocente".

points = []
score = 0
questions = ["A) Telefonou para a vítima? ", "B) Esteve no local do crime? ", "C) Mora perto da vítima? ", "D) Devia para a vítima? ", "E) Já trabalhou com a vitima? "]
print("Digitem (s) para sim ou (n) para não: \n")

while True:
    for i in range(5):
        print(questions[i])
        answer = input()
        points.append(answer)
        if answer == 's':
            score += 1
    break      
if score == 2:
    print("Você é Suspeita")
elif score > 3 and score < 4:
    print("Você é complice")
elif score == 5:
    print("\n Você é o assasino")

else:
    print("Você é inocente")

