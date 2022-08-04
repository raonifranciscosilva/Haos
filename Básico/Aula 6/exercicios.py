
#1-Fazer um programa que peça duas notas, mostre a média
#e diga se o aluno está aprovado por média

#Passo 1: Criar as variáveis e pedir a digitação das notas
nota1 = float(input('Digite a primeira nota \n'))
nota2 = float(input('Digite a segunda nota \n'))

#PAsso 2: Criar a variável MÈDIA que irá conter a média das notas
media = (nota1+nota2)/2

print(type(media))
print('A média foi {}'.format(media))

#Passo 3: criar o if, interpretando se a média for maior ou igual a 6
if media >= 6:

#Passo 4: exibir no PRINT se o aluno está aprovado
    print('Aluno aproado por média')

#Passo 5: else para dizer reprovado
else:
    print('Aluno reproado por média')
    

#2-Fazer um programa que peça as aulas dadas de um curso
#e a quantidade de faltas. O programa deve exibir se o aluno
#passou por frequencia


#3-Fazer um programa que peça duas notas, peça as aulas dadas
#peça as faltas e diga se o aluno está aprovado por MÈDIA e 
#por FREQUENCIA (os dois verdadeiros)

