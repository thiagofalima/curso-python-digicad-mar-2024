

with open('hino.txt', 'r', encoding='utf-8') as hino:

    # print(hino.read())

    # conta_brasil = 0
    #
    # for palavra in hino.read().split():
    #     if "Brasil" in palavra:
    #         conta_brasil += 1
    #
    # print(f'Temos {conta_brasil} Brasil no hine nacional.')
    # # print(hino.read().split().count("Brasil"))
    texto = hino.read().replace("!", '').replace(",", '')
    print(texto.split().count("Brasil"))

