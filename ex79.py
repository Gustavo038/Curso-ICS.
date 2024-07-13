dicionario = {
    "Brasil": "Brasília",
    "Belgica": "Bruxelas",
    "Argentina": "Buenos Aires",
    "Alemanha": "Berlim",
    "Egito": "Cairo"
    }

capital = input("A capital de qual pais você deseja atualizar: ")
capital2 = input("Qual o nome da nova Capital: ")

def atualizar_capital(paises, pais, nova_capital):
    if pais in paises:
        paises[pais] = nova_capital
        print("A capiatl de ", pais, "Foi atualizada para ", nova_capital)
    else:
        print("O pais ", pais, "não esta no dicionario")

atualizar_capital(dicionario, capital, capital2 )
print(dicionario)