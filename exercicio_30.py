num1 = input("digite o primeiro numero ")
num2 = input("digite o segundo numero ")

if int(num1) > int(num2):
    print("o primeiro numero e o maior")
elif int(num2) > int(num1):
    print("O segundo numero e o maior: " + num2)
else:
    print("eles sao iguais")