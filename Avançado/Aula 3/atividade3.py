#criar duas classes
#Classe VEICULO
#classe ONIBUS


class Veiculo:
    def __init__(self, nome, velocidade_maxima, tipo_combustivel):
        self.nome = nome
        self.velocidade_maxima = velocidade_maxima
        self.tipo_combustivel = tipo_combustivel

    def passageiros(self, capacidade):
        print(f'A capacidade do  é de {capacidade} pessoas')

class Onibus(Veiculo):
    def __init__(self,capacidade_passageiros=0):
        self.capacidade = capacidade_passageiros
        return super().passageiros(self.capacidade)

#Na utilização da classe veiculo, pode-se colocar o argumento como opcional
busao = Onibus(50)



