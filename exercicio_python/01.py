# Consegui fazer sozinho :)
# 01) Tendo como dado de entrada a altura (h) de uma pessoa, construa um
# algoritmo que calcule seu peso ideal, utilizando as
# seguintes fórmulas:
# a) Para homens: (72.7*h) - 58
# b) Para mulheres: (62.1*h) – 44.7

sexo = input("Homem? sim ou não?: ")

altura = input("digite sua altura: ")
altura = float(altura)

#Peso ideial para homens: (72.7*h) - 58
#Peso ideial para mulheres: (62.1*h) – 44.7


if sexo == "sim":
	peso_ideal = (72.7*altura) - 58
	print("Seu peso ideal é: " + str(peso_ideal))
else:
	peso_ideal = (62.1*altura) - 44.7
	print("Seu peso ideal é: " + str(peso_ideal))


