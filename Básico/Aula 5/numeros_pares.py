# % resto de diisão

#todo número IMPAR dividido por 2 da resto 1 (um)
#todo número PAR dividido por 2, da resto 0 (zero)

#crie programa que peça um número e diga se é par ou ímpar

# 1-pedir a digitação  de um numero
numero_digitado = int(input('Digite um número'))

# 2-crie outra variáel
# 3-nessa variável, atribua o resto da divisão por 2
resto_divisão = numero_digitado%2


# 4- utilizando IF, veja se ela é igual a zero, então mostre
# num PRINT('Par')
if numero_digitado%2 == 0:
    print('Par')
# 5-caso contrário, no ELSE, mostre PRINT('Ímpar') 
else:
    print('Ímpar')

