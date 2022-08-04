#FOR  precisa de variavel de controle, porém não se inicializa

nomes = ['Raoni', 'Dani', 'Maya', 'Naiara', 'Cauê']

#FOR controle in OBJETO:

for x in nomes:

    print(x)


for y in nomes:

    #quando chegar em Naiara, pare ----> BREAK
    if y == 'Naiara':
        break

    print(y)