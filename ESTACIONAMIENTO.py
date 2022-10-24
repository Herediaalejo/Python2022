#REQUERIMIENTOS DEL SISTEMA:
#10-INGRESAR DATOS DEL VEHICULO CUANDO INGRESA AL ESTACIONAMIENTO
#20-GENERAR Y REGISTRAR TICKET CON DATOS DEL CLIENTE MENSUALIZADO
#30-INGRESAR DATOS DE VEHICULO CUANDO SALE DEL ESTACIONAMIENTO
#40-GENERAR FACTURA
#50-INGRESAR DATOS DE VEHICULO CUANDO INGRESA EN EL AREA DE LAVADO
#60-INGRESAR DATOS DE VEHICULO CUANDO SALE DEL AREA DE LAVADO
#70-GENERAR INFORME DE LOS CLIENTES MENSUALIZADOS QUE ESTAN AL DIA
#80-GENERAR INFORME DE TOTAL FACTURADO POR DIA EN ESTACIONAMIENTO 
#90-GENERAR INFORME DE TOTAL FACTURADO POR DIA EN EL LAVADO EXPRESS Y COMPLETO
#100-GENERAR INFORME DE LOS CLIENTES MENSUALIZADOS QUE ESTAN EN MORA
import os
fin=False
CMVehiculo=""
CMFecha=""
CMDatosPersonales=""
clientesMensuales=[]
infClienteMensualAlDia=[]
infClienteMensualEnMora=[]
op=0
op1=0
op2=0
while(fin==False):
    os.system("cls")
    print("Bienvenido al Sistema de Registro de Datos del estacionamiento del centro\n")
    op=int(input("1-Ingresar datos de vehiculo\n2-Registrar cliente mensual\n3-Informes\n"))
    if(op==1):
        os.system("cls")
        op1=int(input("1-Ingresar datos de vehiculo diario\n2-Ingresar datos de vehiculo a lavado\n"))
    if(op==2):
        os.system("cls")
        CMDatosPersonales=input("Datos personales del cliente: ")
        CMVehiculo=input("Datos del vehiculo: ")
        CMFecha=input("Fecha de alta: ")
        clientesMensuales.append([CMDatosPersonales,CMVehiculo,CMFecha])
    if(op==3):
        print("1-Clientes Mensuales al dia\n2-Clientes mensuales en mora\n3-Clientes")