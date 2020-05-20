# #Auxiliado pelo Miqueias, colega de turma.
# 03) Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que
# depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto,
# mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O
# programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# Desconto do IR:
# • Salário Bruto até 900 (inclusive) - isento
# • Salário Bruto até 1500 (inclusive) - desconto de 5%
# • Salário Bruto até 2500 (inclusive) - desconto de 10%
# • Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o
# exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.

valor_hora_trab = int(input("Informe qual o valor das sua hora de trabalho: "))
quant_hora_trab = int(input("Informe a quantia de horas trabalhadas no mes: "))


sal_bruto = (valor_hora_trab * quant_hora_trab)

fgts = sal_bruto*11/100
inss = sal_bruto*10/100

if sal_bruto <= 900:
    descontos = inss + 0
    sal_liquido = sal_bruto - descontos

    print("Salario Bruto: R${}" .format(sal_bruto))
    print("IR: Isento")
    print("(-) INSS: R${}" .format(inss))
    print("(-) FGTS: R${}" .format(fgts))
    print("Total de Descontos: R${}" .format(descontos))
    print("Salario Liquido: R${}" .format(sal_liquido))
elif sal_bruto > 900 <= 1500:
    descontos = inss + (sal_bruto * 5/100)
    sal_liquido = sal_bruto - descontos

    print("Salario Bruto: R${}" .format(sal_bruto))
    print("(-) IR (5%): R${}" .format(sal_bruto * 5/100))
    print("(-) INSS (%10): R${}" .format(inss))
    print("FGTS (%11): R${}" .format(fgts))
    print("Total de Descontos: R${}" .format(descontos))
    print("Salario Liquido: R${}" .format(sal_liquido))
elif sal_bruto > 1500 <= 2500:
    descontos = inss + (sal_bruto * 10/100)
    sal_liquido = sal_bruto - descontos

    print("Salario Bruto: R${}" .format(sal_bruto))
    print("(-) IR (10%): R${}" .format(sal_bruto * 10/100))
    print("(-) INSS (%10): R${}" .format(inss))
    print("FGTS (%11): R${}" .format(fgts))
    print("Total de Descontos: R${}" .format(descontos))
    print("Salario Liquido: R${}" .format(sal_liquido))
elif sal_bruto > 2500:
    descontos = inss + (sal_bruto * 20/100)
    sal_liquido = sal_bruto - descontos
    
    print("Salario Bruto: R${}" .format(sal_bruto))
    impost_renda = sal_bruto * 20/100
    print("(-) IR (20%): R${}" .format(sal_bruto * 15/100))
    print("(-) INSS (%10): R${}" .format(inss))
    print("FGTS (%11): R${}" .format(fgts))
    print("Total de Descontos: R${}" .format(descontos))
    print("Salario Liquido: R${}" .format(sal_liquido))