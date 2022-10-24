"""Ingresar por teclado la dimension de una matriz cuadrada y completarla con numeros aleatorios(1 al 20).
a)Calcular promedio de la diagonal superior
b)El menor de la diagonal inferior
c)Calcular el porcentaje de numeros divisibles por 2 y 3 de las columnas pares"""

import random
from traceback import print_last

n = 0
num = 0
mat = []
msj = ""
suma=0
con=0
prom=0
menor=0
por23=0
div23=0
cant=0
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
        if(j<i):
            if(i==1):
                menor=num
            if(num<menor):
                menor=num
        if(j%2==0):
            cant=cant+1
            if(num%2==0 and num%3==0):
                div23=div23+1
    msj = msj + "\n" 
print (msj)
prom=suma/con
print(prom)
print(menor)
por23=(div23*100)/cant
print("Porcentaje de numero div por 2 y 3 de las columnas pares: ")
print(str(por23)+" %")



    



