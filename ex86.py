
dict1 = {'a': 500, 'b': 400, 'c': 300}
dict2 = {'b': 300, 'c': 200, 'd': 100}

def mescla_dicionarios(dict1, dict2):

    resultado = dict(dict1)  

    for chave, valor in dict2.items():
        if chave in resultado:
            resultado[chave] += valor
        else:
            resultado[chave] = valor  

    return resultado


dicionario_mesclado = mescla_dicionarios(dict1, dict2)

  
print("Dicionário Mesclado:")
print(dicionario_mesclado)