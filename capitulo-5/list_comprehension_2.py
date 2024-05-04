

lista_multiplos_5 = [n for n in range(1, 51) if n % 5 == 0]
print(lista_multiplos_5)

lista_completa = [n if n % 5 == 0 else 'n' for n in range(1, 51)]

print(lista_completa)