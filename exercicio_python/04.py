# # Consegui fazer sozinho :)
# 04) Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um
# triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
# Dicas:
# • Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# • Triângulo Equilátero: três lados iguais;
# • Triângulo Isósceles: quaisquer dois lados iguais;
# • Triângulo Escaleno: três lados diferentes;

valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
valor3 = int(input("Digite o terceiro valor: "))

valores = valor1 + valor2

if valor3 > valores:
    print("Voce tem um triangulo")
elif valor1 == valor2 and valor2 == valor3:
    print("Voce tem um triangulo equilatero")
elif valor1 == valor2 or valor2 == valor3 or valor1 == valor3:
    print("Voce tem um triangulo isoceles")
elif valor1 != valor2 != valor3:
    print("Voce tem um triangulo escaleno")
else:
    print("Esses valores nao podem ser um triangulo")
