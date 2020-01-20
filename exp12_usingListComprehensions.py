num=int(input("enter a number to check number is prime or not:"))
prime_list=[i for i in range (2,(num//2)+1) if num%i==0]
def isPrime(num):
    if num>1:
        if len(prime_list)!=0:
            print("{} is not prime number".format(num))
        else:
            print("{} is prime number".format(num))
    else:
        print("{} is not prime number".format(num))
isPrime(num)