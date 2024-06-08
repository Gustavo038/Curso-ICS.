numeros = [1, 2, 3, 4, 5]
def soma_lista(numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total

resultado = soma_lista(numeros)
print(resultado)