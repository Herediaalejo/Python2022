def promedio(vector):
    suma=0
    prom=0
    for i in range (0, len(vector)):
        suma= suma + vector[i]
    if (len(vector)>0):
        prom=suma/len(vector)
    return prom
def mayor(vector):
    may=0
    for i in range(0, len(vector)):
        if(i==0):
            may=vector[i]
        if (vector[i] > may):
            may=vector[i]
    return may
def imprimir (Vec1, Vec2, Vec3):
    Msj= ""
    for i in range (0, len(Vec1)):
        print("-------------------------------")
        Msj= "Dni: " + str(Vec1[i])
        Msj = Msj + " Nombre: " + str(Vec2[i])
        Msj = Msj + " Telefono: " + str(Vec3[i])
        print(Msj)

def borrar(Dni, Vec1, Vec2, Vec3):
    Msj = ""
    b = 0
    indice = 0
    for i in range (0, len(Vec1)):
        if (Dni == Vec1[i]):
            indice = i
            b = 1
    if (b==1):
        Vec1.pop(indice)
        Vec2.pop(indice)
        Vec3.pop(indice)
        Msj = "Contacto Borrado"
    else:
        Msj="No existe Dni"
    print(Msj)

def modificar(dni,nombre,telefono,vec1,vec2,vec3):
    b=0
    for i in range (0,len(vec1)):
        if (dni == vec1[i]):
            vec2[i]=nombre
            vec3[i]=telefono
            b=1
    if (b==1):
        print ("cliente actualizado")
    else: 
        print("cliente inexistente")

def validacion (usuario, clave, vec1, vec2):
    b=0
    for i in range(0, len(vec1)):
        if(usuario==vec1[i]) and (clave==vec2[i]):
            b=1
    if (b==1):
        print("Ha ingresado correctamente")
    else:
        print("Usuario y/o clave incorrectos")


def imprimirAlineadoTresCifras(mat):
    can=0
    msj=""
    for i in range(0, len(mat)):
        for k in range(0, len(mat)):
            can = len(str(mat[i][k]))
            if(can==1):
                msj = msj + "   " + str(mat[i][k])
            if(can==2):
                msj = msj + "  " + str(mat[i][k])
            if(can==3):
                msj = msj + " " + str(mat[i][k])
        msj = msj + "\n" 
    print(msj)







""" 
Msj = "Ingrese el DNI que desea modificar"
        print(Msj)
        print (VecDni)
        Dni = int(input(""))
        VecDni.remove(Dni)
        Msj = "Ingrese el nuevo DNI"
        print(Msj)
        Dni = int(input(""))
        VecDni.append (Dni)
        Msj = "Ingrese el nombre que desea modificar"
        print(Msj)
        Nombre = str(input(""))
        VecNom.remove(Nombre)
        Msj = "Ingrese el nuevo Nombre"
        print(Msj)
        Nombre = str(input(""))
        VecNom.append(Nombre)
        Msj ="Ingrese el telefono que desea modificar"
        print(Msj)
        Telefono = int(input(""))
        VecTelefono.remove(Telefono)
        Msj = "Ingrese el nuevo Telefono"
        print(Msj)
        Telefono = int(input(""))
        VecTelefono.append(Telefono) """