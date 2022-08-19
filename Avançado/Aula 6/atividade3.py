# Criar a conexao para um arquivo
caminho = 'C:/Users/raoni/OneDrive - UNIP/Python/Haos/Avançado/Aula 6/documento3.txt'

arquivo_escrita = open(caminho,'w')

# Escrever um nome no arquivo
arquivo_escrita.write('Raoni')

#SEMPRE FECHAR O ARQUIVO
arquivo_escrita.close()

arquivo_leitura = open(caminho, 'r')

# apresentar num print o conteúdo
print(arquivo_leitura.read())