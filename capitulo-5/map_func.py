# def dobro(num):
#   return num * 2
#
#
# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# print(list(enumerate(lista)))
#
# for i, numero in enumerate(lista):
#   lista[i] = dobro(numero)
#
# print(lista)

# def dobro(num):
#     return num * 2
#
#
# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# lista_dobro = list(map(dobro, lista))  # Repare que a função dobro está sem ()
#
# print(lista_dobro)

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# lista_dobro = list(map(lambda x: x * 2, lista))

print(list(map(lambda x: x * 2, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))