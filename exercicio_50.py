listas_de_entrada = [1, 2, 3, 4, 5]
def inverter_listas(lista):
    lista_invetida = []
    for elemento in lista:
        lista_invetida.insert(0, elemento)# o insert serve para determinar uma posição em python 
    return lista_invetida

resultado = inverter_listas(listas_de_entrada)
print(resultado)