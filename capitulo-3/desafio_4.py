
senha = input("Digite sua senha (deve conter 6 digitos): ")

# while len(senha) != 6:
#     senha = input("A senha deve ter 6 caracteres\n"
#                   "Digite novamente: ")
#
# print(senha)

while True:

    if len(senha) != 6:
        senha = input("A senha deve ter 6 caracteres\n"
                      "Digite novamente: ")
        continue
    else:
        break

print(senha)

senha = input("Senha: ")
print("Digite sua senha de 6 caracteres")
while True:
    if len(senha) == 6:
        print("Senha cadastrada")
        break
    elif len(senha) != 6:
        print("Senha incorreta, por favor digite novamente")
        continue