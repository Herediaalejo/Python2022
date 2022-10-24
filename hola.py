suma=0
con=0
num=0
prom=0
while(con<10):
    print("Ingresar Numero")
    num=int(input())
    suma+=num
    con+=1
prom=suma/con
resultado="EL PROMEDIO ES: " + str(prom)
print(resultado)
#str = string
#int = entero
#float = Real
#bool = booleano
