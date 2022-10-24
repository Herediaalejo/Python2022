import random
from traceback import print_last
"""fila = 0
col = 0
num = 0
vec = []
fila = int(input("Ingrese numero de filas/columnas: "))
col = fila
for i in range (0, fila):
    vec.append([0]*col)
for i in range(0, fila):
    for j in range(0, col):
        num=random.randint(1,20)
        vec[i][j]=num
for i in range(0, fila):
    print(vec[i])"""""

n = 0
num = 0
mat = []
msj = ""
suma=0
con=0
prom=0
n = int(input("Ingres dimension de la matriz: "))
for i in range(0, n):
    mat.append([0]*n)
for i in range(0, n):
    for j in range(0, n):
        num=random.randint(1,20)
        mat[i][j]=num
        msj = msj + " - " + str(num)
        if (j>i):
            suma=suma+num
            con=con+1
    msj = msj + "\n" 
print (msj)
prom=suma/con
print(prom)


    



