def numero_secreto(numero_secreto):
    numeros = "1,2,3,4,5,6,7,8,,9,10"
    

    if numeros :
        return "esta palavra nao tem palíndromo"
    
    
while True:

    numeros = input("insere uma palavra")
    res = numero_secreto(numeros)
    print(res)