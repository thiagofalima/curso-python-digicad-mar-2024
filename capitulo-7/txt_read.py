

texto = open("meu_texto.txt", 'r', encoding='utf-8')

print(texto.read().split())

# print(texto.readlines())
#
# for linha in texto.readlines():
#     print(linha)

texto.close()