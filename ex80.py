dicionario = {
    "Brasil": "Brasília",
    "Belgica": "Bruxelas",
    "Argentina": "Buenos Aires"
} 
dicionario1 = {
    "Alemanha": "Berlim",
    "Egito": "Cairo",
    "França": "Paris"
}

dicionario2 = {**dicionario, **dicionario1}
print(dicionario2)