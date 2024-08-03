class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self._preco = 0  
        self.set_preco(preco) 

    def get_preco(self):
        return self._preco

    def set_preco(self, valor):
        if valor < 0:
            print("Erro: O preço não pode ser negativo.")
        else:
            self._preco = valor


class ProdutoEletronico(Produto):
    def __init__(self, nome, preco, garantia):
        Produto.__init__(self, nome, preco)  
        self.garantia = garantia

    def detalhes(self):
        return f'Produto: {self.nome}, Preço: R$ {self.get_preco():2}, Garantia: {self.garantia} anos'


# Exemplo de uso
produto = Produto("Caneta", 2.50)
print(f'Produto: {produto.nome}, Preço: R$ {produto.get_preco():2}')

produto_eletronico = ProdutoEletronico("Celular", 1500.00, 1)