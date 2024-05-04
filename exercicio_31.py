def solicitando_numero_par_impar(numero):
    lista_impar = "1,3,5,7,9"
    ultimo_numero = numero[-1]

    if ultimo_numero in lista_impar:
        return "impar"
    
    else:
        return "par"
    
while True:

    numero_par = input("Digite um numero")
    res = solicitando_numero_par_impar(numero_par)
    print(res)