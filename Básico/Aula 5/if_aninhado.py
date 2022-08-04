#aninhado = ninho

# numero1 = 10
# numero2 = 10


# if numero1 >= numero2: #inicio do if

#     if numero1 == numero2:
#         print('Números são iguais')
#     else:
#         print('O primeiro número é maior que o segundo')

# else: #final do if
#     print('O segundo é maior que o primeiro')


camiseta_digitada = input('Digite a cor da camiseta')
boné_sim = input('Esta de boné? Sim ou não?')

if camiseta_digitada == 'azul': #inicio do if

    if boné_sim == 'sim':
        print('Boa noite')
    else:
        print('ocê está de azul, porém não está de boné')

else: #final do if
    print('Você não está de azul')