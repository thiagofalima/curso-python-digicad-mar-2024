area_circunferencia = lambda raio: 3.14 * raio ** 2

print(area_circunferencia(2))
print(area_circunferencia(5))
print(area_circunferencia(10))

area_meio_de_campo = area_circunferencia(9.15)

print(f'A área da circunferência do meio de um campo de futebol'
      f' é de {area_meio_de_campo:.2f} m².')
