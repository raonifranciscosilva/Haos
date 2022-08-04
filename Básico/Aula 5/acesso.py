#criar um programa que peça uma senha e diga pela senha
#qual o nível de acesso da pessoa
#1-admin
#2-Editor
#3-aluno
#4-visitante

numero = int(input('Digite sua senha: '))

if numero == 1:
    print('Administrador')
elif numero == 2:
    print('Editor')
elif numero == 3:
    print('Aluno')
elif numero == 4:
    print('visitante')
else:
    print('Tente novamente')