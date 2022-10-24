import os
palabraoculta=[]
palabra=[]
cantidad=0
letra=""
fin=False
aciertos=0
fallos=0
cantidad=int(input("ingresar cantidad de letras: "))
for i in range(0,cantidad):
    msj="Ingresar letra " + str(i+1) + ": "
    letra=input(msj)
    palabraoculta.append(letra)
    palabra.append("-")
    os.system("cls")
while(fin==False):
    b=0
    msj=""
    for i in range (0, len(palabra)):
        msj=msj + " " + palabra[i]
    print(msj)
    letra=input("Ingresar letra ")
    for i in range(0,len(palabraoculta)):
        if (letra==palabraoculta[i] and palabra[i]== "-"):
            palabra[i]=letra
            aciertos=aciertos+1
            b=1
    if(aciertos==cantidad):
        fin=True
    if(b==0):
        fallos=fallos+1
    if(fallos==5):
        fin=True
msj= ""
for i in range (0, len(palabra)):
    msj=msj + palabraoculta[i]
print("La palabra era:" + msj)
if(aciertos==cantidad):
    print("YOU WIN")
else:
    print("YOU LOSE")
print("Aciertos: " + str(aciertos))
print("Fallos: " + str(fallos))
