#peça a digitação de vários números e mostre a média

#iteração = realizar a mesma coisa várias vezes

#coleta a quantidade de dados digitados
quantidade = int(input('Digite a quantidade de números a serem coletados: '))

somatoria = 0

#for
for i in range(quantidade):
    x = int(input('Digite um numero: '))
    somatoria = somatoria + x #variavel que guarda o valor dela prorpia mais o valor digitado
    #somatoria += x

import numpy as np

np.average(somatoria)

#media = soma de todos os elementos, dividido pela quantidade de elementos
media = somatoria / quantidade

print(f'A media é: {media}')