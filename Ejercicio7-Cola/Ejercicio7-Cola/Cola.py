from Nodo import Nodo
class ColaEncadenada:
    def __init__(self,tiempo,frecuencia):
        self.tac=tiempo
        self.fllc=frecuencia
        self.cant=0
        self.pr=Nodo()
        self.ul=Nodo()
    def vacia(self):
        return self.cant==0
    def insertar(self, elemento):
        ps1=Nodo()
        ps1.ingresaritem(elemento)
        if self.ul.obenersig==None:
            self.pr=ps1
        else:
            self.ul.cargasig(ps1)
        self.ul=ps1
        self.cant=self.cant+1
        return self.ul.obteneritem()
    def suprimir(self):
        if self.vacia():
            print("Cola Vacia")
        else:
            aux=self.pr
            x=self.pr.obteneritem()
            self.pr=self.pr.obenersig()
            self.cant-=1
            if self.pr==None:
                self.ul==None
            return x