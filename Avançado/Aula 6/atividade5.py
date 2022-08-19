# Pedir pro usuário digitar uma frase e escrever num arquivo
caminho = 'C:/Users/raoni/OneDrive - UNIP/Python/Haos/Avançado/Aula 6/documento3.txt'
arquivo = open(caminho,'a')

for i in range(5):
    
    
    arquivo.writelines(input('Digite seu nome: \n'))
    

