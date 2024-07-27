from Pessoa import Pessoa

class Trabalhador(Pessoa):
    empresa = ""

    def altera_empresa(self, empresa):
        self.empresa = empresa

    def retorna_empresa(self):
        return self.empresa