
from itertools import count
from tkinter import N
from typing import Type


numeros = [2, 1, 4.2, 7, 9.7, 5, 4.1]

def funcao_soma():
    return sum(numeros)


def valor_menor():
    return min(numeros)

def valor_maior():
    return max(numeros)

def arrumar():
    return sorted(numeros,reverse=True)#REVERSE inverte o raciocinio

def arredondar():
    return round(sum(numeros),1)

def absoluto():
    return abs(-5)#retorna o valor absolute de um número


#fazer uma função personalizada que calcule a 
# média dos elementos de uma lista
#COMO SABER QUANTOS ELEMENTOS TEM NA LISTA?
def funcao_media():
    return sum(numeros) / len(numeros)

def funcao_media2(lista):
    return sum(lista) / len(lista)


print(funcao_media)
print(funcao_media2(numeros))
#print(absoluto())
# print(arrumar())
# print(funcao_soma())
# print(valor_menor())
# print(valor_maior())



dados = ['Raoni', 1, 4, 'Dani', 'Maya', 5, '2']

quantidade = 0
for elemento in dados:
    if type(elemento) == str:
        quantidade += 1

print('A quantidade de textos é: ', quantidade)