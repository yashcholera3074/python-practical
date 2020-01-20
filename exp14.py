num=int(input("enter how many element of fibonnaci series you want:"))
def Fibonacci(num):
    f1=0
    f2=1
    if(num<1):
        return("enter valid integer")
    for i in range(0,num):
        if i!=num-1:
            print(f2,end=",")
            new=f1+f2
            f1=f2
            f2=new
        else:
            print(f2)

Fibonacci(num)