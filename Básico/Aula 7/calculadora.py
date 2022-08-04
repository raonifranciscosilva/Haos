#construir quatro funções
#1-soma
#2-subtrair
#3-diidir
#4-multiplicar

#pedir a digitação de dois números
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

def adicao():
    print('Eu vou somar coisas')
    print(num1+num2)

def subtracao():
    print('Eu vou subtrair coisas')
    print(num1-num2)

def divisao():
    print('Eu vou dividir coisas')
    print(num1/num2)

def multiplicacao():
    print('Eu vou multiplicar coisas')
    print(num1*num2)

#Exibir num PRINT todas as possibilidades
#1-soma
#2-subtrair
#3-diidir
#4-multiplicar

print('Escolha uma opção abaixo: ')
print('1 - Soma')
print('2 - Subtração')
print('3 - Divisão')
print('4 - Multiplicação')

#coletar a opção
escolha = int(input())

#utilizar um IF para saber a opção
if escolha == 1:
    adicao()
elif escolha == 2:
    subtracao()
elif escolha == 3:
    divisao()
elif escolha == 4:
    multiplicacao()
else:
    print('você não digitou uma opção válida')





