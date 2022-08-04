#while é estrutura de repetição/iteração

from itertools import count
from posixpath import normcase


# x = 1 #criar e inicializar variável

# while x < 10:  #começando em 1 e indo até o 9
#     print(x)   #mostra na tela o valor da variáel
#     x = x + 1  #isso adiciona +1 a cada iteração (a cada rodada)
    

nomes = ['Raoni', 'Dani', 'Maya', 'Naiara', 'Cauê']

#criar uma variável de controle
contador = 0

#descobrir a quantidade de elementos da tupla
#função LEN()
final = len(nomes)

#definir a lógica do while
#o contador tem de começar nno zero e ir até onde?
while contador < final:
    print(nomes[contador])
    
    # definir o incremente do contador
    contador = contador + 1

