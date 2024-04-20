
minha_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(minha_lista)
print(type(minha_lista))

# length
print(len(minha_lista))

#count
print(minha_lista.count(8))

# append

valor = 42
minha_lista.append(valor)
minha_lista.append(56)
print(minha_lista)

lista_mista = [42, 3.14, "Hello", True]

for elemento in lista_mista:
    print(elemento)


print(minha_lista)
print(*minha_lista, sep='\n')

minha_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(max(minha_lista))
print(min(minha_lista))
print(sum(minha_lista))


lista = list(range(1, 101))
# print(lista)
# print(*lista, sep='\n')

print(lista[25])
print(lista[10])
print(lista[54])
print(lista[89])
print(lista[3])

#slicing

print(lista[0:10])
print(lista[10:20])
print(lista[4:50:2])
print(lista[:10])
print(lista[90:])
print(lista[::-1])
print(sum(lista))



