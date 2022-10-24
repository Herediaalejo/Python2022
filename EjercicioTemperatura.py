#cargar dos vectores de 10 elementos cada una con las temperaturas maxima y minima.
#calcular temperatura maxima y minima
#a)la mayor temperatura minima
#b)la menor temperatura maxima
#c)promedio de la temperatura maxima
#d)El dia de mayor temperatura 
#e)El dia de menor temperatura 


vec1=[30,20,17,15,19,21,31,25,21,15]
vec2=[10,8,4,2,5,7,15,9,4,1] 
mayorMin=0
menorMax=0
mayor1=0
menor1=0
dia=0
dia1=0
prom=0
suma=0



for i in range(0,len(vec1)):
    if(i==0):
        mayorMin=vec2[i]
        menorMax=vec1[i]
        mayor1=vec1[i]
        menor1=vec2[i]
    
    if(mayorMin < vec2[i]):
        mayorMin=vec2[i]

    if(menorMax > vec1[i]):
        menorMax=vec1[i]
    
    suma=suma+vec1[i]

    if(mayor1 < vec1[i]):
        mayor1=vec1[i]
        dia=i + 1
    
    if(menor1 > vec2[i]):
        menor1=vec2[i]
        dia1=i+1

prom= suma/ len(vec1)

print(f"""
La mayor temperatura minima es: {mayorMin}°
La menor temperatura máxima es:  {menorMax}°
El promedio de la temperatura maxima es: {prom}
El día {dia} fue de mayor temperatura de {mayor1}°
El día {dia1} fue de menor temperatura de {menor1}°
""")
