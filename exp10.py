import random
num=int(input("number of element in list a"))
start=int(input("starting range of list"))
end=int(input("ending range of list"))
a=[]
for i in range(num):
    a.append(random.randint(start,end))
b=[]
for i in a:
    if i%2==0:
        b.append(i)
print(b)