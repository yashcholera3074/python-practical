num=int(input("enter a number to check number is prime or not:"))
def isPrime(num):
    if num > 1:
        for i in range(2, num // 2):
            if num % i == 0:
                print("{} is not prime number".format(num))
                break
        else:
            print("{} is prime number".format(num))
    else:
        print("1 is not a prime number")
isPrime(num)