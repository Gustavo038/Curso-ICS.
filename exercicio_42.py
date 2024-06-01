listas_de_entrada = ["maçã","banana","kiwi","abacate","uva"]
def retorna_palavras_maiores_4(lista):
    palavras_maiores = []
    for palavras in lista:
        if len(palavras) > 4:
            palavras_maiores.append(palavras)
    return palavras_maiores

resultado =retorna_palavras_maiores_4(listas_de_entrada)
print(resultado)