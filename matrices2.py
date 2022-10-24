matriz=[]
num=0
msj=""
for i in range(0, 4):
    matriz.append([1]*4)
print(matriz)
for i in range(0,4):
    for j in range(0,4):
        num=int(input("Ingrese numero: "))
        matriz[i][j]=num
print(matriz)
matriz[3][3]=20
for i in range(0,4):
    msj= msj + str(matriz[i]) + "\n"
print(msj)
for i in range(0,4):
    for k in range(0,4):
        msj=msj+" "+str(matriz[i][k])
    msj=msj+"\n"
print(msj)
for i in range(0,4):
    print(matriz[i])
