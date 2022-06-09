import numpy as np
import funciones as fn
AN = 78900
AV = 240000
initFlag = True
listaAsientos = np.arange(1,43,1, dtype=object)
listaAsientos = listaAsientos.reshape(7,6)
listaAsientos = np.insert(listaAsientos, (5,5), '_', axis=0)
listaAsientos = np.insert(listaAsientos, (3,3), '', axis=1)
listaAsientos = np.insert(listaAsientos, (0,8), '|', axis=1)

print("-"30)
print("   Bienvenide a Vuelos Duoc")
print("-"30)
while initFlag == True:
    try:
        print("1. Ver asientos disponibles")
        print("2. Comprar asiento")
        print("3. Anular vuelo")
        print("4. Modificar datos de pasajero")
        print("5. Salir")
        opmenu = int(input("Seleccione la acción a realizar: "))

        while opmenu < 1 or opmenu > 5:
            print("Opción seleccionada no válida")
            opmenu = int(input("Vuelva a ingresar una opción: "))