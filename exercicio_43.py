lista_de_entrada = [10,20,30,40,50]

def calcula_media(lista):
    soma = 0
    for valor in lista:
        soma += valor
    media = soma / len(lista)
    return media

resultado = calcula_media(lista_de_entrada)
print(resultado)