import random
from telnetlib import TM
from Cola import ColaEncadenada

total=int(input("Ingrese la cantidad en minutos de tiempo de atencion total del banco\n"))
cant=int(input("Ingrese un numero entero que indique los minutos de atencion del cajero\n"))
frec=int(input("Ingrese un numero entero que reprecenta la frecuencia de llegada de clientes\n"))
cola=ColaEncadenada(cant,frec)
aux_cant=total
aux_te=0
cont=cola.tac
tm=0
while aux_cant!=0:
    x=random.uniform(0,1)
    if x <= 1/cola.fllc:
        if cola.vacia():
            (cola.insertar(aux_te)
            aux_te+=cola.tac
        else:
            cola.insertar(aux_te)
            aux_te+=cola.tac
    aux_cant-=1
    aux_te-=1
    if cont==0:
        tm=cola.pr.obteneritem()
        cola.suprimir()
        cont=cola.tac
    else:
        cont-=1
print("El tiempo maximo de espera de la simulacion es: ",tm)
    


