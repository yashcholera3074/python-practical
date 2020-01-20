num=int(input("enter a number to find it's divisors:"))
new=[]
if num>1:
    for i in range(2,(num//2)+1):
        if(num%i==0 and (num//i)%2==0):
            new.append(i)
print("divisor of",num,"is:",new)