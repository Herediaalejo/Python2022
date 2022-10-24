from traceback import print_last


codigo=0
cantidad=0
pago=0
precio=0
cont=0
descuento=0
recargo=0
totalE=0
totalT=0
while(codigo!=999):
    print("1- Producto 1, Precio: 1000")
    print("2- Producto 2, Precio: 1500")
    print("3- Producto 3, Precio: 2000")
    print("999- Finalizar")
    print("Ingrese codigo")
    codigo=int(input(""))
    if(codigo>=1 and codigo <=3):
        print("Ingrese cantidad")
        cantidad= int(input(""))
        print("Ingrese forma de pago:")
        print("1- Efectivo")
        print("2- Tarjeta")
        pago=int(input(""))
        if codigo==1:
            precio=1000
            cont+=cantidad
        if codigo==2:
            precio=1500
        if codigo==3:
            precio=2000
        subtotal=precio*cantidad
        if pago==1:
            if subtotal>10000:
                descuento=subtotal*0.20
                totalE= totalE+ (subtotal-descuento)
            else:
                totalE=subtotal
        if pago==2:
            recargo=subtotal*0.30
            totalT= totalT + (subtotal+recargo)    
print("El total de venta con efectivo es: $" + str(totalE))
print("El total de venta con tarjeta es: $" + str(totalT))
print("Cantidad de producto 1 vendido: " + str(cont))
