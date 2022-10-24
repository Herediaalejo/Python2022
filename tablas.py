import Funciones
tablas = []
dim = 10
msj = ""
can = 0
for i in range(0, dim):
    tablas.append([0] * dim)
for i in range(0, dim):
    for k in range(0, dim):
        tablas[i][k] = (i+1) * (k+1)
Funciones.imprimirAlineadoTresCifras(tablas)