from Pila import PilaEncadenada

binario=PilaEncadenada()
decimal=int(input("Ingrese un numero entero: "))
bandera=True
while bandera:
    if decimal>2:
        binario.insertar(decimal%2)
        decimal=decimal//2
    else:
        if decimal == 1:
            binario.insertar(1)
        else:
            binario.insertar(0)
            binario.insertar(1)
        bandera=False
while binario.vacia()!=True:
    print(binario.suprimir())

        