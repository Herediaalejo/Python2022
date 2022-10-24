vecnombre=["jose", "juan", "flor"]
vec1=[8,5,10]
vec2=[9.8.8]
promocionados=""
prom=0
mayorprom=0
mayornombre=0
for i in range (0, len(vecnombre)):
    if(vec[i]>=7 and vec2[i]>=7):
        promocionados= (f"""
        nombre{vecnombre[i]}
        nota 1: {vec2[i]}
        nota 2: {vec2[i]}
        """)
        print(promocionados)
        prom= vec1[i] + vec2[i]/2
        if(i==0):
            mayorprom=prom
        if(prom>mayorprom):
            mayorprom=prom
            mayornombre=mayornombre[i]
print(prom)
print(f"""
El Mayor promedio {mayorprom}
nombre: {mayornombre}
""")