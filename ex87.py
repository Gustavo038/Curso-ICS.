
notas_alunos = {
    'Ana': 9.0,
    'Luiz': 7.0,
    'Maria': 8.0,
    'Sarah': 7.0,
    'kaique': 8.9
}

tabela_conversao = {
    (9.0, 10.0): 'A',
    (8.0, 9.0): 'L',
    (7.0, 8.0): 'M',
    (6.0, 7.0): 'S',
    (0.0, 6.0): 'K'
    
}

def converter_notas_para_conceitos(notas, tabela):
    conceitos = {}
    for aluno, nota in notas.items():
        for faixa, conceito in tabela.items():
            if faixa[0] <= nota < faixa[1]:
                conceitos[aluno] = conceito
                break  
    return conceitos


conceitos_alunos = converter_notas_para_conceitos(notas_alunos, tabela_conversao)



print("Conceitos dos alunos:")
for aluno, conceito in conceitos_alunos.items():
    print("{aluno}: {conceito}")