
class Pessoa:

    nome = ''
    quantidade = 0
    
    def __init__(self, nome):
        self.nome = nome
        Pessoa.quantidade += 1 
    
    def quantidade_pessoas():
        return Pessoa.quantidade

pessoa1 = Pessoa("Julia")
pessoa2 = Pessoa("Pedro")
pessoa3 = Pessoa("joao")

print(Pessoa.quantidade_pessoas())