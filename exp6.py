a=[]
b=[]
lenA=int(input("enter length of list1:"))
for i in range(lenA):
    a.append(input())
lenB=int(input("enter length of list2:"))
for i in range(lenB):
    b.append(input())
c=[]
for i in a:
    for j in b:
        if i==j:
            c.append(i)
print(set(c))

