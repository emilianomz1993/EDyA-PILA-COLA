class Pila:
    def __init__(self,cant):
        self.pila=[]
        self.pila = [None] * cant
        self.cant=cant
        self.tope1=0;
        self.tope2=cant-1
    def lleno(self):
        print ("La pila esta llena")
    def vacio(self):
        print ("La lista estaq vacia")
    def insertar(self,x,pila):
        if pila == 1:
            if (self.tope1 < self.cant) and (self.tope1<=self.tope2):
                self.pila[self.tope1]=x
                self.tope1=self.tope1+1
            else:
                return  self.lleno()
        elif pila==2:
            if (self.tope2 >= 0) and (self.tope2>=self.tope1):
                self.pila[self.tope2]=x
                self.tope2=self.tope2-1
            else:
                return  self.lleno()
    def suprimir(self, pila):
        if pila==1:
           if self.tope1==0:
               self.vacio()
           else:
                print("Se elimino el elemento ",self.pila[self.tope1-1]," de la lista")
                self.tope1=self.tope1-1
        elif pila==2:
            if self.tope2==self.cant-1:
                self.vacio()
            else:
                print("Se elimino el elemento ",self.pila[self.tope2]," de la lista")
                self.tope2=self.tope2+1
    def recorrer(self,pila):
        if pila==1:
            for i in range(self.tope1-1,-1,-1):
                print(self.pila[i])
        elif pila==2:
            for i in range(self.tope2+1,len(self.pila)):
                print(self.pila[i])
