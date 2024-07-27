from Pessoa import Pessoa

class Estudante(Pessoa):
    curso = ''

    def altera_curso(self, curso):
        self.curso = curso

    def retorna_curso(self):
        return self.curso