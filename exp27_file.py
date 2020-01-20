str1=open("exp24","r") #exp24 is file
str1=str1.read()
list1=list(str1.split())
for i in range(len(list1)):
    list2=[]
    list2=list(list1[i])

    if list2[0]=="m" and len(list2)==5:
        print(list1[i])