
dicionario = {}

print(dicionario)
print(type(dicionario))

dicionario = {"a": 1, "b": 2, "c": 3}

print(dicionario["b"])

dicionario["d"] = 4

print(dicionario)

dicionario["a"] = "novo valor"

print(dicionario)

print(dicionario.pop("d"))
print(dicionario)

del dicionario["c"]

print(dicionario)

