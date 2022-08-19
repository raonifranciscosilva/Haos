#C:/Users/raoni/OneDrive - UNIP/Python/Haos/Avançado/Aula 6
#atribuir o caminho do arquio para uma variavel
caminho = 'C:/Users/raoni/OneDrive - UNIP/Python/Haos/Avançado/Aula 6/documento3.txt'

arquivo = open(caminho,'r')

#'r' - método de leitura somente
# 'w' - método de escrita, apaga todo o conteúdo do arquivo
# 'a' - método apend, adiciona conteúdo ao final do arquio (não apaga)
# 'x' - método que cria um novo arquivo. Se o arquivo já existe, dará erro

#print(arquivo.read())

print('---------------------------------------')

print(arquivo.readline())

#exiba todas as linhas com readline()
#utilize uma estrutura de repetição
for elemento in arquivo:
    print(elemento)