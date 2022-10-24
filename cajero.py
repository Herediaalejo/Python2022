import os
vecUser= ["lucas45", "alejo44", "agostina01"]
vecPassword=["remo2022", "contraseña", "carpeta"]
vecSaldos=[10000, 30000, 20000]
vecResumen=[]
fin=False
user=""
password=""
saldo=0
opcion=0
extraccion=0
deposito=0
indice=0
msj=""
while(fin==False):
    print("Ingrese el Usuario:")
    user=str(input(""))
    print("Ingrese la contraseña:")
    password=str(input(""))
    for i in range(0, len(vecUser)):
        if(user==vecUser[i] and password==vecPassword[i]):
                fin=True
                saldo=vecSaldos[i]
                indice=i
    if(fin==False):
        print("Usuario incorrecto")
print("Bienvenido al SISTEMA")
fin=False
while(fin==False):
    print("1-->Extraccion\n2-->Deposito\n3-->Consultar Saldo\n4-->Resumen\n10-->Salir")
    opcion=int(input(""))
    if(opcion==10):
        fin=True
        print("Gracias por utilizar BANCOS ISAUI S.A")
    if (opcion!=1 and opcion!=2 and opcion!=3 and opcion!=4 and opcion!=10):
        print("Opcion incorrecta, ingrese nuevamente")
    if(opcion==3):
        print("Su saldo es: $" + str(saldo))
    if(opcion==1):
        print("Ingrese monto a extraer")
        extraccion=int(input(""))
        if(extraccion<=saldo):
            saldo = saldo - extraccion
            vecSaldos[indice]=saldo
            msj="Extraccion de $" + str(extraccion)
            vecResumen.append(msj)
        else:
            print("Saldo insuficiente")
        if(extraccion<=0):
            print("Extraccion INCORRECTA")
    if(opcion==2):
        print("Ingrese monto a depositar")
        deposito=int(input(""))
        saldo=saldo+deposito
        vecSaldos[indice]=saldo
        msj="Deposito de $" + str(deposito)
        vecResumen.append(msj)
    if(opcion==4):
        for i in range(0, len(vecResumen)):
            print(vecResumen[i])
    car=input("Presione ENTER")
    os.system("cls")
