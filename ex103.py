class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

class Carro_eletronico(Carro):
    def __init__(self, marca, modelo, autonomia):
        self.marca = marca
        self.modelo = modelo
        self.autonomia = autonomia

    def detalhes(self):
        print(f"marca: {self.marca}")
        print(f"modelo: {self.modelo}")
        print(f"autonomia: {self.autonomia}")

Carro1 = Carro_eletronico("Nissan", "GTR-R34", "660km")
Carro1.detalhes()
