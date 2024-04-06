numero = int(input('Informe o número que '
                   'se deve apresentar a tabuada: '))

print(f'Vamos ver a tabuada do {numero}')

for num in range(1, 11, 1):
    print(f'{num} X {numero} = {num * numero}')
