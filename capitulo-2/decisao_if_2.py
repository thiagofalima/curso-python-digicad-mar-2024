nome = input('Entre com seu nome: ').title()
idade = int(input('Entre com sua idade: '))
print(f'Oi meu nome é {nome} e tenho {idade} anos de idade.')

if idade >= 18:  # repare que estamos usando o operador lógico >= (maior ou igual a)
    print(f'{nome} é maior de idade!')