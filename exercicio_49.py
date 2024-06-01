lista_de_entrada = ["Ola", "mundo", "python", "!"]
def concatenear_strings(lista):
    concatena = ""
    for elemento in lista:
        concatena += elemento
    return concatena

resultado = concatenear_strings(lista_de_entrada)
print(resultado)