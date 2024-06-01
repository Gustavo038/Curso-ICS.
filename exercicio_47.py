lista_de_entrada = [1, 2, 3, 4, 5]
def quadrado_impares(numeros):
    nova_lista = []
    for num in numeros:
        if num % 2 != 0:
            nova_lista.append(num ** 2)
    return nova_lista

resultado = quadrado_impares(lista_de_entrada)
print(resultado)