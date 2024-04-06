# recebendo os dados:

a = int(input("Entre com o lado a: "))
b = int(input("Entre com o lado b: "))
c = int(input("Entre com o lado c: "))

# Verificando se o tipo do triângulo

# Equilátero
if a == b == c:
    print("Equilatero")
# Isóceles
elif a == b or b == c or c == a:
    print("Isóceles")
# else:
#     print("Escaleno")
elif a != b != c:
    print("Escaleno")
