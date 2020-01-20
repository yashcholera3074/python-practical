num=int(input("enter a number to check:"))
num2=int(input("enter number to divide by first number:"))

if(num%4==0):
    print("number is even and multiple of 4")
elif(num%4!=0 and num%2==0):
    print(num,"is even but but not multiple of 4 ")
else:
    print(num,"is odd and not multiple of 4")
if (num2//num)%2==0:
    print(num,"divide",num2,"evenly")
else:
    print(num,"divide",num2,"oddly")