lista_de_entrada = [-10, 15, -20, 25, 30]

def remove_numeros_negativos(listas):
    nova_lista = []
    for numero in listas:
        if numero >= 0:
            nova_lista.append(numero)
    return nova_lista
    
resultado = remove_numeros_negativos(lista_de_entrada)
print(resultado)