

texto = open('meu_texto.txt', 'w', encoding='utf-8')

# print(type(texto))

texto.write("Hello world \n")

texto.writelines(["Olá mundo\n", "Halo Welt\n"])

texto.writelines("e ai pareiro")

print(texto.encoding)

texto.close()