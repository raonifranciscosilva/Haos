#override = alterar o funcionamento de métodos

class Passaro:
    def intro(self):
        print('Eu sou uma ave')
    
    def voo(self):
        print('A maioria das aves voa')


class Papagaio(Passaro):
    def voo(self):
        print('Eu sou um papagaio e eu sei voar')


class Pinguim(Passaro):
    def voo(self):
        print('Eu sou um pinguim e não sei voar')


passaro = Passaro()
papagaio = Papagaio()
pinguim = Pinguim()

pinguim.intro()
pinguim.voo()

papagaio.intro()
papagaio.voo()
