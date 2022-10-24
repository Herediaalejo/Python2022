import random
f=0
c=0
mat=[]
n=3
b=0
num=0
con=0
for i in range(0,n):
    mat.append([0]*n)
while(con<9):
    num=random.randint(1,9)
    for i in range(0, n):
        for k in range(0, n):
            if(num==mat[i][k]):
                b=1
    if(b==0):
        mat[f][c]=num
        c=c+1
        con=con+1
        if(c>2):
            f=f+1
            c=0
    b=0
for i in range(0, n):
    print(mat[i])