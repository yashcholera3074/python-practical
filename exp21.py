def bubbleSort(arr):
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
arr=[]
n=int(input("how many element in list?"))
print("enter {} element".format(n))
for i in range(n):
    arr.append(input())
bubbleSort(arr)
print(arr)