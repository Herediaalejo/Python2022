
import os
from datetime import datetime
import time

### VARIABLES DE LA HORA, CREO QUE SOLO SE USAN UNA VEZ ###

fecha=datetime.now()
TIME=str(fecha.strftime("%H:%M:%S"))

### VARIABLES UNIVERSALES ###

op = ""
returm = ""
msj = ""
flag = False
bucle = False
bucle2 = False
bucle3 = False
horaEst = 0
bucleLavadoReg = False
bucleLavadoCob = False
precio = 0
b=0

### VARIABLES QUE SE PODRIAN ELIMINAR Y SUSTITUIR CON OTRAS MAS GENERALES, PERO REQUERIRIA RE-ESCRIBIR VARIAS LINEAS ###

dni = ""
name = ""
matri = ""

### VARIABLES MENSUALIZADOS ###

universal = ""
matsub = []
matdom = []

plazasEst = 70
plazasLavado = 17
ingresosDiarios = 0

### USUARIOS PRE-CARGADOS ####

clientesEst=[["GHJ-435","06:41:22","6","41"],["RDJ-675","06:47:11","6","47"],["TUY-529","07:31:22","7","31"],["MA-007","07:45:10","7","45"],["LAL-793","08:23:04","8","23"]]

clientesLav=[["LOL-451","Express","08:01:32","8","1"],["RAR-717","Completo","08:22:52","8","22"],["LMH-323","Completo","08:34:56","8","34"]]

clientesmen=[["GYP-459","44608999","Carlos Javier","543541999988","carlosdaniel@gmail.com","Pasaje mendoza, balnearia","hora","minuto","2022-09-19","ACTIVO"],["ZIP-666","86963221","Gustavo Oscar","543541222208","Gustav@hotmail.com","avenida no se cuanto","hora","minuto","2022-03-24","ACTIVO"]]

legajoMen = [["GYP-459","44608999","Carlos Javier","543541999988","carlosdaniel@gmail.com","Pasaje mendoza, balnearia","hora","minuto","2022-09-19","ACTIVO"],["ZIP-666","86963221","Gustavo Oscar","543541222208","Gustav@hotmail.com","avenida no se cuanto","hora","minuto","2022-03-24","ACTIVO"]]

### BUCLE NUMERO UNO ###

