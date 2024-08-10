pedidos = [
    {"tipo": "Comida", "nome": "Hambúrguer", "preco": 15.50, "calorias": 500},
    {"tipo": "Bebida", "nome": "Coca-Cola", "preco": 5.00, "tamanho": "350ml"},
    {"tipo": "Comida", "nome": "Salada", "preco": 10.00, "calorias": 150},
    {"tipo": "Bebida", "nome": "Suco de Laranja", "preco": 7.00, "tamanho": "400ml"}
]

class ItemPedido:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


class Comida(ItemPedido):
    def __init__(self, nome, preco, calorias):
        super().__init__(nome, preco)
        self.calorias = calorias
    def descrever(self):
        return f"Comida: {self.nome}, custa {self.preco} reais e tem {self.calorias} calorias."


class Bebida(ItemPedido):
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self.tamanho = tamanho
    def descrever(self):
        return f"Bebida: {self.nome}, custa {self.preco} reais e tem {self.tamanho}."


def processar_pedidos(pedidos):
    itens = []
    for pedido in pedidos:
        if pedido["tipo"] == "Comida":
            item = Comida(pedido["nome"], pedido["preco"], pedido["calorias"])
        elif pedido["tipo"] == "Bebida":
            item = Bebida(pedido["nome"], pedido["preco"], pedido["tamanho"])
        itens.append(item)
    
    
    for item in itens:
        print(item.descrever())
processar_pedidos(pedidos)
