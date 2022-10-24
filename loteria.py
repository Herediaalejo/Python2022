import random
vec=[]
num=0
pollo=0

num= random.randint(0,10)
vec.append(num)
pollo= int(input("adivina que numero entre 0 y 10 estoy pensando: "))
if (pollo==vec[0]):
    print ("you win")
else:
    print("you lose")


