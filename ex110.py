class Documento:
    def __init__(self, titulo, conteudo):
        self.titulo = titulo
        self.conteudo = conteudo


class Livro(Documento):
    def __init__(self, titulo, conteudo, autor):
        super().__init__(titulo, conteudo)  
        self.autor = autor

    def resumo(self):
        return self.conteudo[:30] + '...' if len(self.conteudo) > 30 else self.conteudo



livro = Livro("Aprendendo Python", "Este livro é uma introdução à programação em Python.", "João Silva")

print(f'Título: {livro.titulo}')
print(f'Autor: {livro.autor}')
print(f'Resumo: {livro.resumo()}')

