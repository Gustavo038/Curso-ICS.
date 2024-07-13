def remover_funcionarios_salario_baixo(funcionarios, salario_minimo):
    funcionarios_para_remover = [funcionario for funcionario, salario in funcionarios.items() if salario < salario_minimo]
    
    for funcionario in funcionarios_para_remover:
        del funcionarios[funcionario]
    
    return funcionarios

funcionarios = {
    'Italo': 2500,
    'Vitor': 3000,
    'Thiago': 4600,
    'Samuel': 2000
}

salario_minimo = 2000

funcionarios_filtrados = remover_funcionarios_salario_baixo(funcionarios, salario_minimo)

print("Funcionários filtrados:", funcionarios_filtrados)