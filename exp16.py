class Student:
    def __init__(self,r_no,name,age,marks):
        self.r_no = r_no
        self.name = name
        self.age = age
        self.marks = marks

    def displayStudent(self,other):
        if self.marks==other.marks:
            print("student having same marks:")
            print ("Roll no : ", self.r_no, "Name : ", self.name,  ", Age: ", self.age,  ", Marks: ", self.marks)
            print ("Roll no : ", other.r_no, "Name : ", other.name,  ", Age: ", other.age,  ", Marks: ", other.marks)
stu = []
n=int(input("how many student?"))
for i in range (1,n+1):
    print("Enter Details for Students %d" % (i))
    r_no = int(input("Enter Roll no:"))
    name = input("Enter Name:")
    age = int(input("Enter Age:"))
    marks = eval(input("Enter Marks:"))
    stu.append(Student(r_no,name,age,marks))



for i in range(n-1):
    for j in range(i+1,n):
        stu[i].displayStudent(stu[j])