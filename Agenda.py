import os
import Funciones
Dni = ""
Nombre = ""
Telefono = ""
VecDni = []
VecNom = []
VecTelefono = []
fin = False
opcion = 0
while (fin==False):
    os.system("cls")
    Msj= "1-> Agregar, 2-> Modificar, 3-> Eliminar, 4-> Imprimir, 5-> Salir"
    print(Msj)
    opcion = int(input(""))
    if (opcion==1):
        Msj = "Ingrese el DNI"
        print(Msj)
        Dni = int(input(""))
        VecDni.append (Dni)
        Msj = "Ingrese el Nombre"
        print(Msj)
        Nombre = str(input(""))
        VecNom.append(Nombre)
        Msj = "Ingrese el Telefono"
        print(Msj)
        Telefono = int(input(""))
        VecTelefono.append(Telefono)    
    if (opcion == 3):
        Msj = "Ingresar Dni a Borrar"
        print(Msj)
        Dni = int(input(""))
        Funciones.borrar (Dni, VecDni, VecNom, VecTelefono)
        car = input("Presionar Enter")
    if (opcion == 4):
        Funciones.imprimir(VecDni, VecNom, VecTelefono)
        car = input("Presionar enter")
    if (opcion == 5):
        fin = True
    if (opcion == 2):
        print ("ingresar dni")
        dni=int(input (""))
        print ("ingresar nombre")
        nombre= str(input(""))
        print("ingresar telefono")
        telefono= int(input (""))
        Funciones.modificar(dni,nombre,telefono,VecDni,VecNom,VecTelefono)
        car=input("presione para continuar")

