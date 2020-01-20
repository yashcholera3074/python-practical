class Complex:
    def __init__(self,rl,img):
        self.rl=rl
        self.img=img

    def __add__(self, other):
        return self.rl+other.rl,self.img+other.img

    def __str__(self):
        return self.rl,self.img

complex=[]
for i in range(1,3):
    print("enter complex number {}".format(i))
    rl=int(input("enter real number"))
    img=int(input("enter imaginary number"))
    complex.append(Complex(rl,img))
print("addition of complex numbers are:",complex[0]+complex[1])
