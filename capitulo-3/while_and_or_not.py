lista_acessos = ['thiago_001', 'chave_1', 'chave_2']
controle_acesso = False

while not controle_acesso:
    chave_acesso = input('Informe sua credencial: ')

    if chave_acesso in lista_acessos:

        controle_acesso = True

    else:
        continue
print('\nBem-vindo ao sistema.')