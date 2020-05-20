# #Devido a falta de responsabilidade com o prazo de entrega, não consegui finalizar a tempo utilizando minhas proprias competencias, para finalizar a tempo utilizei como base o codigo disponibilizado por um colega de turma. Apos finalizar ela toda, com minhas proprias competencias, irei entregar novamente, mesmo que a nota ja esteja atribuida.
#13- Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

def func_soma(a, b, c):
    try:
        return float(a)+float(b)+float(c)
    except:
        return a+b+c
print('Some 3 argumentos (string ou float)')
x = []
for i in range(3):
    x.append(input(f'Digite o argumento { i + 1}: '))
print('Resultado:', func_soma(x[0],x[1],x[2]))