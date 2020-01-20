a=[1,1,2,3,5,8,13,21,34,55,89]
new=[]
new2=[]
for x in a:
    if x<5:
        new.append(x)


num=int(input("enter number to get numbers in list whose value is less than that number:"))
for x in a:
    if x<num:
       new2.append(x)
print("list of number whose value is less than 5 is:",new)
print("list of number whose value are less then",num,"is:",new2)