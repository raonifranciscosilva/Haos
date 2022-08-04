from importlib import import_module


class Pessoa:
    def __init__(self, nome, sobrenome):
        self.umNome = nome
        self.umSobrenome = sobrenome


    def mostra_nome(self):
        print(self.umNome, self.umSobrenome)


#criar o objeto (instância da classe)
nome = input('Digite um nome: ')
sobrenome = input('Digite um nome: ')

pessoa1 = Pessoa(nome, sobrenome)
pessoa2 = Pessoa('Potira', 'Silva')

pessoa1.mostra_nome()
pessoa2.mostra_nome()
#objetos vão permitir o acesso a procedimentos


