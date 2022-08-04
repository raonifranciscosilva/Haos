#Criar uma lista/tupla com 5 nomes
#criar um FOR e mostrar nome a nome

nomes = ['Raoni','Dani','Maya','Naiara','Cauê']

#colocar uma condição dentro do for (if dentro)
#que avalia se um determinado valor foi achado
#se for achado esse valor, utilize o CONTINUE
#para pular a etapa, mas continuar a mostrar 
#os elementos no PRINT()

for elemento in nomes:
    
    if elemento == 'Naiara':
        continue
    print(elemento)

    
    

print('Terminei')
