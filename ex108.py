class Veiculo:
    def quantidade_de_rodas(self):
        return 0  


class Moto(Veiculo):
    def quantidade_de_rodas(self):
        return 2  


class Carro(Veiculo):
    def quantidade_de_rodas(self):
        return 4  



moto = Moto()
carro = Carro()

print(f'Uma moto tem {moto.quantidade_de_rodas()} rodas.')
print(f'Um carro tem {carro.quantidade_de_rodas()} rodas.')
