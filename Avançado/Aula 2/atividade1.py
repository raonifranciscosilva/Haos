#Criar a classe Cachorro


class Cachorro:
    #atributos podem ser dentro da classe
    #ou ainda dentro do INIT
    especie = 'Canis Familiaris'
    def __init__(self, nome, raca):
        self.umNome = nome
        self.umaRaca = raca
        #umNome é variavel do método
        #nome é variável de inicialização do método (passagem de parametro)
    
    def som(self, latido):
        #retorne o latido
        #fazer a atribuição
        return latido

#Herança
#Classes filhas herdam as características da classe PAI
#Classes filhas podem receber outros atributos

class Labrador(Cachorro):
    pass

class Pinscher(Cachorro):
    pass
                                                #cachorro1.nome = 'Bolt'
                                                #cachorro2.nome = 'Yola'
class Rottweiller(Cachorro):                    #print(cachorro1 == cachorro2)
    pass


#criando o objeto

labrador = Labrador('Marley', 'Labrador')

print(f'O nome do cão é {labrador.umNome} e a raça é {labrador.umaRaca}')




# #Criar objeto e passar os atributos
# tapioca = Cachorro('Tapioca', 'Vira Lata')
# yola = Cachorro('Yola', 'Labrador')

# print(f'O nome é {tapioca.umNome} e a raça é {tapioca.umaRaca}')
# print(f'O nome é {yola.umNome} e a raça é {yola.umaRaca}')

# print(tapioca.especie) #acessando a variavel de classe


# print('Até aqui tudo bem')

