
dicionario = {"nome": "Thiago", "idade": 25, "profissão": "professor"}

print(dicionario.items())

for chave, valor in dicionario.items():
    print(f'{chave} --> {valor}')


print(dicionario.keys())
print(dicionario.values())

ceps = {
      "cep": "01001-000",
      "logradouro": "Praça da Sé",
      "complemento": "lado ímpar",
      "bairro": "Sé",
      "localidade": "São Paulo",
      "uf": "SP",
      "ibge": "3550308",
      "gia": "1004",
      "ddd": "11",
      "siafi": "7107"
    }

print(type(ceps))

