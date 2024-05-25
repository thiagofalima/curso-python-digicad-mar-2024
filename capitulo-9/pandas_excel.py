import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel("notas.xlsx")
# print(df)
# print(df["nome"])
# print(df.loc[5])

notas_1 = np.array(df['nota-1'])
notas_2 = np.array(df['nota-2'])

df['medias'] = (notas_1 + notas_2) / 2
# print(df)
df['status'] = ['aprovado' if media > 5 else 'reprovado' for media in df['medias']]
print(df)
df.to_excel("notas_medias.xlsx")

fig, ax = plt.subplots()
grafico = ax.bar(df['nome'], df['medias'], color= '#32012F', align='edge', width=0.5)
ax.bar_label(grafico, padding=3)
ax.set_ylim(0, 10)
plt.show()


