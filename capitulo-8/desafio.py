import datetime

ano = int(input("Ano de Nascimento: "))
mes = int(input("Mês de Nascimento: "))
dia = int(input("Dia de Nascimento: "))

aniversario = datetime.datetime(ano, mes, dia)

print(f"Você nasceu no dia: {aniversario.day}/{aniversario.month}/{aniversario.year}")