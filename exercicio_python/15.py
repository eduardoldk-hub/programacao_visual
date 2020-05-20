# # Consegui fazer sozinho :)
# # Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.




def somar_TaxaImposto(taxaImposto, valor):
    return valor + valor * taxaImposto / 100

value1 = int(input('Digite a taxa: '))
value2 = float(input('Digite o valor: '))

print(somar_TaxaImposto(value1, value2))