class Nodo:
    def __init__(self):
        self.item=None
        self.siguiente=None
    def obteneritem(self):
        return self.item
    def ingresaritem(self,elemento):
        self.item=elemento
    def obenersig(self):
        return self.siguiente
    def cargasig(self,nodo):
        self.siguiente=nodo