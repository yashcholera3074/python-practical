num=int(input("number of element in list:"))
list1=[]
list2=[]
def useLoop(num):
    for i in range(num):
        list1.append(input())
    for i in list1:
        if i not in list2:
            list2.append(i)
    return list2
print(useLoop(num))