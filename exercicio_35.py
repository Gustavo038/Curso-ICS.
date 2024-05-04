def contador_de_letras(numero_secreto):
    numeros = "1,2,3,4,5,6,7,8,,9,10"
    

    if numeros :
        return "esta palavra tem 6 letras"
    
    else:
        return "parabens vc acertou"
    
while True:

    numeros = input("insere uma palavra")
    res = contador_de_letras(numeros)
    print(res)