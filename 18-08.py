import random
vec1= []
vec2= []
vec3= []
num1= 0
num2=0
for i in range (0, 10):
    num1=random.randint(1, 11)
    num2=random.randint(1, 11)
    vec1.append(num1)
    vec2.append(num2)
    vec3.append(num1*num2)
for i in range (0, len(vec1)):
    print(str(vec1[i]) + " x "+ str(vec2[i]) + " = " + str(vec3[i]))
