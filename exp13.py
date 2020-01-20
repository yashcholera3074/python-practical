num=int(input("enter number of element of list:"))
def List(num):
    a=[]
    b=[]
    for i in range(num):
        a.append(input())
    b.append(a[0])
    b.append(a[len(a)-1])
    print(b)
List(num)