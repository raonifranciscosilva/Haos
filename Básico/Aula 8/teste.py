#Lista
#Tupla
#set

#Dicionário
    #        key  :  value
carro = {   'marca': 'Ford',
            'modelo': 'Ka',
            'ano': '2016',
            'cor1': 'Branco', #não aceita key duplicada
            'cor2': 'Branco',
            'cor3': ['BRanco', 'Vermelho', 'Cinza'],
            

}

#Desafio 1 - mostrar na tela se a KEY 'categoria' existe

todas_chaves = carro.keys()
todos_values = carro.values()



if 'categoria' in carro.keys:
    print('Categoria está sim no dicionário')
else:
    print('Categoria não está no dicionário')








# #verificar todas as chaves
# print(carro.keys())

# #verificar todos os valores
# print(carro.values())






#carro_arrumado = carro.pop('cor2')



#print(carro_arrumado)

#carro.pop('cor2') #remoe um elemento do dicionário (passar a chave a ser remoida)

#print(carro)





#TYPE()
#print(type(carro['cor2']))





#print(carro['cor3'][1][0])






#descobrir a quantidade de elementos
#print(len(carro))

#print(carro['marca'][0]) #acessa a key marca e traz o elemento 0






# print(carro)

# carro.clear()#limpou o dicionário

# print(carro)


#objeto[index] -----> isso serve para outros arrays
#objeto[key]   -----> isso serve para dicionários








