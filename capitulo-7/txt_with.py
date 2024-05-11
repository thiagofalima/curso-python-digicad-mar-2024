

with open("arquivo_novo.txt", 'w', encoding='utf-8') as arquivo:
    arquivo.writelines(["Arquivo novo", "A Laura ta com fome"])

with open("arquivo_novo.txt", 'r', encoding='utf-8') as arquivo:
    print(arquivo.read())