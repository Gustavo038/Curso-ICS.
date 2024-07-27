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
    
    def imprimir_dados_completos(self):
        return "Dados completos: " + self.nome + self.sobrenome + str(self.idade) + self.profissao + self.endereco
    
    def aniversario(self):
       self.idade += 1

    def retorna_endeco(self):
        return self.endereco
    
    def modifica_profissao(self, nova_profissao):
        self.profissao = nova_profissao

    def quem_e_mais_velho(pessoa1, pessoa2):
        if pessoa1.idade >  pessoa2.idade:
            print( pessoa1.nome + "e mais velho(a) do que " + str(pessoa2.nome))
        elif pessoa2.idade > pessoa1.idade:
            print( pessoa2.nome + "é mais velho(a) do que " + str(pessoa1.nome))
        else:
            print("Eles(a) tem a mesma idade")

    def imprimir_nome_completo(self):
        return self.nome + self.sobrenome