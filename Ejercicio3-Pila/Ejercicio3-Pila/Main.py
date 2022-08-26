from Pila import PilaEncadenada

numero=int(input("Ingrese un numero entero: "))
numerox=numero
pila=PilaEncadenada()
while numerox >=1:
    pila.insertar(numerox)
    numerox-=1
numero_factorial=1
while pila.vacia()!=True:
    numero_factorial*=pila.suprimir()
print("El factorial de ", numero," es ", numero_factorial)
    
    


