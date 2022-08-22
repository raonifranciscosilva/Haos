import numpy as np


#matriz = np.arange(1,10).reshape(2,2)
matriz = np.array()
print(matriz)

# #                           Exercício 3
# # Programa que coleta os nomes de pessoas de um arquivo, altera todos para maiúscula e
# # escreve novamente no arquivo os nomes modificados.


# #PAsso1: Criar o caminho para o arquivo
# caminho = 'C:/users/raoni/Documents/teste.txt'
# #Passo2: Abrir a conexao com o arquivo ----> OPEN()
# arquivo_leitura = open(caminho, 'r')

# #Passo3: colocar os nomes do arquivo dentro de um array
# nomes = arquivo_leitura.read()

# #passo 4: mostrar o conteúdo
# print(nomes)

# #passo 5: fechar o arquivo
# arquivo_leitura.close()

# #passo 6: criar novo array com os nomes arrumado
# nomes_arrumados = nomes.title()

# #passo 7: abrir novamente o arquivo e jogar para o arquivo os dados arrumados
# arquivo_escrita = open(caminho, 'w')
# arquivo_escrita.write(nomes_arrumados)

# #passo 8: fechar o arquivo de escrita
# arquivo_escrita.close()