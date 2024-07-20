class Pessoa:
    nome = ''
    sobrenome = ''
    idade = None
    profissao = ""
    endereco = ""

    def __init__(self, nome_passado, sobrenome_passado, idade_passada, profissao_passada, endereco_passado):
        self.nome = nome_passado
        self.sobrenome = sobrenome_passado
        self.idade = idade_passada
        self.profissao = profissao_passada
        self.endereco = endereco_passado
    
    def imprimir_dados_completos(self,):
        return self.nome + self.sobrenome + self.profissao + str(self.idade)

pessoa1 = Pessoa("Gustavo", "Pereira", 16, " profisonal ", " Rua h numero 555")
pessoa2 = Pessoa("João ", "Pedro", 20 , "Programador ", " Rua j numero 454")
pessoa3 = Pessoa("Julia", "Lacerda", 26 , "Atriz ", "Rua i numero 501")

print(Pessoa.imprimir_dados_completos(pessoa1))
print(Pessoa.imprimir_dados_completos(pessoa2))
print(Pessoa.imprimir_dados_completos(pessoa3))