import os
tablero1J1 = []
tablero2J1 = []
tablero1J2 = []
tablero2J2 = []
fin = False
op = 0
msj="   A B C D E F G H I J\n"
con=1
letra=""
numero=0
posicionLetra=0
op2=0
longBarco=0
A=0
B=0
msj2=""
B5="1-Barco de 5 casilleros"
B4="2-Barco de 4 casilleros"
B3_1="3-Barco de 3 casilleros"
B3_2="4-Barco de 3 casilleros"
B2="5-Barco de 2 casilleros"
BARCO5=[]
BARCO4=[]
BARCO3_1=[]
BARCO3_2=[]
BARCO2=[]
jugador=1
jugador2=False
bandera=False
car=""
fin2=False
modo=1
T1J1=""
T1J2=""
T2J1=""
T2J2=""
p5=0
p4=0
p3_1=0
p3_2=0
p2=0
pun=0
BarcoAtacado=0
for i in range(0, 10):
    tablero1J1.append(["-"]*10)
    tablero2J1.append(["-"]*10)
    tablero1J2.append(["-"]*10)
    tablero2J2.append(["-"]*10)
while(fin==False):
    if(modo==1):
        print("BIENVENIDOS A LA BATALLA NAVAL\n\nES EL TURNO DEL JUGADOR " + str(jugador) + "\n\nELIJA UN BARCO PARA COLOCAR EN EL TABLERO\n")
    if(modo==2):
        print("ES EL MOMENTO DE ATACAR!!\n\nES EL TURNO DEL JUGADOR " + str(jugador) + "\n\nElija coordenada de ATAQUE!" )
    for i in range(0,10):
        for k in range(0, 10):
            if(k==0 and con!=10):
                msj=msj+" " + str(con)+" "
                con=con+1
            if(i==9 and k == 0):
                msj=msj + str(con)+" "
            if(jugador==1 and modo==1):
                msj=msj+tablero1J1[i][k] + " "
            if(jugador==2 and modo==1):
                msj=msj+tablero1J2[i][k] + " "
            if(jugador==1 and modo==2):
                msj=msj+tablero2J1[i][k] + " "
            if(jugador==2 and modo==2):
                msj=msj+tablero2J2[i][k] + " "
        msj = msj + "\n"
    print(msj)
    if(jugador==1 and modo==1):
        T1J1=msj
    if(jugador==2 and modo==1):
        T1J2=msj
    if(jugador==1 and modo==2):
        T2J1=msj
    if(jugador==2 and modo==2):
        T2J2=msj
    con=1
    msj="   A B C D E F G H I J\n"
    if(modo==1):
        if(jugador==2 and bandera==False):
            B5="1-Barco de 5 casilleros"
            B4="2-Barco de 4 casilleros"
            B3_1="3-Barco de 3 casilleros"
            B3_2="4-Barco de 3 casilleros"
            B2="5-Barco de 2 casilleros"
            bandera=True
        msj2=B5+"\n"+B4+"\n"+B3_1+"\n"+B3_2+"\n"+B2
        print(msj2)
        op = int(input(""))
        if(op==1):
            longBarco=5
            B5=""
        if(op==2):
            longBarco=4
            B4=""
        if(op==3):
            longBarco=3
            B3_1=""
        if(op==4):
            longBarco=3
            B3_2=""
        if(op==5):
            longBarco=2
            B2=""
        print("\nEn que parte del tablero desea colocarlo?(Colocar letra en mayuscula)")
        if(B5=="" and B2=="" and B3_1=="" and B3_2=="" and B4 =="" and jugador==2 and modo==1):
            modo=2
            jugador=1
    letra=input("Letra: ")
    numero=int(input("Numero: "))
    if(letra=="A"):
        posicionLetra=1
    if(letra=="B"):
        posicionLetra=2
    if(letra=="C"):
        posicionLetra=3
    if(letra=="D"):
        posicionLetra=4
    if(letra=="E"):
        posicionLetra=5
    if(letra=="F"):
        posicionLetra=6
    if(letra=="G"):
        posicionLetra=7
    if(letra=="H"):
        posicionLetra=8
    if(letra=="I"):
        posicionLetra=9
    if(letra=="J"):
        posicionLetra=10
    A=numero-1
    B=posicionLetra-1
    if(modo==1):
        op2=int(input("Hacia que lado?\n1-ARRIBA\n2-ABAJO\n3-IZQUIERDA\n4-DERECHA\n"))
        os.system("cls")
        while(longBarco>0):
            if(jugador==1):
                if(longBarco==5 or p5==1):
                    BARCO5.append([A,B])
                    p5=1
                if(longBarco==4 or p4==1):
                    BARCO4.append([A,B])
                    p4=1
                if(longBarco==3 or p3_1==1):
                    BARCO3_1.append([A,B])
                    p3_1=1
                if(longBarco==3 or p3_2==1):
                    BARCO3_2.append([A,B])
                    p3_2=1
                if(longBarco==2 or p2==1):
                    BARCO2.append([A,B])
                    p2=1
                if(tablero1J1[A][B]=="-"):
                    tablero1J1[A][B]="x"
                    longBarco=longBarco-1                
                else:
                    print("\nNO PUEDES PONER BARCOS SUPERPUESTOS!!!")
                    fin=True
                    break
            if(jugador==2):
                if(tablero1J2[A][B]=="-"):
                    tablero1J2[A][B]="x"
                    longBarco=longBarco-1
                else:
                    print("\nNO PUEDES PONER BARCOS SUPERPUESTOS!!!")
                    fin=True
                    break
            if(op2==1):
                A=A-1
            if(op2==2):
                A=A+1
            if(op2==3):
                B=B-1
            if(op2==4):
                B=B+1
        p5=0
        p4=0
        p3_1=0
        p3_2=0
        p2=0
        if(B5=="" and B2=="" and B3_1=="" and B3_2=="" and B4 =="" and jugador==1 and modo==1):
            print("GENIAL! ES EL TURNO DEL JUGADOR NUMERO 2, PRESIONE ENTER PARA CONTINUAR")
            car=input("")
            jugador=2
    if(modo==2):
        if(jugador==1):
            if(tablero1J2[A][B]=="x"):
                tablero2J1[A][B]=="x"
            else:
                tablero2J1[A][B]=="o"
                jugador=2
        if(jugador==2):
            if(tablero1J1[A][B]=="x"):
                tablero2J2[A][B]="x"
            else:
                tablero2J1[A][B]="o"
                jugador=1
        for i in range(0,5):
            for k in range(0,5):
                if(tablero2J1[A][B]=="x" or tablero2J2[A][B]=="x"):
                    if(BARCO5[i][k]==A and BARCO5[i][k+1]==B):
                        if(pun==0):
                            BarcoAtacado=5
                        pun=1
                    if(BARCO4[i][k]==A and BARCO4[i][k+1]==B):
                        if(pun==0):
                            BarcoAtacado=4
                        pun=1
                    if(BARCO3_1[i][k]==A and BARCO3_1[i][k+1]==B):
                        if(pun==0):
                            BarcoAtacado=3
                        pun=1
                    if(BARCO3_2[i][k]==A and BARCO3_2[i][k+1]==B):
                        if(pun==0):
                            BarcoAtacado=3
                        pun=1
                    if(BARCO2[i][k]==A and BARCO2[i][k+1]==B):
                        if(pun==0):
                            BarcoAtacado=2
                        pun=1
                    if(pun==1):      
                        BarcoAtacado-=1
        if(BarcoAtacado==0):
            print("BARCO HUNDIDO!!!")
            pun=0
        if(T2J1==T1J2):
            print("GANO EL JUGADOR 1!! FELICIDADES")
            fin=True
        if(T2J2==T1J1):
            print("GANO EL JUGADOR 2!! FELICIDADES")
            fin=True