while (2 > 1):
    os.system("cls")

    matri = "....."

    lavado = "....."

    ### IMPRIMIR HORA Y CUPO ###

    print("Fecha: " + str(fecha.date()))

    print("Hora: " + TIME +"\n")

    print("Plazas disponibles estacionamiento: " + str(plazasEst) + "/" + str(75))

    print("Plazas disponibles lavado: "+ str(plazasLavado) + "/" + str(20) + "\n")

    ### IMPRIMIR OPCIONES ###

    print ("1) Cliente por hora\n2) Cliente mensualizado\n3) Cliente lavado\n4) Consultar informes")

    op = input("\n:")

    os.system("cls")


    ### SI LA OPCION ES CUATRO, SE IMPRIME EL INFORME DIARIO ###

    if (op == "4"):
        bucle = True
        while (bucle == True):
            os.system("cls")
            op = input("1) Clientes en estacionamiento\n2) Balances diarios\n3) Mensualizados historicos\n4) Salir\n\n:")

            if(op == "1"):
                os.system("cls")
                msj="\nCLIENTES DIARIOS\n"
                for i in range(0,len(clientesEst)):
                    msj=msj+"Matricula: "+ clientesEst[i][0] + " HORA DE INGRESO: " + clientesEst[i][1] + "\n"
                msj=msj+"\nCLIENTES LAVADO\n"
                for i in range(0,len(clientesLav)):
                    msj=msj+"Matricula: " + clientesLav[i][0] + " TIPO DE LAVADO: " + clientesLav[i][1] + " HORA DE INGRESO: " + clientesLav[i][2] + "\n"
                print(msj)
                bucle2 = True
                while (bucle2 == True):
                    op = input("1) Salir\n2) Regresar\n:  ")
                    if (op == "1"):
                        bucle = False
                        bucle2 = False
                    elif (op == "2"):
                        bucle == True
                        bucle2 = False
                    else:
                        print ("input no admitido")
                        bucle2 = True
            
            elif(op == "2"):
                os.system("cls")
                print("DIA: " + str(fecha.date()) + " TOTAL FACTURADO: $" + str(ingresosDiarios))
                bucle2 = True
                while (bucle2 == True):
                    op = input("\n1) Salir\n2) Regresar\n:  ")
                    if (op == "1"):
                        bucle = False
                        bucle2 = False
                    elif (op == "2"):
                        bucle == True
                        bucle2 = False
                    else:
                        print ("input no admitido")
                        bucle2 = True
                        retrum = input("")

            if(op == "3"):
                os.system("cls")
                matdom = ["Matricula: ","DNI: ","Nombre y apellido: ","Numero personal: ","Correo electronico: ","Direccion: ","0","0","Fecha de registro: ","Estado de cuenta: "]
                msj="\nMENSUALIZADOS HISTORICOS\n\n"
                for r in range(0,len(legajoMen)):
                    for t in range (0,10):
                        if ((matdom[t] != "0")):
                            if ( t % 2 != 0 ):
                                msj = msj + "\n"
                            msj = msj + matdom[t]
                            msj = msj + legajoMen[r][t]
                            if ( (t % 2 != 0) and matdom[t] != "Estado de cuenta: " ):
                                msj = msj + " --- "
                    msj = msj + "\n\n"
                    
                print(msj)
                bucle2 = True
                while (bucle2 == True):
                    op = input("1) Salir\n2) Regresar\n:  ")
                    if (op == "1"):
                        bucle = False
                        bucle2 = False
                    elif (op == "2"):
                        bucle == True
                        bucle2 = False
                    else:
                        print ("input no admitido")
                        bucle2 = True


            elif (op == "4"):
                bucle = False
            
            else:
                print ("input no admitido")
                bucle = True
                retrum = input("")


    ### SI LA OPCION ES UNO, SE PREGUNTA POR REGISTRAR O COBRAR CLIENTE ###



    elif (op == "1"):

        os.system("cls")

        print("1) Registrar cliente por hora\n2) Cobro de cliente por hora\n3) Regresar")

        op = input("\n:")

        os.system("cls")

        ### SE INICIA UN BUCLE EN EL QUE SE PIDEN LOS DATOS DEL CLIENTE

        if (op == "1"):
            bucle = True
            while (bucle == True):

                os.system("cls")

                matri = ""

                name = datetime.now()

                hora = str(name.strftime("%H:%M:%S"))

                print("REGRISTRANDO USUARIO DIARIO\n\nIngrese datos de usuario:\n")

                print("\nMatricula: ......" + "\nHorario de ingreso " + hora)

                matri = input("Ingresar Matricula:  ")

                os.system("cls")

                print ("\nMatricula: " + str(matri) + "\nHorario de ingreso: " + hora)

                horaH = str(name.hour)

                horaM = str(name.minute)

                clientes=[matri, hora, horaH, horaM,]

                print ("\nDatos correctos?\n1)SI\n2)NO\n3)CANCELAR")

                op = input("\n:")

                if (op == "1" or op == "SI" or op == "si" or op == "Si" ):
                    bucle = False
                    clientesEst.append(clientes)
                    plazasEst = plazasEst - 1
                    print("\nCliente agregado correctamente")
                    op = input("\nPresiona ENTER para continuar")
                elif (op == "2" or op == "NO" or op == "no" or op == "No" ):
                    bucle = True
                elif (op == "3" or op == "CANCELAR" or op == "cancelar" or op == "Cancelar" ):
                    bucle = False
                else:
                    print("\nopcion no admitida")

        ### ------------ ###

        elif (op == "2"):
        
            hora=datetime.now()
            horaEgreso=hora.strftime("%H:%M:%S")
            matri = input("Ingresar matricula del vehiculo a cobrar    :")

            for i in range(0, len(clientesEst)):
                for k in range(0,4):

                    if (clientesEst[i][k] == matri):

                        b=1
                        indice=i
                        horaI = int(clientesEst[i][2])
                        minI = int(clientesEst[i][3])
                        horaE = hora.hour
                        minE = hora.minute

                        if (horaE > horaI):
                            horaEst=horaE-horaI
                            if(minE>(minI+15)):
                                horaEst=horaEst+1
                        else:
                            horaEst=1
                        cash = 200*horaEst
                        print("\nMatricula:" + str(clientesEst[i][0]) + "\nHORA DE INGRESO: " + str(clientesEst[i][1]) + "\nHORA DE EGRESO: " + horaEgreso + "\nHORAS ESTACIONADAS: " + str(horaEst) + " horas\nPRECIO A PAGAR: $" + str(cash))
                        diario = [indice, cash]

            if(b==0):
                print("\nCliente no encontrado")
                op=input("\nPresione ENTER para continuar")
            if(b==1):
                cobro = diario
                plazasEst = plazasEst + 1
                clientesEst.pop(cobro[0])
                ingresosDiarios = ingresosDiarios + cobro[1]
                op=input("\nPresione ENTER para continuar")

        elif (op == "3"):
            bucle = False


    ### CLIENTE MENSUALIZADO ###

    elif (op == "2"):
        bucle = True
        while (bucle == True):

            os.system("cls")

            print("1) Administrar cliente mensual\n2) Ingreso de cliente mensual\n3) Salida cliente mensual\n4) Regresar")

            op = input("\n:")

            os.system("cls")

            if (op == "1"):
                bucle2 = True
                while (bucle2 == True):

                    os.system("cls")
                    print("1) Registrar cliente mensual\n2) eliminar cliente mensual\n3) Mostrar clientes mensuales\n4) Regresar")

                    op = input("\n:")

                    os.system("cls")


                    if (op == "1"):
                        bucle3 = True

                        while (bucle3 == True):

                            matsub = ["......","......","......","......","......","......",]
                            matdom = ["Matricula","DNI","Nombre y apellido","Numero personal","Correo electronico","Direccion"]

                            ### MATRICULA, DNI, NOMBRE, NUMERO, CORREO, DIRECCION, HORA, MINUTO, ESTADO ###
                            ###     0       1     2        3       4        5        6      7       8   ###

                            for i in range (0,len(matdom)):

                                print("REGRISTRANDO USUARIO MENSUAL\n\nIngrese datos de cliente:\n")

                                print ("\nMatricula : "+ matsub[0] +"\nDNI : "+ matsub[1])
                                print ("\nNombre y apellido : "+ matsub[2] +"\nNumero personal : "+ matsub[3])
                                print ("\nCorreo elecrinico : "+ matsub[4] +"\nDireccion : "+ matsub[5])

                                print ("\n1) CANCELAR\n")

                                universal = input("Ingresar "+ matdom[i] +"   :  ")

                                if (universal == "1" or universal == "CANCELAR" or universal == "cancelar" or universal == "Cancelar"):
                                    bucle3 = False
                                    break

                                matsub[i]= universal
                                os.system("cls")
                            if (universal == "1" or universal == "CANCELAR" or universal == "cancelar" or universal == "Cancelar"):
                                print("")
                            else:
                                print("REGRISTRANDO USUARIO MENSUAL\n\nIngrese datos de cliente:\n")

                                print ("\nMatricula : "+ matsub[0] +"\nDNI : "+ matsub[1])
                                print ("\nNombre y apellido : "+ matsub[2] +"\nNumero personal : "+ matsub[3])
                                print ("\nCorreo elecrinico : "+ matsub[4] +"\nDireccion : "+ matsub[5])

                                print("\n¿Datos correctos?\n1) SI\n2) NO\n3) CANCELAR")

                                op = input("\n:")

                                if (op == "1"):
                                    bucle3 = False
                                    matsub.append("hora")
                                    matsub.append("minuto")
                                    matsub.append(str(fecha.date()))
                                    matsub.append("ACTIVO")   
                                    clientesmen.append(matsub)
                                    legajoMen.append(matsub)
                                if (op == "2"):
                                    bucle3 = True 
                                if (op == "3" or op == "CANCELAR" or op == "cancelar" or op == "Cancelar"):
                                    bucle3 = False
                    
                    elif (op == "4"):
                        bucle2 = False


                    ### ESO CONCLUYE EL REGISTRO DE LOS MENSUALES ###

                    elif (op == "3"):
                        msj = ""
                        for i in range (0,len(clientesmen)):
                            for k in range (0,8):
                                msj = msj + clientesmen[i][k] + " | "
                            msj = msj + "\n"

                        print (msj)
                        op = input("\n:")

                    elif (op == "2"):

                        bucle2 = True
                        op = input("\nIngresar matricula de cliente mensualizado que desea dar de baja  :")
                        flag = False
                        universal = 0
                        for i in range (0,len(clientesmen)):
                            for k in range (0,10):                           
                                if (op == clientesmen[i][k]):

                                    os.system("cls")
                                    print("Ingresar matricula de cliente mensualizado que desea dar de baja  :" + str(op))
                                    print("\n1) DAR DE BAJA\n2) CANCELAR")
                                    op = input(":")

                                    if (op == "1"):
                                        flag = True
                                        universal = i
                                        legajoMen[i][9] = "INACTIVO"
                                        bucle2 = False
                                    elif (op == "2"):
                                        bucle2 = False
                        

                        if (flag == True):
                            print("\ncliente mensual correctamente retirado\n")
                            plazasEst = plazasEst + 1
                            clientesmen.pop(universal)
                            op = input("\n:")
                            bucle2 = False

                        elif (flag == False and op == "2"):
                            print("\ncliente mensual no retirado\n")
                            op = input("\n:")
                            bucle2 = False

                        elif (flag == False and op != "2"):
                            print("\ncliente mensual no encontrado\n")
                            op = input("\n:")
                            bucle2 = True

            elif (op == "2"):
                bucle2 = True
                op = input("\nIngresar matricula de cliente mensualizado  :")
                universal = "0"
                for i in range (0,len(clientesmen)):

                    if (op == clientesmen[i][0] and clientesmen[i][8]!="hora"):
                        print ("\nEl cliente ya se encuentra dentro del estacionamiento")
                    
                    if (op == clientesmen[i][0] and clientesmen[i][8]=="hora"):
                        hora=datetime.now()
                        clientesmen[i][8]=str(hora.hour)
                        clientesmen[i][9]=str(hora.minute)
                        universal = "1"

                if (universal == "1"):
                    print("\ncliente mensual correctamente ingresado\n")
                    plazasEst = plazasEst - 1
                    op = input("\n:")
                    bucle2 = False
                else:
                    print("\ncliente mensual no encontrado\n")
                    op = input("\n:")
                    bucle2 = True

            elif (op == "3"):
                bucle2 = True
                op = input("\nIngresar matricula de cliente mensualizado  :")
                universal = "0"
                for i in range (0,len(clientesmen)):

                    if (op == clientesmen[i][0] and clientesmen[i][8]=="hora"):
                        print ("\nEl cliente no se encuentra dentro del estacionamiento")
                    
                    if (op == clientesmen[i][0] and clientesmen[i][8]!="hora"):

                        clientesmen[i][8]="hora"
                        clientesmen[i][9]="minuto"
                        universal = "1"

                if (universal == "1"):
                    print("\ncliente mensual correctamente retirado\n")
                    plazasEst = plazasEst + 1
                    op = input("\n:")
                    bucle2 = False
                else:
                    print("\ncliente mensual no encontrado\n")
                    op = input("\n:")
                    bucle2 = True

            if (op == "4"):
                bucle = False

    ### LAVADO ###

    elif(op=="3"):

        os.system("cls")

        name = datetime.now()

        hora = str(name.strftime("%H:%M:%S"))

        horaH = str(name.hour)

        horaM = str(name.minute)

        op = input("1)Registrar cliente lavado \n2)Cobrar a cliente lavado\n:")

        if(op=="1"):
            bucleLavadoReg = True
        if(op=="2"):
            bucleLavadoCob = True

        while(bucleLavadoReg==True):

            os.system("cls")

            print("REGISTRANDO USUARIO LAVADO\n\nIngrese datos de usuario:\n")

            print("\nMatricula: " + matri +"\nTipo de lavado: " + lavado + "\nHorario de ingreso " + hora)

            if(matri=="....."):

                matri = input("Ingresar Matricula: ")

            elif(lavado=="....."):

                opLavado = int(input("Ingrese tipo de lavado: \n\n1)Express\n2)Completo\n:"))

                if(opLavado==1):
                    lavado="Express"
                if(opLavado==2):
                    lavado="Completo"

            else:
        
                clienteLavado=[matri, lavado, hora, horaH, horaM]

                print ("\nDatos correctos?\n1)SI\n2)NO\n3)CANCELAR")

                op = input("\n:")

                if (op == "1" or op == "SI" or op == "si" or op == "Si" ):

                    bucleLavadoReg = False
                    clientesLav.append(clienteLavado)
                    plazasLavado = plazasLavado - 1
                    print("Cliente agregado correctamente")
                    op = input("Presione ENTER para continuar")

                elif (op == "2" or op == "NO" or op == "no" or op == "No" ):

                    bucleLavadoReg = True
                    matri="....."
                    lavado="....."

                elif (op == "3" or op == "CANCELAR" or op == "cancelar" or op == "Cancelar" ):

                    bucleLavadoReg = False

                else:

                    print("\nopcion no admitida")
        while(bucleLavadoCob==True):

            hora=datetime.now()
            horaEgreso=hora.strftime("%H:%M:%S")
            matri = input("Ingresar matricula del vehiculo a cobrar    :")

            for i in range(0, len(clientesLav)):
                for k in range(0,4):

                    if (clientesLav[i][k] == matri):
                        b=1
                        tipo=""
                        indice=i
                        horaCompI=clientesLav[i][2]
                        matri=clientesLav[i][0]
                        horaI = int(clientesLav[i][3])
                        minI = int(clientesLav[i][4])
                        tipo = clientesLav[i][1]
                        horaE = hora.hour
                        minE = hora.minute
                        if(tipo=='Express' or tipo=='express'):
                            precio=500
                        elif(tipo=='Completo' or tipo=='completo'):
                            precio=1000
                        if (horaE > horaI):
                            horaEst=horaE-horaI
                        if(minE>(minI+15)):
                            horaEst=horaEst+1
                        precio = precio + (200 * horaEst)
                        print("\nMatricula: " + matri +"\nTipo de Lavado: " + tipo + "\nHORA DE INGRESO: " + horaCompI + "\nHORA DE EGRESO: " + horaEgreso + "\nHORAS ESTACIONADAS: " + str(horaEst) + " horas" + "\nPRECIO A PAGAR: $" + str(precio))
                        lav = [indice, precio]
            if(b==0):
                print("\nCliente no encontrado")
                bucleLavadoCob=False
                op=input("\nPresione ENTER para continuar")
            if(b==1):
                plazasLavado = plazasLavado + 1
                clientesLav.pop(lav[0])
                ingresosDiarios = ingresosDiarios + lav[1]
                print("\nCliente agregado correctamente")
                op=input("\nPresione ENTER para continuar")
                bucleLavadoCob=False
                b=0