#criando uma classe
from mimetypes import init


class NomeClasse:
    atributo1 = 'Preto'
    atributo2 = 18
#########################################


#keyword SELF = é um parametro que todos os métodos de uma 
#classe tem de ter. o self é passado pra frente pelo prórpio 
# Python. self sempre tem de ser o primeiro parametro de função

def procedimento1(self, parametro1, parametro2):
    self.atributo1 = parametro1
    self.atributo2 = parametro2

# Construtor da classe
#é o método que invocado sempre que uma instância da classe
# é criada   __init__
# recebe orbrigatoriamente o SELF

def __init__(self, parametro1, parametro2):
    #self.atributo da classe = parametros
    self.atributo1 = parametro1
    self.atributo2 = parametro2
    #self.atributo1 = valor

