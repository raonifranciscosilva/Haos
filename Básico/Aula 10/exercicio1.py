# 1-Crie um programa que mostre o seu nome
from ast import If
from traceback import print_tb


print('Raoni')
# 2-Crie um programa que mostre o seu nome e sobrenome
print('Raoni', 'Silva')

# 3-Crie um programa que peça a digitação do nome e mostre
#     num print o resultado
nome = input('Digite seu nome')
print(nome)
# 4-Fazer um programa que peça dois números, verifique
#     qual dos dois é maior e mostre
num1 = input('Digite um numero')
num2 = input('Digite um numero')
if num1 > num2:
    print('O primeiro é maior que o segundo')
else:
    print('O segundo é maior que o primeiro')

# 5-Fazer um programa que conta de 1 a 10 utilizando FOR
#for VARIAVEL DE CONTROLE in OBJETO A SER LIDO:

#----->Variavel de controle: dita o início da contagem e incremento
#----->Objeto a ser lido: lista, tupla, etc que irá ser feita a ITERAÇÃO
for elemento in range(1,10):
    print(elemento)

# 6-Fazer um programa que conta de 1 a 10 utilizando WHILE
#Criar a variavel de control
posicao = 0
#while VARIAVEL_CONTROLE < 10
#       print(VARIAVEL_CONTROLE)
#       posicao = posicao + 1
while posicao < 10:
    print(posicao)
    posicao = posicao + 1

# 7-Fazer um programa que peça 5 números, verifique qual 
#     dos cinco é maior e mostre
num1 = input('Digite um número: ')
num2 = input('Digite um número: ')
num3 = input('Digite um número: ')
num4 = input('Digite um número: ')
num5 = input('Digite um número: ')



# 8-Fazer um programa com uma FUNÇÃO que receba um NOME e 
#     um SOBRENOME, a função deve retornar uma frase com os dois

