class Pessoa:
    def _init_(self, nome_passado, sobrenome_passado, idade_passada):
        self.nome = nome_passado
        self.sobrenome = sobrenome_passado
        self.idade = idade_passada

    def nome(self):
        return self.nome + str(self.sobrenome)
    
    def idade(self):
        return self.idade
    
class Estudante(Pessoa):
    def _init_(self, nome_passado, sobrenome_passado, idade_passada, curso):
        super()._init_(nome_passado, sobrenome_passado, idade_passada)
        self.curso = curso

    def obter_curso(self):
        return self.curso
    
pessoa1 = Estudante("Gustavo ", "Pereira", 16, "programador")


print("Nome e Idade: " + pessoa1.nome() + " Curso: " + pessoa1.obter_curso())