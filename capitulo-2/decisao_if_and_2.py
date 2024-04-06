nome = input('Entre com seu nome: ').title()
idade = int(input('Entre com sua idade: '))
cnh = input('Possui CNH (Responda com "s" ou "n"): ')

print(f'\nOi meu nome é {nome} e tenho {idade} anos de idade.\n')

if idade >= 65 and cnh == 's':
    print(f'{nome} renove sua CNH a cada 5 anos.')
elif idade >= 65 and cnh == 'n':
    print(f'{nome} não tem {idade} mas não dirige.')
elif 65 > idade >= 18 and cnh == 's':
    print(f'{nome} renove sua CNH a cada 10 anos')
elif 65 > idade >= 18 and cnh == 'n':
    print(f'{nome} tem {idade} mas não dirige.')
else:
    print(nome + ' é ' + 3 * 'jovem ainda, ')
