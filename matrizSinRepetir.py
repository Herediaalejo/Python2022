import random
num = 0
mat = []
dim = 3
b = False
intentos=0
for i in range(0, dim):
    mat.append([0]*dim)
while(b==False):
    repetido = False
    c=False
    num = random.randint(1,9)
    if(intentos==0):
        mat[0][0]=num
        col=1
    else:
        for i in range(0, dim):
            for k in range(0, dim):
                if(mat[i][k]==num):
                    repetido=True
        if (repetido==False):
            for i in range(0, dim):
                for k in range(0, dim):
                    if(mat[i][k]==0 and c==False):
                        mat[i][k]=num
                        c=True
                    if (mat[i][k]!=0):
                        b=True
                    else:
                        b=False
    intentos=intentos+1
for i in range(0, dim):
    print(mat[i])
                    
        
            

                    


