
import datetime

meu_tempo = datetime.datetime.now()

print(meu_tempo)
print(type(meu_tempo))
meu_aniversario = datetime.datetime(1998, 7, 11)

print(f'Eu já vivi {meu_tempo - meu_aniversario}.')

dias_vividos = meu_tempo - meu_aniversario
