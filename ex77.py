dicionario = {
    "Brasil": "Brasília",
    "Belgica": "Bruxelas",
    "Argentina": "Buenos Aires",
    "Alemanha": "Berlim",
    "Egito": "Cairo"
}

def conta_itens(dicionario):
    return len(dicionario)

resultado = conta_itens(dicionario)
print("existem" , resultado , "itens No dicionario")