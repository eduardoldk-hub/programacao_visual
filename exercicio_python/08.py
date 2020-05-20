#Auxiliado pelo Miqueias, colega de sala.
# Faça um programa que mostre os n termos da Série a seguir e imprima no final
# a soma da série:
#S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.

n = int(input("Digite um valor: "))
count = 0
impar = 0
value_list = []

if n < 1:
    print("Valor invalido")

else:
    for i in range(1,(n + 1)):
        impar += 1
        if impar % 2 == 0:
            impar += 1
        if i == n:
            print("{0}/{1} " .format(i,impar), end = '')
        else:
            print("{0}/{1} + " .format(i,impar), end = '')

        sum_value = i / impar
        value_list.append(sum_value)
    print('\n')
    print("Essa e a soma: %.2f" % sum(value_list))







