dicionario = {
    "Brasil": "Brasília",
    "Belgica": "Bruxelas",
    "Argentina": "Buenos Aires",
    "Alemanha": "Berlim",
    "Egito": "Cairo"
}
pais = input("Digite um pais: ")

def Verifica_Pais(paises, dicionario):
    if paises in  dicionario:
        print("Existe esse pais em nosso dicionario")
    else:
        print("Não existe esse pais em nosso dicionario")

Verifica_Pais(pais, dicionario)