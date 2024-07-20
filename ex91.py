class Pessoa:
    nome = ''
    sobrenome = ''
    idade = None
    profissao = ""


    def __init__(self, nome_passado, sobrenome_passado, idade_passada, profissao_passada):
        self.nome = nome_passado
        self.sobrenome = sobrenome_passado
        self.idade = idade_passada
        self.profissao = profissao_passada

    def nova_profissao(self):
        return self.profissao

pessoa = Pessoa("Gustavo", "Pereira", 18, "profisonal")
pessoa.profissao = "Programador"
print(pessoa.nova_profissao())