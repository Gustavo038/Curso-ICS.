
num1 = input("digite o primeiro numero ")
num2 = input("digite o segundo numero ")
operacao = input("digite qual operacao vc deseja + - * /")

if operacao == "+":
    soma = int(num1) + int(num2)
    print(soma)
elif operacao == "-":
    subtracao = int(num1) - int(num2)
    print(subtracao)
elif operacao == "*":
    multiplicacao = int(num1) * int(num2)
    print(multiplicacao)
elif operacao == "/":
    divisao = int(num1) / int(num2)
    print(divisao)
