import math

# print('oi')

def soma(a: int, b: int):
    return a + b


result = soma(10, 2)

print(result)


def area_circ(raio: float):
    return math.pi * raio ** 2


# a1 = area_circ()
a2 = area_circ(3.0)

# print(a1)
print(a2)


def titulo(palavra: str, nome: str) -> str:
    return palavra.title() + " - " + nome.title()


print(titulo(nome="Thiago", palavra="Monstro"))
