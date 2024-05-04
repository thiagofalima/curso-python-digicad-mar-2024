class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresenta(self):
        print(f'oi meu nome é {self.nome} e tenho {self.idade} anos.')


class Brasileiro(Pessoa):
    def __init__(self, nome, idade, estado: str, cidade: str):
        super().__init__(nome, idade)
        self.estado = estado
        self.cidade = cidade

    def apresenta(self):
        super().apresenta()
        print(f'sou de {self.cidade} / {self.nome}.')


thiago = Brasileiro('Thiago', 25, 'SP', 'São Paulo')

print(thiago.nome)
print(thiago.idade)
print(thiago.estado)
print(thiago.cidade)

thiago.apresenta()