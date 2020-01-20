str=input("enter a string")
first=list(str)
for i in range((len(first)//2)):
    if first[i]!=first[len(first)-i-1]:
        print("string is not palindrome")
        break
    print("string is palindrome")
    break