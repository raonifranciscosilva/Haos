#variáeis
#numero = 2
#outro_numero = pi * 2 + 

# nomes = ('Raoni', 'Dani', 'Maya')
# outros_nomes = ('Raoni', 'Dani', 'Maya')



# print(nomes==outros_nomes) #comparação de igualdade

# print(nomes is outros_nomes)#FALSE


from dataclasses import replace


numero = 1
outro_numero = 1

print(numero == outro_numero)#True
print(numero is outro_numero)#True

print('----------------------------------------------------')

#Constantes
#Valores que não se alteram
#True, False, None
#PI = 3.1415169

nome = ['Raoni', "Dani",'Maya']

print('Raoni' in nome)#case sensitive

print('Cauê' in nome)#verifica a existencia

print('Cauê' not in nome)#not in verifica a não existencia

#is - é o mesmo
#not is - não é o mesmo obj