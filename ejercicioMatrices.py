import random
filas=0
col=0
mat=[]
mat2=[]
num=0
suma=0
con5=0
promedio=0
filas=int(input("Ingrese numero de filas:\n"))
col=int(input("Ingrese numero de columnas:\n"))
for i in range(0, filas):
    mat.append([0]*col)
for i in range(0, filas):
    for j in range(0, col):
        num=random.randint(1,50)
        if(num%5==0):
            suma=suma+num
            con5=con5+1
        mat[i][j]=num
print(mat)
print("\n")
for i in range(0, filas):
    print(mat[i])
promedio=suma/con5
print("El promedio de los divisibles por 5 es: " + str(promedio))
for i in mat:
    print(i)
for i in range(0,filas):
    mat2.append([0]*col)
i=0
j=0
con=0
while(con<(filas*col)):
    num=random.randint(1,50)
    if(j==col):
        i=i+1
        j=0
    if(num%5==0):
        mat2[i][j]=num
        con=con+1
        j=j+1
for i in mat2:
    print(i)