nome = input('Entre com seu nome: ').title()
idade = int(input('Entre com sua idade: '))

print(f'Oi meu nome é {nome} e tenho {idade} anos de idade.')

if idade >= 65:  # repare que estamos usando o operador lógico >= (maior ou igual a)
    print(f'{nome} é bem experiente.')
    cnh = input('Possui CNH (Responda com s ou n)? ')

    if cnh == 's':
        print('Renove a CNH a cada 5 anos.')
    else:
        pass
elif 65 > idade >= 18:
    print(f'{nome} é maior de idade.')
    cnh = input('Possui CNH (Responda com s ou n)? ')
    if cnh == 's':
        print('Renove a CNH a cada 10 anos.')
    else:
        pass

else:
    print(f'{nome} é menor de idade.')
