#Devido a falta de responsabilidade com o prazo de entrega, não consegui finalizar a tempo utilizando minhas proprias competencias, para finalizar a tempo utilizei como base o codigo disponibilizado por um colega de turma. Apos finalizar ela toda, com minhas proprias competencias, irei entregar novamente, mesmo que a nota ja esteja atribuida.
# 20-Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida.

def month_ext(month):
    months = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
    try:
        return months[month-1]
    except:
        print("Digite um mês válido")
day = int(input('Digite o Dia: '))
month = 13
while month > 12:
    month = int(input('Digite o Mes: '))
    month_ext(month)
year = int(input('Digite o Ano: '))
print('%.2i de %s de %i'% (day,month_ext(month),year))