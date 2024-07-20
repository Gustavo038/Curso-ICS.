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

    def novo_nome(self):
        return self.nome
    
    def novo_sobrenome(self):
        return self.sobrenome

pessoa = Pessoa("Gustavo", "Pereira", 18, "programador")
pessoa.nome = "Marcos"
pessoa.sobrenome = "Samuel"
print(pessoa.novo_nome() + pessoa.novo_sobrenome())