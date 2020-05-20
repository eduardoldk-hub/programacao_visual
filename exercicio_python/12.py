# #Devido a falta de responsabilidade com o prazo de entrega, não consegui finalizar a tempo utilizando minhas proprias competencias, para finalizar a tempo utilizei como base o codigo disponibilizado por um colega de turma. Apos finalizar ela toda, com minhas proprias competencias, irei entregar novamente, mesmo que a nota ja esteja atribuida.
# 12- A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos. Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, e identificar os usuários com maior espaço ocupado. Através de um programa, baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado "usuarios.txt":
# alexandre 456123789
# anderson 1245698456
# antonio 123456456
# carlos 91257581
# cesar 987458
# rosemary 789456125
# Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar um programa que gere um relatório, chamado "relatório.txt", no seguinte formato:

# ACME Inc. Uso do espaço em disco pelos usuários
# ------------------------------------------------------------------------
# Nr. Usuário Espaço utilizado % do uso
# 1 alexandre 434,99 MB 16,85%
# 2 anderson 1187,99 MB 46,02%
# 3 antonio 117,73 MB 4,56%
# 4 carlos 87,03 MB 3,37%
# 5 cesar 0,94 MB 0,04%
# 6 rosemary 752,88 MB 29,16%
# Espaço total ocupado: 2581,57 MB
# Espaço médio ocupado: 430,26 MB
# Obs.: Não é necessário ler os dados de um arquivo, os dados pode ser inseridos por input() e o relatório final pode ser exibido com print().


users = []
space = []
count = 0
menu = 1
while menu != 0:
    while True:
        users.insert(count, input('Nome do usuário (máximo de: 15 characters): '))
        if len(users[count]) > 15:
            print('Digite um nome com no máximo 15 characters')
        else:
            size = len(users[count])
            users[count] = users[count] + ' '*( 15 - size )
            break
    space.append(float(input('Espaço usado em MB: ')))
    count += 1
    menu = int(input('Deseja cadastrar outro usuário (1)\nTerminou de Cadastrar (0)\n\t\t>>'))

total_space = sum(space)
print('\nNr.\tusuario\t\tEspaço utlizado\t\t\t% do uso')
for i in range(len(users)):
    percent_use = round(space[i] * 100 / total_space, 2)
    print(f'\n{ i + 1 }\t{users[i]}\t\t{space[i]}MB\t\t\t{percent_use}%')
print(f'Espaço total ocupado: {total_space}\nEspaço médio ocupado: {total_space/len(space)}')