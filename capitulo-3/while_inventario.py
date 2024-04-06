inventario = []
resposta = "S"

while resposta == "S":
    item = []
    item.append(input("Equipamento: "))
    item.append(float(input("Valor: ")))
    item.append(int(input("Número Serial: ")))
    item.append(input("Departamento: "))
    inventario.append(item)
    resposta = input("Digite \"S\" para continuar ou pressione enter para sair: ").upper()

for elemento in inventario:
    print(elemento)
