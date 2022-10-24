from traceback import print_stack


vec1= []
vec2= []
vec3= []
nom= ""
nota1=0
nota2=0
promedio=0
mayorP=0
IndiceMayor=0
for i in range (0, 5) :
    print ("Ingrese el nombre")
    nombre= input("")
    vec1.append(nombre)
    print ("Ingrese la primera nota")
    nota1= int(input(""))
    vec2.append(nota1)
    print ("Ingrese la segunda nota")
    nota2= int(input(""))
    vec3.append(nota2)
for i in range (0, 5) :
    promedio = (vec2[i] + vec3[i]) / 2
    if(vec2[i] >= 7 and vec3[i] >= 7):
        print(vec1[i] + " " + str(vec2[i]) + " " + str(vec3[i]))
    if(promedio>=mayorP):
        IndiceMayor=i
        mayorP=promedio
print ("El promedio mas alto es: " + vec1[IndiceMayor] + " " + str(mayorP))


