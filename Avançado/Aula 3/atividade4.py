class Pessoa():
    def __init__(self, nome, rg):
        self.nome = nome
        self.rg = rg

    def mostrar(self):
        print(self.nome)
        print(self.rg)
        
    def detalhes(self):
        print("Meu nome é {}".format(self.nome))
        print("rg: {}".format(self.rg))
    
class Empregado(Pessoa):
    def __init__(self, nome, rg, salario, cargo):
        self.salario = salario
        self.cargo = cargo
        Pessoa.__init__(self, nome, rg)
        #assim se utiliza o INIT da classe PAI
        
    def detalhes(self):
        print("Meu nome é {}".format(self.nome))
        print("rg: {}".format(self.rg))
        print("Salario: {}".format(self.salario))
        print("cargo: {}".format(self.cargo))

douglas = Empregado('Douglas', 1111, 99999999, 'Analista')

douglas.detalhes()