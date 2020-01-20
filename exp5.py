num=int(input("enter a number:"))
def getfactors(num):
    for i in range(1,num+1):
        if num%i==0:
            print(i)
getfactors(num)
