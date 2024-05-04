
class Carro:

    def __init__(self, marca: str, modelo: str, ano: int):

        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def liga_carro(self):

        return f'Seu carro {self.marca} {self.modelo} está ligado'

    def abastece(self, capacidade, valor_litro):
        gasto = capacidade * valor_litro
        return f'Seu {self.marca} gastará R$ {gasto:.2f} para ser abastecido.'


nave_thiago = Carro('BMW', 'X6', 2023)

print(nave_thiago)
print(type(nave_thiago))

print(nave_thiago.marca)
print(nave_thiago.modelo)
print(nave_thiago.ano)
print(nave_thiago.liga_carro())

print(nave_thiago.abastece(30, 5))
