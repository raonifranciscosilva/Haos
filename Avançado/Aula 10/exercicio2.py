# Programa que calcula a área de um triangulo
# •	Importar biblioteca MATH
# •	Fórmulas: 
# lados = (a+b+c)/2
# area = raiz quadrada(lados*(lados-a)*(lados-b)*(lados-c))

# Grave num arquivo os valores dos lados do triangulo e o resultado

import math as mt

lado1 = int(input("Digite o comprimento do lado: "))
lado2 = lado1
lado3 = lado1

perimetro = (lado1 + lado2 + lado3) / 2

area = mt.sqrt(perimetro*(perimetro-lado1)*(perimetro-lado2)*(perimetro-lado3))

#print('A area do triagulo é: ' + area)
print(f'A area do triagulo é {area}')


