class Pessoa:

    def _init_(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def criar_pessoa_anonima(nome, sobrenome):
        return (nome + sobrenome)
    
pessoa1 = Pessoa.criar_pessoa_anonima("Anônimo ", "Jóse")
print(pessoa1)