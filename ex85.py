
lista_pessoas = [
    ('Gustavo', 10),
    ('Enzo', 26),
    ('Luiz', 87),
    ('Kaique', 10),
    ('Maria Clara', 55),
    ('Ana', 12),
    ('Sarah', 90)
]


pessoas_por_idade = {}


for nome, idade in lista_pessoas:
    if idade in pessoas_por_idade:
        pessoas_por_idade[idade].append(nome)
    else:
        pessoas_por_idade[idade] = [nome]


print("Pessoas agrupadas por idade:")
for idade, nomes in pessoas_por_idade.items():
    print(f"Idade {idade}: {nomes}")