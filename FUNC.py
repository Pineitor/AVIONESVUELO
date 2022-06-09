import numpy as np
AN = 78900
AV = 240000
def comprarAsiento(listaAsientos):
    print("Tarifas: ")
    print(f"Asiento Normal 1 al 30: ${AN}")
    print(f"Asiento VIP 31 al 42: ${AV}")
    asiento = int(input("Seleccione su asiento: "))
    while asiento < 1 or asiento > 42:
        print("Asiento no existente. Seleccione otro asiento:")
        asiento=int(input())
    print("Asiento reservado")
    reserva = np.where(listaAsientos == asiento)
    listaAsientos[reserva] = 'X'
    return asiento, reserva

def validarDatos():
    nom=input("Ingrese su nombre: ")
    rut=int(input("Ingrese su rut sin puntos ni guión, si su rut termina en K reemplazar por un 0: "))
    while rut < 50000000 or rut > 300000000:
        print("Rut no válido. Vuelva a ingresar su rut: ")
        rut=int(input())
    telefono=int(input("Ingrese su teléfono (formato 9 dígitos sin +56): "))
    while telefono < 199999999 or telefono > 999999999:
        print("Teléfono ingresado no válido. Vuelva a ingresar su teléfono (formato 9 dígitos sin +56): ")
        telefono=int(input())
    print("Ingrese su banco: ")
    print("1. Banco Santander")
    print("2. Banco Falabella")
    print("3. Banco Duoc")
    print("4. Otro banco")
    banco=int(input())
    while banco < 1 or banco > 4:
        print("Banco seleccionado no válido. Vuelva a ingresar su banco: ")
        banco=int(input())
    return np.array([nom, rut, telefono, banco],dtype=object)
    


