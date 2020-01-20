string1=(input("enter a string1:"))
string2=(input("enter a string2:"))
list1=list(string1.lower())
list2=list(string2.lower())
if(len(list1)==len(list2)):
    for i in range(len(list1)):
        if(list1[i] is not list2[i]):
            print("string does not match")
            break
    else:
        print("string match")
else:
    print("string does not match")