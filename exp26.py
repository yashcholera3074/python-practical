print("enter text to append")
with open("python.py","a") as f:
    f.write(input())
with open("python.py","r") as f:
    print(f.read())