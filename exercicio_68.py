minha_lista = [3, 4]
def triplicar_elemento(lista):
    nova_lista = []
    for elemento in lista:
        nova_lista.append(elemento)
        nova_lista.append(elemento)
        nova_lista.append(elemento)
    return nova_lista

resultado = triplicar_elemento(minha_lista)
print(resultado)