def insertionSort(arr):
    for i in range(1, len(arr)):
        tmp = arr[i]
        j = i - 1;
        while (j >= 0 and ord(arr[j]) > ord(tmp)):
            arr[j + 1] = arr[j]
            j = j - 1
            arr[j + 1] = tmp

string="welcome"
arr=list(string)
insertionSort(arr)
string=''.join(arr)
print(string)