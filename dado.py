from calendar import c
import random
con = 0
con123 = 0
con3 = 0
con6 = 0
num = 0
while con<100:
    num= random.randint(1, 6)
    if num==3:
        con3+=1
    if num==3 or num==2 or num==1:
        con123+=1
    if num<6:
        con6+=1
    con+=1
pr3=con3/con
pr123=con123/con
pr6=con6/con
print("probabilidad de que salga 3: " + str(pr3))
print("probabilidad de que salga 1,2 o 3: " + str(pr123))
print("probabilidad de que salga uno menor a 6: " + str(pr6))
print(help(random))