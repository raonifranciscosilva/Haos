

caminho = 'C:/Users/raoni/OneDrive - UNIP/Python/Haos/Avançado/Aula 6/documento3.txt'

arquivo = open(caminho,'w')

arquivo.write('o modo W apagou tudo e depois escreveu isso aqui')

#SEMPRE FECHAR O ARQUIVO
arquivo.close()

#isso aqui não vai ser executado
arquivo.write('Arquio fechado não recebe dado')
