class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome  
        self._idade = idade  

    def get_nome(self):        #para acessar e modificar o nome
        return self._nome

    def set_nome(self, nome):
        self._nome = nome

    def get_idade(self):
        return self._idade

    def set_idade(self, idade):
        if idade < 0:
            print("Erro: A idade não pode ser negativa.")
        else:
            self._idade = idade


class Funcionario(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)  
        self._salario = salario 

    def get_salario(self):
        return self._salario

    def set_salario(self, salario):
        if salario < 0:
            print("Erro: O salário não pode ser negativo.")
        else:
            self._salario = salario



pessoa = Pessoa("João", 30)
print(f'Nome: {pessoa.get_nome()}, Idade: {pessoa.get_idade()}')

funcionario = Funcionario("Maria", 28, 3000.00)
print(f'Nome: {funcionario.get_nome()}, Idade: {funcionario.get_idade()}, Salário: R$ {funcionario.get_salario():2}')


funcionario.set_salario(-1500.00)
funcionario.set_idade(29)
print(f'Nome: {funcionario.get_nome()}, Idade: {funcionario.get_idade()}, Salário: R$ {funcionario.get_salario():2}')
