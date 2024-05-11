# Criando a super classe

class Animal:

    def __init__(self, nome: str, raca: str):
        self.nome = nome
        self.raca = raca

    def apresenta(self):
        print(f'Oi eu sou um {self.raca} e me chamo {self.nome}')


class TubaraoMartelo(Animal):

    def __init__(self, nome, raca, cor: str, idade: int):
        super(). __init__(nome, raca)
        self.cor = cor
        self.idade = idade

    def apresenta(self):
        super().apresenta()
        print(f'Sou {self.cor} e tenho {self.idade} anos de idade.')


tutu = TubaraoMartelo('Thiago', 'Tubarao', 'Azul', 25)

print(tutu.nome)
print(tutu.raca)
print(tutu.cor)
print(tutu.idade)

tutu.apresenta()