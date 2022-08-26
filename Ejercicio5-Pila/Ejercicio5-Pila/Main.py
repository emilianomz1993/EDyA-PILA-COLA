from Pila import Pila

N=int(input("Ingrese cantidad de fichas "))
pila1=Pila(N)
for i in range(N,0,-1):
    pila1.insertar(i)
pila2=Pila(N)
pila3=Pila(N)
bandera=True
contador_movimientos=0
while bandera and (pila1.tope!=0 or pila2.tope!=0):
    opc=int(input(" 1-Mover Pieza\n 2-Terminar Intento"))
    if opc==1:
        print("Pila 1:\n")
        pila1.recorrer()
        print("Pila 2:\n")
        pila2.recorrer()
        print("Pila 3:\n")
        pila3.recorrer()
        pilaini=int(input("Ingrese pila inicio"))
        if pilaini==1:
            if pila1.tope==0:
                print("La pila 1 esta vacia")
            else:
                pilades=int(input("Ingrese pila destino"))
                if pilaini==pilades:
                    print("No se puede ingresar un disco en la misma pila de donde se tomo")
                else:
                    x=pila1.pila[pila1.tope-1]
                    pila1.suprimir()
                    if pilades==2:
                        pila2.insertar(x)
                        contador_movimientos+=1
                    elif pilades==3:
                        pila3.insertar(x)
                        contador_movimientos+=1
                    else:
                        print("Columna no valida")
        elif pilaini==2:
            if pila2.tope==0:
                print("La pila 2 esta vacia")
            else:
                pilades=int(input("Ingrese pila destino"))
                if pilaini==pilades:
                    print("No se puede ingresar un disco en la misma pila de donde se tomo")
                else:
                    x=pila2.pila[pila2.tope-1]
                    pila2.suprimir()
                    if pilades==1:
                        pila1.insertar(x)
                        contador_movimientos+=1
                    elif pilades==3:
                        pila3.insertar(x)
                        contador_movimientos+=1
                    else:
                        print("Columna no valida")
        elif pilaini==3:
            if pila3.tope==0:
                print("La pila 3 esta vacia")
            else:
                pilades=int(input("Ingrese pila destino"))
                if pilaini==pilades:
                    print("No se puede ingresar un disco en la misma pila de donde se tomo")
                else:
                    x=pila3.pila[pila3.tope-1]
                    pila3.suprimir()
                    if pilades==1:
                        pila1.insertar(x)
                        contador_movimientos+=1
                    elif pilades==2:
                        pila2.insertar(x)
                        contador_movimientos+=1
                    else:
                        print("Columna no valida")
        else:
            print("Columna no valida")
    elif opc==2:
        bandera=False
if bandera:
    print("Lo lograste en ",contador_movimientos, "movimientos de ", (2**N)-1, "minimos")
else:
    print("El juego termino sin resultado")


