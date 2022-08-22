
#                          Exercício 2
#Criar um Código que escreve num arquivo, porém com as tratativas de exceção criadas para a abertura 
# do arquivo e a tratativa para escrita no arquivo
# •	Uma tratativa para abrir o arquivo
# •	Uma tratativa para escrever no arquivo
# •	Não esquecer de fechar o arquivo


#clausula try
try:
    arquivo = open('arquivo.txt')
    try:
        arquivo.write('Raoni')
    except:
        print('Não é possível abrir o arquivo')
    finally:
        arquivo.close()
except:
    print('Não é possível abrir o arquivo')

