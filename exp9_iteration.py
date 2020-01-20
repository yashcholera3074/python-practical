abc=input("enter a string")
abc=abc.replace(" ","")
lis=list(abc)
lis2=set(lis)
for i in lis2:
    if i in lis:
        count=abc.count(i)
    print(i,":",count)