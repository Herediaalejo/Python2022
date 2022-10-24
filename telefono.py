mat=[]
i=1
op=0
b=0
mat.append([""]*4)
mat[0][0]="dni"
mat[0][1]="nombre"
mat[0][2]="apellido"
mat[0][3]="telefono"
fin=False
car=""
while(fin==False):
    msj="1-agregar\n2-buscar\n3-imprimir\n4-salir\n"
    op=int(input(msj))
    if(op==1):
        dni=input("Ingresar dni: ")
        nom=input("Ingresar nombre: ")
        ape=input("Ingresar apellido: ")
        tel=input("Ingresar telefono: ")
        mat.append([""]*4)
        mat[i][0]=dni
        mat[i][1]=nom
        mat[i][2]=ape
        mat[i][3]=tel
        i=i+1
    if(op==4):
        fin=True
    if(op==2):
        dni=input("Ingresar dni: ")
        for f in range(0,i):
            for c in range(0,4):
                if(dni==mat[f][c]):
                    b=1
                    nom=mat[f][1]
                    ape=mat[f][2]
                    tel=mat[f][3]
                    msj="Dni: " + dni + " Nombre: " + nom + " Apellido: " + ape + " Telefono: " + tel
                    print(msj)
                    car=input("Presione una tecla para continuar ")
        if(b==0):
            print("cliente inexistente")
    if(op==3):
        msj=""
        for l in range(0, i):
            msj= msj + mat[l][0] + "        " + mat[l][1] + "               " + mat[l][2] + "               " + mat[l][3] + "           " + "\n"
        print(msj)