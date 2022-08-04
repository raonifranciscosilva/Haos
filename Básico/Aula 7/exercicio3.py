#3-Fazer um programa que peça duas notas, peça as aulas dadas
#peça as faltas e diga se o aluno está aprovado por MÈDIA e 
#por FREQUENCIA (os dois verdadeiros)

#passo 1: pedir as notas de prova
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

#Passo 2: Pedir a carga horária
carga_horaria = int(input('Digite a carga horária: '))


#passo 3: Pedir as faltas
quantidade_faltas = int(input('Digite a quantidade de faltas: '))


#Passo 4: fazer o calculo da média
media = (nota1+nota2)/2

#PAsso 5: Fazer o calculo da frequencia
faltas_maximas = carga_horaria * 0.75


#Passo 6: 
condição1 = media >= 6
condição2 = quantidade_faltas < faltas_maximas


if condição1 and quantidade_faltas < faltas_maximas: 
    print('Aprovado')
else:
    print('Reprovado')