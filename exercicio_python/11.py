#Devido a falta de responsabilidade com o prazo de entrega, não consegui finalizar a tempo utilizando minhas proprias competencias, para finalizar a tempo utilizei como base o codigo disponibilizado por um colega de turma. Apos finalizar ela toda, com minhas proprias competencias, irei entregar novamente, mesmo que a nota ja esteja atribuida.
# 11- Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. Escreva um programa (usando uma lista de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:
# $200 - $299
# $300 - $399
# $400 - $499
# $500 - $599
# $600 - $699
# $700 - $799
# $800 - $899
# $900 - $999
# $1000 em diante



inter = [200.0, 299.0, 300.0, 399.0, 400.0, 499.0, 500.0, 599.0, 600.0, 699.0, 700.0, 799.0, 800.0, 899.0, 900.0, 999.0, 1000.0, 'ou mais']

sales_list = []
gross_value = 0
menu = 1;
count = 0
count2 = 0
while menu != '0':
    gross_value = float(input('Insira o valor total de suas vendas brutas na semana: '));
    salary = float(200 + gross_value * 9/100);
    print(salary)
    sales_list.append(salary)
    menu = input('Cadastrar outro vendedor (1)\nVerificar a quantidade de vendedores que receberam salários em determindados intervalos (0)\n\t\t>>');
sales_list.sort()
menu = 1;
print('\t\tIntervalos!')
for i in range(1, len(inter) + 1):
    if i % 2 == 0:
        count2 += 1
        print(inter[count], f'({count2})')
    else:
        print(inter[count], '', end="")
    count += 1
while menu != '0':
    count = 0
    count_sales = 0
    verify = int(input('\nDigite o intervalo: '))
    for i in sales_list:
        if verify != 9:
            if i >= inter[(verify - 1) * 2] and i <= inter[(verify - 1) * 2 + 1]:
                count_sales += 1;
        elif i >= inter[(verify - 1) *2 ]:
            count_sales += 1;
    print(f'{count_sales} vendedores recebem esse salário!')
    menu = input('Verificar outro intervalo (1)\nSair (0)\n\t\t>>');


    