f= open("exp24","r")
count=0

for line in f:
    count+=1
print("number of lines:",count)
f1=set(open("exp24").read().split())
print("number of unique words:",len(f1))
