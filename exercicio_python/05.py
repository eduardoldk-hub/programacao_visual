# # Aulixiado pelo Jocenei, colega de tuma.
# 05) Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# • Álcool:
# ◦ até 20 litros, desconto de 3% por litro
# ◦ acima de 20 litros, desconto de 5% por litro
# • Gasolina:
# ◦ até 20 litros, desconto de 4% por litro
# ◦ acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, o tipo de
# combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo
# cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

print("---Bem vindo ao Posto de Combustivel Ldk---")
print("---Gasolina R$2.50 -- Alcool R$1.90---")

fuel_type = str(input("\n Digite G para Gasolina e A para Alcool? "))
liters_fuel = float(input("Quantos litros deseja abastecer? "))


g_cost = 2.50
a_cost = 1.90
discount = 0
final_cost = 0

if fuel_type == 'g':    
    if liters_fuel <= 20:
        discount = (liters_fuel * g_cost) * 3/100
        final_cost = (liters_fuel * g_cost) - discount
        print("Quantidade de litros Gasolna pedida: {}" .format(liters_fuel))
        print("Custo final do abastecimento: R${}" .format(final_cost))
        print("Desconto total: {}" .format(discount))
    
    elif liters_fuel > 20:
        discount = (liters_fuel * g_cost) * 5/100
        final_cost = (liters_fuel * g_cost) - discount
        print("Quantidade de litros Gasolna pedida: {}" .format(liters_fuel))
        print("Custo final do abastecimento: R${}" .format(final_cost))
        print("Desconto total: {}" .format(discount))

if fuel_type == 'a':
    if liters_fuel <= 20:
        discount = (liters_fuel * a_cost) * 4/100
        final_cost = (liters_fuel * a_cost) - discount
        print("Quantidade de litros de Alcool pedida: {}" .format(liters_fuel))
        print("Custo final do abastecimento: R${}" .format(final_cost))
        print("Desconto total: {}" .format(discount))

    elif liters_fuel > 20:
        discount = (liters_fuel * a_cost) * 6/100
        final_cost = (liters_fuel * a_cost) - discount
        print("Quantidade de litros de Alcool pedida: {}" .format(liters_fuel))
        print("Custo final do abastecimento: R${}" .format(final_cost))
        print("Desconto total: {}" .format(discount))