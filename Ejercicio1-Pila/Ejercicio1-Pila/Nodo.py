class Nodo:
    def __init__(self):
        self.siguiente=None
        self.item=None

    def obteneritem(self):
        return self.item

    def cargaitem(self,valor):
        self.item=valor

    def obenersig(self):
        return self.siguiente

    def cargasig(self, sig):
        self.siguiente=sig