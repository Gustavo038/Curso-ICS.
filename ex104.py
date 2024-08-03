class Funcionario:
    def __init__(self, nome):
        self.nome = nome

    def calcular_salario(self):
        return 0 


class FuncionarioHorista(Funcionario):
    def __init__(self, nome, horas_trabalhadas, taxa_por_hora):
        Funcionario.__init__(self, nome)  
        self.horas_trabalhadas = horas_trabalhadas
        self.taxa_por_hora = taxa_por_hora

    def calcular_salario(self):
        return self.horas_trabalhadas * self.taxa_por_hora



funcionario = Funcionario("João")
print(f"Salário de {funcionario.nome}: R$ {funcionario.calcular_salario()}")

funcionario_horista = FuncionarioHorista("Maria", 40, 15)
print(f"Salário de {funcionario_horista.nome}: R$ {funcionario_horista.calcular_salario()}")

