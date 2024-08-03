class Animal:
    def som(self):
        pass

class Gato(Animal):
    def som(self):
        return "Miau"
    
gato = Gato()
print(gato.som())