dicionario = {
    "Brasil": "Brasília",
    "Belgica": "Bruxelas",
    "Argentina": "Buenos Aires",
    "Alemanha": "Berlim",
    "Egito": "Cairo"
}

pessoa = input("Digite o nome de um pais: ")

if pessoa in dicionario:
    print(dicionario[pessoa])
else:
    print("Não existe a capital de: " + pessoa + " No nosso dicionario")