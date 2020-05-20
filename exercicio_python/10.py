# # Consegui fazer sozinho :)
# 10) Faça um programa que leia um número indeterminado de valores, corresponden-
# tes a notas, encerrando a entrada de dados
# quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
# a) Mostre a quantidade de valores que foram lidos;
# b) Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
# c) Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
# d) Calcule e mostre a soma dos valores;
# e) Calcule e mostre a média dos valores;
# f) Calcule e mostre a quantidade de valores acima da média calculada;
# g) Calcule e mostre a quantidade de valores abaixo de sete;
# h) Encerre o programa com uma mensagem;

product = 1
values_list = []
count = 0

while True:
    values = float(input("Valor {0}: " .format(product)))
    if values == -1:
        break
    values_list.append(values)

    product += 1
        


print("Quantidade de valores lidos:", len(values_list))
print("Valoes em ordem que foram inseridos: ", values_list)
values_list.reverse()
print("Valores em ordem inversa: ", values_list)
print("Soma dos valores: ", sum(values_list))
media =  sum(values_list) / len(values_list)
print("Média dos valores inseridos: ", media)

for i in values_list:
    if i > media:
        count += 1
print("Numero de Valores acima da média: ", count)

for i in values_list:
    if i < 7:
        count += 1
print("Numero de Valores abaixo de 7: ", count)

print("\n Programa encerrado!\n \n ")


