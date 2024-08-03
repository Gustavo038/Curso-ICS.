class InstrumentoMusical:
    def tocar(self):
        print("Tocando um instrumento musical genérico.")


class Guitarra(InstrumentoMusical):
    def tocar(self):
        print("Tocando guitarra")



instrumento = Guitarra()
instrumento.tocar()  


instrumento_genérico = InstrumentoMusical()
instrumento_genérico.tocar()  
