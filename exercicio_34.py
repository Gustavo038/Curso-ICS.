def numero_secreto(numero_secreto):
    numeros = "1,2,3,4,5,6,7,8,,9,10"
    senha = numero_secreto

    if numeros in senha:
        return "numeros"
    
    else:
        return "parabens vc acertou"
    
while True:

    numeros = input("Tente adivinha o numero que eu estou pensando entre em 1 a 10")
    res = numero_secreto(numeros)
    print(res)