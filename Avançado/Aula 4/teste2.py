from lib2to3.pgen2.token import SLASHEQUAL


class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite


    def depositar(self, valor):
        #devemos aqui aumentar o valor do atributo SALDO
        #implementando a operação
        self.saldo = self.saldo + valor


    def sacar(self, valor):
        #devemos aqui reduzir o valor do atributo SALDO
        #implementando a lógica do saque
        self.saldo = self.saldo - valor
        #self.saldo -= valor


    def extrato(self):
        #devemos aqui exibir o valor do atributo saldo
        print(f'O numero da conta é {self.numero}, e o saldo é {self.saldo}')

                                #conta
    def transferir(self, destino, valor):
        self.saldo -= valor
        destino.saldo += valor
        # retirou	= self.sacar(valor)
        # if	(retirou	==	False):
        #     return False
        # else:
        #     destino.depositar(valor)
        #     return True



class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf


raoni = Cliente('Raoni', 'Silva', 12345678900)
dani = Cliente('Dani', 'Amorim', 12345678201)


conta1 = Conta(111, raoni, 1000, 1000)
conta2 = Conta(222, dani, 1000, 1000)

conta1.transferir(conta2, 1)

print(conta2.saldo)

# #utilizando o objeto da CONTA(), podemos passar como atributo o objeto CLIENTE()
# minha_conta = Conta('1234-5', dani, 100, 1000)





# print(f'O nome do titular é {minha_conta.titular.nome}')       
# print(f'O sobrenome do titular é {minha_conta.titular.sobrenome}')

# print(f'O saldo é {minha_conta.extrato()}')       






# conta1 = Conta('1234-5', 'Raoni', 50, 100)

# conta1.extrato()

# conta1.depositar(150)

# conta1.extrato()

# conta1.sacar(30)

# conta1.extrato()



