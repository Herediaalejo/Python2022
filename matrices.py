numero=0
Msj=""
Mat=[]
Filas=2
col=3
for i in range(0, Filas):
    Mat.append([0]*col)
print(Mat)
for i in range(0, Filas):
    for j in range(0, col):
        numero=int(input("Ingresar Numero: " + str(i) + "," + str(j) +":"))
        Mat[i][j]=numero
print(Mat)
for i in range(0,Filas):
    for j in range(0, col):
        #print(Mat[i][j])
        Msj=Msj+""+str(Mat[i][j]) + "/"
    Msj=Msj+ "\n"
print(Msj)
for i in range(0,Filas):
    print(Mat[i])
