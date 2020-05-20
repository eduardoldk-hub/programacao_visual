# #Devido a falta de responsabilidade com o prazo de entrega, não consegui finalizar a tempo utilizando minhas proprias competencias, para finalizar a tempo utilizei como base o codigo disponibilizado por um colega de turma. Apos finalizar ela toda, com minhas proprias competencias, irei entregar novamente, mesmo que a nota ja esteja atribuida.
# 14-  Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.

def value(argument):
    if(argument > 0):
        return "P"
    elif(argument < 1):
        return "N"

num = int(input('Digite um numero inteiro para verificação de negativo ou positivo: '))
print('(P) Positivo (N) Negativo\nResultado:',value(num))
