#2-Fazer um programa que peça as aulas dadas de um curso
#e a quantidade de faltas. O programa deve exibir se o aluno
#passou por frequencia

#Passo 1
quantidade_faltas = int(input('Digite a quantidade de faltas: '))

#Passo 2: pedir a carga horária
carga_horaria = int(input('Digite a carga horária do curso'))

#passo 3: Calcular a frequencia maximo (carga_horaria * 0.25)
faltas_maximas = carga_horaria * 0.25 

#passo 4: avaliar se a fasltas do aluno são maiores que faltas maximas
if quantidade_faltas > faltas_maximas:
    print('Reprovado')
else:
    print('Aprovado')
