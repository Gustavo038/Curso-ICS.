
dicionario_original = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4
}

def inverte_dicionario(dicionario):
    return {valor: chave for chave, valor in dicionario.items()}


dicionario_invertido = inverte_dicionario(dicionario_original)


print("Dicionário Original:")
print(dicionario_original)
print("Dicionário Invertido:")
print(dicionario_invertido)