sol = False
calor = False

if sol and calor:
    print('Bora para praia!')
elif sol and not calor:
    print('Bora para o parque!')
elif not sol and calor:
    print('Bora para a piscina.')
elif not sol and not calor:
    print('Netflix?')