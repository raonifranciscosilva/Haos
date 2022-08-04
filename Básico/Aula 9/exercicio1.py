#criar uma função personalizada
def minha_funcao(fator1, fator2):
    return fator1 * fator2


def outra_funcao(multiplicador):
    return lambda fator : fator * multiplicador


quintuplo = outra_funcao(5)
dobro = outra_funcao(2)
triplo = outra_funcao(3)

print(quintuplo(3))
print(triplo(3))
print(dobro(3))