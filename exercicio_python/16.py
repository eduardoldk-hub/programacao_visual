# # #Devido a falta de responsabilidade com o prazo de entrega, não consegui finalizar a tempo utilizando minhas proprias competencias, para finalizar a tempo utilizei como base o codigo disponibilizado por um colega de turma. Apos finalizar ela toda, com minhas proprias competencias, irei entregar novamente, mesmo que a nota ja esteja atribuida.
# Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M. Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.


def hours_ap(hours):
    if hours > 12 and hours != 24:
        return [(hours-12),'P.M']
    elif hours == 24:
        return [12,'A.M']
    elif hours == 12:
        return [12,'P.M']
    else:
        return [hours,'A.M']
def hours_24h(hours, types):
    if types == 'A':
        if hours == 12:
            return 0
        else:
            return hours
    else:
        if hours == 12:
            return 12
        else:
            return (hours + 12)

while True:
    print('Converção do horario no formato de 24h para o formato A.M P.M (1)')
    print('Converção do horario no formato A.M P.M para o formato 24h (2)')
    print('Sair (0)')
    menu = int(input('>>'))
    if menu == 1:
        hours = int(input('Digite as horas em formato 24h: '))
        minutes = int(input('Digite os minutos: '))
        print('%.2i:%.2i %s'%(hours_ap(hours)[0],minutes,hours_ap(hours)[1]))
    elif menu == 2:
        hours = int(input('Digite as horas em formato A.M/P.M: '))
        minutes = int(input('Digite os minutos: '))
        types = input('Digite o tipo "A" para A.M ou "P" para P.M: ').upper()
        print('%.2i:%.2i'%(hours_24h(hours,types),minutes))
    elif menu == 0:
        break