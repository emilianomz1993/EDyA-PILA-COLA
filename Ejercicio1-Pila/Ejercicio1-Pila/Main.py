from os import system
from PilaEncadenada import PilaEncadenada
from PilaSec import Pila
import os
import msvcrt


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


opcion=None
banderageneral=True 
while banderageneral:
    opcion=int(input("Ingrese opcion:\n 1-Pila Secuencial\n 2-Pila Encadenada\n Cualquier otro numero para salir del programa\n"))
    clear()
    if opcion==1:
        tamanio=int(input("Ingrese el tamanio de la pila"))
        pilasec=Pila(tamanio)
        clear()
        banderainterna=True
        while banderainterna:
            opcioninterna=int(input("Ingrese opcion:\n 1-Agregar elemento\n 2-Eliminar elemento\n 3-Recorrer pila\n Cualquier otro numero para salir de pila secuencial\n"))
            clear()
            if opcioninterna==1:
                valor=int(input("Ingrese elemento a la pila"))
                pilasec.insertar(valor)
                clear()
            elif opcioninterna==2:
                pilasec.suprimir()
                clear()
            elif opcioninterna==3:
                clear()
                pilasec.recorrer()
                print("Presione una tecla para continuar...")
                clear()
                msvcrt.getch()
            else:
                banderainterna=False
    elif opcion==2:
        pilaenc=PilaEncadenada()
        banderainterna=True
        while banderainterna:
            opcioninterna=int(input("Ingrese opcion:\n 1-Agregar elemento\n 2-Eliminar elemento\n Cualquier otro numero para salir de pila secuencial\n"))
            clear()
            if opcioninterna==1:
                valor=int(input("Ingrese elemento a la pila"))
                pilaenc.insertar(valor)
                clear()
            elif opcioninterna==2:
                print ("Se elimino el elemento ",pilaenc.suprimir())
                clear()
            else:
                banderainterna=False
    else:
        banderageneral=False