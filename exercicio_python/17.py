# # #Devido a falta de responsabilidade com o prazo de entrega, não consegui finalizar a tempo utilizando minhas proprias competencias, para finalizar a tempo utilizei como base o codigo disponibilizado por um colega de turma. Apos finalizar ela toda, com minhas proprias competencias, irei entregar novamente, mesmo que a nota ja esteja atribuida.
# 17 -Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta. O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a função valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. O programa deverá então exibir o valor a ser pago na tela. Após a execução o programa deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero para a prestação. Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso, cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.




def value_payment(value,days):
    if days == 0:
        return valor
    elif days > 0:
        return value + value * 3 / 100 + value * 0.1 / 100 * 10
    else:
        return value
parcels = []
out = 1
while out != 0:
    value = float(input('Digite o valor da parcela: '))
    delay = int(input('Digite os dias de atraso: '))
    parcels.append(value_payment(value, delay))
    out = int(input('Adicionar outra parcela (1)\nEncerrar (0)\n>>'))

print(f'Quantidade de parcelas: {len(parcels)}\nTotal do valor: {sum(parcels)}')
