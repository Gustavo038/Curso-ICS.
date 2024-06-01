lista_de_entrada = ["maça", "banana", "cereja"]
elemento = "banana"
def esta_na_lista(lista, elemento):
    if elemento in lista:
        return True
    else:
        return False
    
resultado = esta_na_lista(lista_de_entrada, elemento)
print(resultado)