
# 1: Receber duas notas

n1 = float(input("N1: "))
n2 = float(input("N2: "))

# 2: Calular a média

# conta errada
# media = n1 + n2 / 2
# print(media)

# conta certa
media2 = (n1 + n2) / 2

# Verificando as condições
if media2 == 10:
    print("Aprovado com distinção.")
elif media2 >= 7:
    print("Aprovado")
else:
    print("Reprovado.")

