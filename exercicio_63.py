lista_numeros = [2, 3, 4, 5]
def produto_lista(numeros):
    produto = 1
    for numero in numeros:
        produto *= numero
    return produto

resultado = produto_lista(lista_numeros)
print(resultado)
