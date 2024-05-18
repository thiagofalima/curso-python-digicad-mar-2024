import datetime

hoje = datetime.datetime.now()

print(hoje.year)
print(hoje.month)
print(hoje.day)
print(hoje.hour)
print(hoje.minute)
print(hoje.second)
print(hoje.microsecond)

aniversario = datetime.date(1998, 7, 11)

print(aniversario.year)
print(aniversario.month)
print(aniversario.day)

df_tempo = datetime.timedelta(10000)

print(aniversario + df_tempo)

print(f'{df_tempo.total_seconds():,}')

hora_compromisso = datetime.time(10, 30)

print(hora_compromisso)


