# TODO: Receber n números do usuário

lista = []

while True:

    num = input("Digite um número (ou s para sair): ").lower()
# TODO: armazenar em uma lista
    if num != 's':
        lista.append(int(num))
    else:
        break

# print(lista)

# TODO: remover os itens repetidos e ordenar

# s = set(lista)

# print(s)

# s = sorted(s)

lista_final = sorted(set(lista))

# print(type(s))

# TODO: e apresentar ao usuario

print(lista_final)
