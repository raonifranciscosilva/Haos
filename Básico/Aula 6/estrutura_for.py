#estrutura FOR
#estrutura de repetição
#estrutura de iteração

# for x in range(1,11):
#     print(x)


from cgi import print_directory


nomes = ['Raoni', 'Dani', 'Maya', 'Naiara', 'Cauê']
numeros = [1, 4, 2, 5, 6, 4]

#for acumulador in numeros:
    #print(acumulador)
    #print(acumulador)
    #todos os comando serão executados


# for x in 'Treinamentos':
#     print(x)

# for x in nomes:
    
#     if x == 'Naiara':
#         break
#     print(x) #imprimir todo mundo


#fazer um for que mostra o nome da pessoa e uma mensagem de bom dia
for x in nomes:
    for y in numeros:
        print(x, y)


#fazer um terço utilizando o for
for ac_painosso in range(1,6):
    print("Pai nosso que estais no céu")
    for ac_aemaria in range(1,6):
        print('Ave maria')