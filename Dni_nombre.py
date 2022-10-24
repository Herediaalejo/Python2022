from ast import Index, While
from sre_constants import RANGE
from traceback import print_last


dni=""
nombre=""
Msj=""
vecNom=[]
vecDni=[]
c=0
b=0
while(c<3):
    Msj="Ingresar nombre"
    print(Msj)
    nombre=input("")
    vecNom.append(nombre)
    Msj="Ingresar DNI"
    print(Msj)
    dni=input("")
    vecDni.append(dni)
    c+=1 
Msj="Ingresar Dni solicitado"
print(Msj)
dni=input("")
for i in vecDni:
    if(dni==i):
        nombre=vecNom[vecDni.index(i)]
        b=1
if(b==1):
    Msj="cliente " + nombre
    print(Msj)
else:
    Msj="No se encontro el cliente"
    print(Msj)



