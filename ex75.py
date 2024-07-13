dicionario = {
    "Brasil": "Brasília",
    "Belgica": "Bruxelas",
    "Argentina": "Buenos Aires",
    "Alemanha": "Berlim",
    "Egito": "Cairo"
}

pessoa = input("Digite o nome de um pais: ")

if pessoa in dicionario:
    print(f"A capital de {pessoa} é {dicionario[pessoa]}")
else:
    print(f"Não existe a capital de {pessoa} no nosso dicionario")