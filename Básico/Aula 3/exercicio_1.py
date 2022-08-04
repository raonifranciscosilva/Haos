

# 1 - crie um programa que peça dois 
# números e mostre a soma e a média

#1 - Criar as variáveis e Atribuir valores
numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))

soma = numero1+numero2
media = (numero1+numero2)/2
resto = numero1%numero2

#2 - mostrar na tela a soma
print('A soma dos números é: {}, e a média é: {}'.format(soma, media))
print('A soma dos números é: ' + soma + 'e a média é: ' + media)

#3 - mostrar na tela a média
print(media)


# 2 - Crie um programa que mostre o resto da divisão de dois números
print(resto)

# 3 - Crie um programa que converte uma temperatura em celsius para farenheit
#A saber: temp_fahrenheit = temp_celsius * 1.8 + 32

#INPUT() -----> recebe como string
#CAST ----> float(input('Digite um valor'))

# 4 - Crie um programa que leia o RAIO e mostre a circunferência e a área
# de um círculo
#A saber: comprimento_circunferencia = 2 * pi * raio
#A saber: area_circunferencia = pi * raio**2
            
#from cmath import pi
#print(pi)


