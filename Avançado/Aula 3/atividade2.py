from http import client


class Pessoa():
    def __init__(self, nome, rg):
        self.nome = nome
        self.rg = rg
    
    def mostrar(self):
        print(f'O nome da pessoa é {self.nome}')
        print(f'O RG da pessoa é {self.rg}')

    def detalhes(self):
        print(f'O nome da pessoa é {self.nome}')
        print(f'O RG da pessoa é {self.rg}')

class Cliente(Pessoa):
   
    def __init__(self, nome, rg, bandeira_cartao):
        #SUPER é o método que permite acesso ao métodos da superclasse
        super().__init__(nome, rg)




obj_cliente = Cliente('Raoni', 123, 'Visa')
obj_pessoa = Pessoa('Raoni', 123)

print(obj_cliente.detalhes())
print(obj_cliente.mostrar())
   