contador = 0
palavra = "kaiak"
teste =  "kaiak"
    
indice_primeira_palavra = len(palavra) -1
indice_segunda_palavra = 0

while True:
    letra_palavra = palavra(indice_primeira_palavra)
    letra_teste = teste(indice_segunda_palavra)

    if letra_palavra != letra_teste:
        print('nao e um palindromo')
        break

    indice_primeira_palavra = indice_primeira_palavra - 1
    indice_segunda_palavra = indice_segunda_palavra + 1

print("parabens, a palavra e um palindromo")