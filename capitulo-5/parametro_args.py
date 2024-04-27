def soma(*args):
    lista = list(args)
    print(lista)
    print(type(lista))
    return sum(lista)


print(soma(1, 2, 3, 4, 5))

