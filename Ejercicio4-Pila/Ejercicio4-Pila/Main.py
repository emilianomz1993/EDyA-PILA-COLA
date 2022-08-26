from Pila import Pila
import msvcrt

valor=int(input("Ingrese dimension de la pila compartida: "))
pila_compartida=Pila(valor)
banderageneral=True 
while banderageneral:
    opcion=int(input("Ingrese opcion:\n 1-Ingresar elemento a pila\n 2-Eliminar elemento de pila\n 3-Recorrer pila\n Cualquier otro numero para salir del programa\n"))
    if opcion==1:
        opcioninterna=int(input("Ingrese opcion:\n 1-Agregar elemento a pila 1\n 2-Agregar elemento a pila 2\n"))
        if opcioninterna==1:
            valor=int(input("Ingrese elemento a la pila 1: "))
            pila_compartida.insertar(valor,1)
        elif opcioninterna==2:
            valor=int(input("Ingrese elemento a la pila 2: "))
            pila_compartida.insertar(valor,2)
    elif opcion==2:
        opcioninterna=int(input("Ingrese opcion:\n 1-Eliminar elemento de pila 1\n 2-Eliminar elemento de pila 2\n"))
        if opcioninterna==1:
            pila_compartida.suprimir(1)
        elif opcioninterna==2:
            pila_compartida.suprimir(2)
    elif opcion==3:
        opcioninterna=int(input("Ingrese opcion:\n 1-Recorrer pila 1\n 2-Recorrer pila 2\n"))
        if opcioninterna==1:
            pila_compartida.recorrer(1)
        elif opcioninterna==2:
            pila_compartida.recorrer(2)
    else:
        banderageneral=False