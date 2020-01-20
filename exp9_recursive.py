def count(string, ch):
    if not string:
        return 0
    elif string[0] == ch:
        return 1 + count(string[1:], ch)
    else:
        return count(string[1:], ch)


string = input("Enter a string:")
lis=set(list(string.replace(" ","")))
for ch in lis:
    print(ch,":",count(string,ch))