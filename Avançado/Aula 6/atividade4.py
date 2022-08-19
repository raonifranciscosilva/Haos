# Escrever uma sequência de 1 a 10 num arquivo
# Escrever uma frase ao final do arquivo
# Escrever um PRINT no terminal indicando o sucesso 


#Etapa 1
caminho = 'C:/Users/raoni/OneDrive - UNIP/Python/Haos/Avançado/Aula 6/documento3.txt'

arquivo = open(caminho,'w')

#escreve de 1 a 10
for elemento in range(1,11):
     arquivo.write(str(elemento) + '\n')

#escreve a frase
arquivo.write('Feito por Raoni Francisco Silva')

#SEMPRE FECHAR O ARQUIVO
arquivo.close()

print('Consegui realizar tudo')