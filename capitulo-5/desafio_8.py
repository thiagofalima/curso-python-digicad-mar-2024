
# Criando a função:

def imc(**kwargs):

    for pessoa, caracteristicas in kwargs.items():

        peso = caracteristicas[0]
        altura = caracteristicas[1]
        calculo = peso / altura ** 2
        print(f'O imc de {pessoa} é {calculo}')


imc(thiago=[85, 1.76], francisco=[61, 1.64])

