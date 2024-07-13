
lista_palavras = [
    'avião', 'carro', 'avião', 'moto', 'carro', 'avião'
]

def conta_ocorrencia_palavras(lista):
    ocorrencias = {}
    for palavra in lista:
        if palavra in ocorrencias:
            ocorrencias[palavra] += 1
        else:
            ocorrencias[palavra] = 1
    return ocorrencias

resultado = conta_ocorrencia_palavras(lista_palavras)


print("Ocorrência de cada palavra:")
for palavra, quantidade in resultado.items():
    print(f"{palavra}: {quantidade}")