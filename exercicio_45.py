lista_de_entrada = ["sol", "lua", "sol", "estrela", "lua", "lua"]
def conta_elemento(lista):
    contador = {}
    for elemento in lista:
        if elemento in contador:
            contador[elemento] += 1
        else:
            contador[elemento] = 1
    return contador

resultado = conta_elemento(lista_de_entrada)
print(resultado)