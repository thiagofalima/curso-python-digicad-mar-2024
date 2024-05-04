# def numeros_pares(num):
#     return num % 2 == 0  # => True ou False
#
#
# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# lista_pares = list(filter(numeros_pares, lista))
# print(lista_pares)

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista_pares = list(filter(lambda x: x % 2 == 0, lista))
print(lista_pares)

print(list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))