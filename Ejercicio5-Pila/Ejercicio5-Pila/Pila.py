class Pila:
    def __init__(self,cant):
        self.pila=[]
        self.cant=int(cant)
        self.tope=0;
    def lleno(self):
        print ("La pila esta llena")
    def vacio(self):
        print ("La lista estaq vacia")
    def insertar(self,x):
        if self.tope < self.cant:
            self.pila.append(x)
            self.tope=self.tope+1
        else:
            return  self.lleno()    
    def suprimir(self):
        if self.tope==0:
            self.vacio()
        else:
            self.tope=self.tope-1
    def recorrer(self):
        self.count=self.tope
        for i in range(self.tope):
            print(self.pila[self.count-1])
            self.count=self.count-1
