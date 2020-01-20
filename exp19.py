def binarySearch(arr,x):
    l=0
    r=len(arr)-1
    while l <= r:

        mid = l + (r - l) // 2;

        if arr[mid] == x:
            return mid

        elif arr[mid] < x:
            l = mid + 1

        else:
            r = mid - 1
    return -1

arr = [];
n = int(input("how many element in list?"))
print("enter a list in sorted order")
for i in range(n):
    arr.append(input())
x = input("enter a name you want to search:")
result = binarySearch(arr, x)
if (result != -1):
    print("{} found at position".format(x),
          result + 1)
else:
        print("{} not found in list".format(x))
