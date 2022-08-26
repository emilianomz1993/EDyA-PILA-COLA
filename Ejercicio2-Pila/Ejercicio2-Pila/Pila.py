from Nodo import Nodo

class PilaEncadenada():
    def __init__(self):
        self.cantidad=0
        self.tope=None

    def vacia(self):
        return  self.cantidad==0

    def insertar(self, valor):
        nodo_pila=Nodo()
        nodo_pila.cargaitem(valor)
        nodo_pila.cargasig(self.tope)
        self.tope=nodo_pila
        self.cantidad+=1
        return nodo_pila.obteneritem()

    def suprimir(self):
        aux=Nodo
        if self.vacia():
            return print("La pila esta vacia")
        else:
            aux=self.tope
            x=self.tope.obteneritem()
            self.tope=self.tope.obenersig()
            self.cantidad-=1
            del(aux)
            return x

