#                           Exercício 1
# 1 - Programa que pede a digitação de 5 nomes e escrever num arquivo
# •	Método 1: Fazer repetindo a instrução de escrita
# •	Método 2: Fazer com apenas uma instrução de escrita

#PAsso1: Criar o caminho para o arquivo
caminho = 'C:/users/raoni/Documents/teste.txt'
#Passo2: Abrir a conexao com o arquivo ----> OPEN()
arquivo = open(caminho, 'a')
#Passo3: utilizar o método WRITE() por 5 vezes
#modo 1:
arquivo.write('Raoni\n')
arquivo.write('Raoni\n')
arquivo.write('Raoni\n')
arquivo.write('Raoni\n')
arquivo.write('Raoni')

#modo 2:
for i in range(5):
    arquivo.write('Raoni\n')

#PAsso4: Fechar a conexão ----> CLOSE()
arquivo.close()


#                          Exercício 2
#Criar um Código que escreve num arquivo, porém com as tratativas de exceção criadas para a abertura 
# do arquivo e a tratativa para escrita no arquivo
# •	Uma tratativa para abrir o arquivo
# •	Uma tratativa para escrever no arquivo
# •	Não esquecer de fechar o arquivo



#                           Exercício 3
# Programa que coleta os nomes de pessoas de um arquivo, altera todos para maiúscula e
# escreve novamente no arquivo os nomes modificados.



