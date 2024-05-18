import datetime

hoje = datetime.datetime.now()
dif_tempo = datetime.timedelta(1000, 3600, 2)

print(dif_tempo)
print(type(dif_tempo))

dia_1000_depois = hoje + dif_tempo

print(dia_1000_depois)