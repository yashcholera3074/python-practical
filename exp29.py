import string
import random

def main():
    size=int(input("length of password?"))
    chars=string.ascii_letters +string.digits +string.punctuation
    print(''.join((random.choice(chars) for i in range(size))))
if __name__=='__main__':
    main()
