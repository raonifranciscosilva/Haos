#arquio PY

#método OPEN() é reponsáel por acessar o arquivo
#pede dois argumentos - caminho do arquivo e tipo de acesso

#caminho: como chegar no arquio (endereço completo)
caminho_arquivo = 'C:/Users/raoni/OneDrive - UNIP/Python/Haos/Avançado/Aula 5/Aula 5.docx'

arquivo = open(caminho_arquivo, 'r', encoding='UTF-8')

#r = read (acesso somente leitura)
#w - Write (acesso de escrita, porém limpa todo o arquivo)
#a - append (acesso de leitura e escrita, porém adiciona ao final um novo conteúdo)
#x - create (cria um novo arquivo, se o arquio existe, dará erro)
#adicionais
#t - text (valor padrão)
#b - binary (modo binário) 01010100100111011100110001

#ENCODING - codificação
#UTF-8




print(arquivo.read())



arquivo.close()#sempre fechar o arquivo



#readline le linha a linha do arquivo
# print(arquivo.readline())
# print('------------------')
# print(arquivo.readline())
# print('------------------')
# print(arquivo.readline())
# print('------------------')
# print(arquivo.readline())
# print(arquivo.readline())
# print(arquivo.readline())





