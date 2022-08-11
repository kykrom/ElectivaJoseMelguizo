import random

list=[]
x=random.randint(0,100)
y=random.randint(0,100)
i=x
while x > y:
        y=random.randint(0,100)
j=0
for i in range(x,y):
    list.append(j)
    z = random.randint(0,100)
    list[j] = z
    print(list[j])
    j+=1