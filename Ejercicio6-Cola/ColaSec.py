class ColaCricular:
    def __init__(self,cant):
        self.pr=0
        self.ul=0
        self.cant=0
        self.tamaño=cant
        self.cola=[]
    def vacia(self):
        return self.cant==0
    def insertar(self,elem):
        if(self.tamaño>self.cant):
            self.cola[self.ul]=elem
            self.ul=(self.ul+1)%self.tamaño
            self.cant+=1
            return elem
        else:
            return None
    def suprimir(self):
        if self.vacia():
            print("La cola esta vacìa")
        else:
            x=self.cola[self.pr]
            self.pr=(self.pr+1)%self.tamaño
            self.cant-=1
            return x
    def recorrer(self):
        if not(self.vacia()):
            for i in range(self.pr,self.ul,1):
                print(self.cola[i])
    
