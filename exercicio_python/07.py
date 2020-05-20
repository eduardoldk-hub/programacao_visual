#Auxiliado por Miqueias, colega de turma.
#  Desenvolver um programa para verificar a nota do aluno em uma prova com 10
# questões, o programa deve perguntar ao aluno a resposta de cada questão e ao
# final comparar com o gabarito da prova (o gabarito pode ser definido dentro do
# código) e assim calcular o total de acertos e a nota (atribuir 1 ponto por
# resposta certa). Após cada aluno utilizar o sistema deve ser feita
# uma pergunta se outro aluno vai utilizar o sistema. Após todos os alunos terem
# respondido informar:
# a) Maior e Menor Acerto;
# b) Total de Alunos que utilizaram o sistema;
# c) A Média das Notas da Turma.




#gabarito
correct_answers = ['a', 'b', 'c', 'd', 'e', 'e', 'd', 'c', 'b', 'a'] 

#todas as notas de todos os alunos
student_points = []


question = 1

while True:
    points = 0
    for i in range(1, 11):
        answers = input(str("Questão {0}: " .format(i)))
        if correct_answers[(i-1)] == answers.lower():
            points += 1
    student_points.append(points)
    another_student = input("Outro aluno irá utilizar? ")
    if another_student == '0':
        break

print("Maior Acerto:" + str(max(student_points)))
print("Menor Acerto: " + str(min(student_points)))
print("Total de alunos que utilizaram o sistema: " + str(len(student_points)))
print("Média das notas da Turma: " + str(sum(student_points) / len(student_points)))


    