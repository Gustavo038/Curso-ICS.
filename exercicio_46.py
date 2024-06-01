lista_de_entrada = (5, 3, 9, 1, 10)
def encontra_maior_numero(lista):
    maior_numero = lista[0]
    for numero in lista:
        if numero > maior_numero:
            maior_numero = numero
    return maior_numero

resultado = encontra_maior_numero(lista_de_entrada)
print(resultado)